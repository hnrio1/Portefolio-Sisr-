#!/bin/bash
#==============================================================================
# Script de Diagnostic Reseau - Linux Bash
# Auteur : Henrio Chambal - BTS SIO SISR
# Description : Audit rapide de la configuration reseau d'une machine Linux
#==============================================================================

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
WHITE='\033[1;37m'

# Fonctions d'affichage
print_header() {
    echo ""
    echo -e "${CYAN}==============================================================${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}==============================================================${NC}"
}

print_subheader() {
    echo ""
    echo -e "${YELLOW}--- $1 ---${NC}"
}

# En-tete du script
clear
echo ""
echo -e "${GREEN}  ____  _                             _   _      ${NC}"
echo -e "${GREEN} |  _ \(_) __ _  __ _ _ __   ___  ___| |_(_) ___ ${NC}"
echo -e "${GREEN} | | | | |/ _' |/ _' | '_ \ / _ \/ __| __| |/ __|${NC}"
echo -e "${GREEN} | |_| | | (_| | (_| | | | | (_) \__ \ |_| | (__ ${NC}"
echo -e "${GREEN} |____/|_|\__,_|\__, |_| |_|\___/|___/\__|_|\___|${NC}"
echo -e "${GREEN}                |___/             Reseau - Linux ${NC}"
echo ""
echo -e "  Auteur : Henrio Chambal - BTS SIO SISR"
echo -e "  Date   : $(date '+%d/%m/%Y %H:%M:%S')"

#==============================================================================
# 1. INFORMATIONS SYSTEME
#==============================================================================
print_header "INFORMATIONS SYSTEME"

echo -e "${WHITE}Nom de la machine    : $(hostname)${NC}"
echo -e "${WHITE}Systeme              : $(uname -s)${NC}"
echo -e "${WHITE}Version kernel       : $(uname -r)${NC}"
echo -e "${WHITE}Distribution         : $(cat /etc/os-release 2>/dev/null | grep "PRETTY_NAME" | cut -d'"' -f2)${NC}"
echo -e "${WHITE}Utilisateur actuel   : $(whoami)${NC}"
echo -e "${WHITE}Uptime               : $(uptime -p 2>/dev/null || uptime)${NC}"

#==============================================================================
# 2. CONFIGURATION RESEAU
#==============================================================================
print_header "CONFIGURATION RESEAU"

# Detecter les interfaces actives
INTERFACES=$(ip -o link show | awk -F': ' '{print $2}' | grep -v lo)

for IFACE in $INTERFACES; do
    # Verifier si l'interface est UP
    STATE=$(ip link show $IFACE | grep -o "state [A-Z]*" | awk '{print $2}')

    if [ "$STATE" = "UP" ]; then
        print_subheader "$IFACE ($STATE)"

        # Adresse MAC
        MAC=$(ip link show $IFACE | grep ether | awk '{print $2}')
        echo -e "${WHITE}  Adresse MAC        : $MAC${NC}"

        # Adresse IP
        IP=$(ip -4 addr show $IFACE | grep inet | awk '{print $2}')
        echo -e "${WHITE}  Adresse IP         : $IP${NC}"

        # Passerelle
        GW=$(ip route | grep default | grep $IFACE | awk '{print $3}')
        echo -e "${WHITE}  Passerelle         : $GW${NC}"

        # DNS
        DNS=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}' | tr '\n' ', ' | sed 's/,$//')
        echo -e "${WHITE}  Serveurs DNS       : $DNS${NC}"
    fi
done

#==============================================================================
# 3. TEST DE CONNECTIVITE
#==============================================================================
print_header "TEST DE CONNECTIVITE"

# Recuperer la passerelle
GATEWAY=$(ip route | grep default | awk '{print $3}' | head -1)

declare -a TARGETS=("$GATEWAY:Passerelle locale" "8.8.8.8:DNS Google" "google.com:Google.com" "1.1.1.1:Cloudflare DNS")

for TARGET in "${TARGETS[@]}"; do
    IP=$(echo $TARGET | cut -d':' -f1)
    NAME=$(echo $TARGET | cut -d':' -f2)

    if [ -n "$IP" ]; then
        if ping -c 1 -W 2 $IP &> /dev/null; then
            echo -e "  ${GREEN}[OK]${NC} $NAME ($IP)"
        else
            echo -e "  ${RED}[ECHEC]${NC} $NAME ($IP)"
        fi
    fi
done

#==============================================================================
# 4. PORTS EN ECOUTE
#==============================================================================
print_header "PORTS EN ECOUTE (TCP)"

echo ""
echo -e "${YELLOW}  Port\t\tService/PID${NC}"
echo -e "${YELLOW}  ----\t\t-----------${NC}"

if command -v ss &> /dev/null; then
    ss -tlnp 2>/dev/null | grep LISTEN | awk '{print $4}' | rev | cut -d':' -f1 | rev | sort -n | uniq | head -15 | while read PORT; do
        PROCESS=$(ss -tlnp 2>/dev/null | grep ":$PORT " | head -1 | sed 's/.*users:(("//' | cut -d'"' -f1)
        echo -e "  ${WHITE}$PORT\t\t$PROCESS${NC}"
    done
elif command -v netstat &> /dev/null; then
    netstat -tlnp 2>/dev/null | grep LISTEN | awk '{print $4, $7}' | head -15
fi

#==============================================================================
# 5. SERVICES RESEAU
#==============================================================================
print_header "SERVICES RESEAU"

SERVICES=("sshd:SSH" "apache2:Apache" "nginx:Nginx" "mysql:MySQL" "NetworkManager:Network Manager" "systemd-resolved:DNS Resolver")

for SERVICE in "${SERVICES[@]}"; do
    SVC_NAME=$(echo $SERVICE | cut -d':' -f1)
    SVC_DESC=$(echo $SERVICE | cut -d':' -f2)

    if systemctl is-active --quiet $SVC_NAME 2>/dev/null; then
        echo -e "  ${GREEN}[OK]${NC} $SVC_DESC ($SVC_NAME)"
    elif pgrep -x $SVC_NAME &> /dev/null; then
        echo -e "  ${GREEN}[OK]${NC} $SVC_DESC ($SVC_NAME)"
    else
        # Ne pas afficher si le service n'existe pas
        if systemctl list-unit-files | grep -q $SVC_NAME 2>/dev/null; then
            echo -e "  ${RED}[ARRET]${NC} $SVC_DESC ($SVC_NAME)"
        fi
    fi
done

#==============================================================================
# 6. TABLE ARP
#==============================================================================
print_header "TABLE ARP (5 dernieres entrees)"

echo ""
echo -e "${YELLOW}  Adresse IP\t\tAdresse MAC\t\t\tInterface${NC}"
echo -e "${YELLOW}  ----------\t\t-----------\t\t\t---------${NC}"

if command -v ip &> /dev/null; then
    ip neigh show | grep -v "FAILED" | head -5 | while read line; do
        IP=$(echo $line | awk '{print $1}')
        MAC=$(echo $line | awk '{print $5}')
        IFACE=$(echo $line | awk '{print $3}')
        echo -e "  ${WHITE}$IP\t\t$MAC\t$IFACE${NC}"
    done
fi

#==============================================================================
# 7. CONNEXIONS ACTIVES
#==============================================================================
print_header "CONNEXIONS ACTIVES (TCP Established)"

echo ""
if command -v ss &> /dev/null; then
    ss -tn state established 2>/dev/null | tail -n +2 | head -10 | while read line; do
        LOCAL=$(echo $line | awk '{print $3}')
        REMOTE=$(echo $line | awk '{print $4}')
        echo -e "  ${WHITE}$LOCAL <-> $REMOTE${NC}"
    done
fi

#==============================================================================
# 8. INFORMATIONS FIREWALL
#==============================================================================
print_header "FIREWALL (iptables)"

if command -v iptables &> /dev/null; then
    RULES=$(iptables -L -n 2>/dev/null | grep -c "^Chain")
    if [ "$RULES" -gt 0 ]; then
        echo -e "  ${WHITE}Nombre de chaines : $RULES${NC}"
        echo -e "  ${WHITE}Politique INPUT   : $(iptables -L INPUT -n 2>/dev/null | head -1 | awk '{print $4}' | tr -d ')')${NC}"
        echo -e "  ${WHITE}Politique OUTPUT  : $(iptables -L OUTPUT -n 2>/dev/null | head -1 | awk '{print $4}' | tr -d ')')${NC}"
    else
        echo -e "  ${YELLOW}Iptables non configure ou acces refuse${NC}"
    fi
else
    echo -e "  ${YELLOW}Iptables non installe${NC}"
fi

#==============================================================================
# FIN DU DIAGNOSTIC
#==============================================================================
echo ""
echo -e "${CYAN}==============================================================${NC}"
echo -e "${CYAN}  DIAGNOSTIC TERMINE - $(date '+%d/%m/%Y %H:%M:%S')${NC}"
echo -e "${CYAN}==============================================================${NC}"
echo ""

read -p "Appuyez sur Entree pour quitter..."
