#!/bin/bash
#==============================================================================
# Script de Backup Automatise - Linux Bash
# Auteur : Henrio Chambal - BTS SIO SISR
# Description : Sauvegarde de dossiers avec compression et rotation
#==============================================================================

# === CONFIGURATION ===
SOURCE_PATH="/home/$USER/Documents"      # Dossier a sauvegarder
DEST_PATH="/home/$USER/Backup"           # Dossier de destination
BACKUP_NAME="backup"                     # Prefixe du nom de fichier
MAX_BACKUPS=5                            # Nombre de backups a conserver

# === COULEURS ===
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# === FONCTIONS ===
log() {
    local TYPE=$1
    local MESSAGE=$2
    local DATE=$(date '+%Y-%m-%d %H:%M:%S')
    case $TYPE in
        "INFO")    echo -e "[$DATE] [${NC}INFO${NC}] $MESSAGE" ;;
        "SUCCESS") echo -e "[$DATE] [${GREEN}SUCCESS${NC}] $MESSAGE" ;;
        "WARNING") echo -e "[$DATE] [${YELLOW}WARNING${NC}] $MESSAGE" ;;
        "ERROR")   echo -e "[$DATE] [${RED}ERROR${NC}] $MESSAGE" ;;
    esac
}

# === SCRIPT PRINCIPAL ===

# En-tete
clear
echo ""
echo -e "${CYAN}==============================================================${NC}"
echo -e "${CYAN}                    SCRIPT DE BACKUP                          ${NC}"
echo -e "${CYAN}==============================================================${NC}"
echo ""

# Verifier que le dossier source existe
if [ ! -d "$SOURCE_PATH" ]; then
    log "ERROR" "Le dossier source n'existe pas : $SOURCE_PATH"
    exit 1
fi

# Creer le dossier de destination s'il n'existe pas
if [ ! -d "$DEST_PATH" ]; then
    log "INFO" "Creation du dossier de destination : $DEST_PATH"
    mkdir -p "$DEST_PATH"
fi

# Generer le nom du fichier avec la date
DATE=$(date '+%Y-%m-%d_%H-%M-%S')
BACKUP_FILE="${BACKUP_NAME}_${DATE}.tar.gz"
BACKUP_FULL_PATH="${DEST_PATH}/${BACKUP_FILE}"

# Afficher les infos
log "INFO" "Source       : $SOURCE_PATH"
log "INFO" "Destination  : $BACKUP_FULL_PATH"

# Creer le backup
log "INFO" "Compression en cours..."
if tar -czf "$BACKUP_FULL_PATH" -C "$(dirname $SOURCE_PATH)" "$(basename $SOURCE_PATH)" 2>/dev/null; then
    SIZE=$(du -h "$BACKUP_FULL_PATH" | cut -f1)
    log "SUCCESS" "Backup cree avec succes ! Taille : $SIZE"
else
    log "ERROR" "Erreur lors de la compression"
    exit 1
fi

# Rotation des backups (supprimer les anciens)
log "INFO" "Verification de la rotation des backups..."
BACKUP_COUNT=$(ls -1 "${DEST_PATH}/${BACKUP_NAME}_"*.tar.gz 2>/dev/null | wc -l)

if [ "$BACKUP_COUNT" -gt "$MAX_BACKUPS" ]; then
    TO_DELETE=$((BACKUP_COUNT - MAX_BACKUPS))
    ls -1t "${DEST_PATH}/${BACKUP_NAME}_"*.tar.gz | tail -n "$TO_DELETE" | while read FILE; do
        log "WARNING" "Suppression de l'ancien backup : $(basename $FILE)"
        rm -f "$FILE"
    done
fi

# Resume
echo ""
echo -e "${CYAN}==============================================================${NC}"
echo -e "${CYAN}                    BACKUP TERMINE                            ${NC}"
echo -e "${CYAN}==============================================================${NC}"
echo ""

# Liste des backups existants
echo -e "${YELLOW}Backups disponibles :${NC}"
ls -1t "${DEST_PATH}/${BACKUP_NAME}_"*.tar.gz 2>/dev/null | while read FILE; do
    SIZE=$(du -h "$FILE" | cut -f1)
    echo "  - $(basename $FILE) ($SIZE)"
done

echo ""
read -p "Appuyez sur Entree pour quitter..."
