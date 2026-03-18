# Haute Disponibilité (HeartBeat) + Load Balancing (HAProxy)

> **Auteur** : Henrio Chambal - BTS SIO 2 SISR
> **Environnement** : VMware Workstation Pro, Debian 12 (Bookworm), Client Windows

## Objectif du projet

Mettre en place une infrastructure web hautement disponible et répartie en charge :
- **HeartBeat** : Basculement automatique d'une IP virtuelle en cas de panne (failover)
- **HAProxy** : Répartition du trafic HTTP entre plusieurs serveurs (load balancing)

## Architecture

### Topologie réseau

```
                    ┌─────────────────┐
                    │  Client Windows │
                    │  172.20.0.100   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    HAProxy      │
                    │  172.20.0.10    │
                    │  (IP virtuelle) │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼────────┐    │    ┌────────▼────────┐
     │    Serv-1       │    │    │    Serv-2       │
     │  172.20.0.11    │◄───┴───►│  172.20.0.12    │
     │  Apache2        │         │  Apache2        │
     │  (THE GRILL 1)  │         │  (THE GRILL 2)  │
     └─────────────────┘         └─────────────────┘
```

### Adressage IP

| Machine | Hostname | IP | Rôle |
|---------|----------|-----|------|
| Serveur Web 1 | Serv-1 | 172.20.0.11/24 | Apache2 (THE GRILL 1) |
| Serveur Web 2 | Serv-2 | 172.20.0.12/24 | Apache2 (THE GRILL 2) |
| IP virtuelle | - | 172.20.0.10/24 | HeartBeat / HAProxy |
| Client | Windows | 172.20.0.100/24 | Tests |

---

## Partie 1 : HeartBeat (Haute Disponibilité)

### Principe

HeartBeat surveille l'état des serveurs et bascule automatiquement l'IP virtuelle vers le serveur secondaire en cas de panne du serveur principal.

### Installation

```bash
apt update && apt upgrade -y
apt install -y apache2 php heartbeat wget unzip
```

### Configuration réseau

**/etc/network/interfaces** (Serv-1)
```
auto ens33
iface ens33 inet static
    address 172.20.0.11
    netmask 255.255.255.0
```

**/etc/hosts** (sur les deux serveurs)
```
127.0.0.1   localhost
172.20.0.11 Serv-1
172.20.0.12 Serv-2
```

### Configuration HeartBeat

Créer 3 fichiers dans `/etc/ha.d/` (identiques sur Serv-1 et Serv-2) :

**1. /etc/ha.d/ha.cf**
```
logfile /var/log/heartbeat
logfacility local0
keepalive 5
deadtime 30
bcast ens33
node Serv-1 Serv-2
auto_failback on
```

**2. /etc/ha.d/haresources**
```
Serv-1 IPaddr::172.20.0.10/24/ens33 apache2
```

**3. /etc/ha.d/authkeys**
```
auth 1
1 md5 greta
```

```bash
chmod 600 /etc/ha.d/authkeys
update-rc.d apache2 remove  # HeartBeat gère Apache
```

### Démarrage et test

```bash
service apache2 stop
service heartbeat start

# Vérifier l'IP virtuelle
ip a | grep 172.20.0.10
```

### Test de basculement

1. Accéder à `http://172.20.0.10` → **The Grill 1**
2. Désactiver la carte réseau de Serv-1 (simuler panne)
3. Attendre quelques secondes
4. Rafraîchir → **The Grill 2** (basculement automatique)
5. Réactiver Serv-1 → retour automatique (failback)

---

## Partie 2 : HAProxy (Load Balancing)

### Principe

HAProxy répartit les requêtes HTTP entre les serveurs web en utilisant l'algorithme round-robin.

### Installation

```bash
apt update && apt install -y haproxy
```

### Configuration réseau HAProxy

**/etc/network/interfaces**
```
auto ens33
iface ens33 inet static
    address 172.20.0.10
    netmask 255.255.255.0

auto ens34
iface ens34 inet dhcp
```

### Configuration HAProxy

**/etc/haproxy/haproxy.cfg** (ajouter à la fin)
```
listen clusterWeb
    bind 172.20.0.10:80
    mode http
    balance roundrobin
    option httpclose
    option forwardfor
    server SRV-WEB1 172.20.0.11:80 check
    server SRV-WEB2 172.20.0.12:80 check

    stats enable
    stats hide-version
    stats refresh 30s
    stats show-node
    stats auth admin:password
    stats uri /statistique
```

```bash
service haproxy restart
```

### Test du load balancing

1. Accéder à `http://172.20.0.10`
2. Rafraîchir (F5) plusieurs fois
3. La page alterne entre **The Grill 1** et **The Grill 2**

### Interface de statistiques

- URL : `http://172.20.0.10/statistique`
- Identifiants : `admin` / `password`
- Affiche l'état des serveurs en temps réel (UP/DOWN)

### Test de panne

```bash
# Sur Serv-1
service apache2 stop
```

- Dans `/statistique` : SRV-WEB1 passe en **DOWN** (rouge)
- Le site reste accessible via SRV-WEB2
- Après `service apache2 start` : retour en **UP** (vert)

---

## Comparaison HA vs LB

| Critère | HeartBeat (HA) | HAProxy (LB) |
|---------|----------------|--------------|
| **Objectif** | Continuité de service | Répartition de charge |
| **Mécanisme** | IP virtuelle flottante | Round-robin HTTP |
| **Cas d'usage** | Un seul serveur actif à la fois | Plusieurs serveurs actifs |
| **Basculement** | Automatique sur panne | Exclusion du serveur DOWN |

---

## Compétences acquises

- Configuration de la haute disponibilité avec HeartBeat
- Mise en place d'un load balancer avec HAProxy
- Gestion des IP virtuelles
- Tests de failover et failback
- Supervision via interface de statistiques

---

## Technologies utilisées

- **OS** : Debian 12 (Bookworm)
- **Virtualisation** : VMware Workstation Pro
- **Services** : Apache2, HeartBeat, HAProxy
- **Réseau** : LAN Segment VMware

