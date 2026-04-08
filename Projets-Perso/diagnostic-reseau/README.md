# Script de Diagnostic Réseau

> **Auteur** : Henrio Chambal - BTS SIO 2 SISR
> **Environnement** : Windows (PowerShell) / Linux (Bash)

## Description

Scripts d'audit rapide de la configuration réseau d'une machine. Utile pour diagnostiquer des problèmes de connectivité ou faire un état des lieux d'une machine.

## Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| Infos système | Nom machine, OS, utilisateur |
| Configuration réseau | IP, masque, passerelle, DNS, MAC |
| Test de connectivité | Ping vers passerelle, DNS, Internet |
| Ports en écoute | Liste des ports TCP ouverts |
| Services réseau | État des services (DHCP, DNS, SSH...) |
| Table ARP | Machines connues sur le réseau |
| Connexions actives | Connexions TCP établies |

## Utilisation

### Windows (PowerShell)

```powershell
# Ouvrir PowerShell en Administrateur
# Se placer dans le dossier du script
cd C:\chemin\vers\diagnostic-reseau

# Autoriser l'exécution de scripts (si nécessaire)
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Lancer le script
.\diagnostic.ps1
```

### Linux (Bash)

```bash
# Rendre le script exécutable
chmod +x diagnostic.sh

# Lancer le script (avec sudo pour toutes les infos)
sudo ./diagnostic.sh
```

## Aperçu

```
  ____  _                             _   _
 |  _ \(_) __ _  __ _ _ __   ___  ___| |_(_) ___
 | | | | |/ _` |/ _` | '_ \ / _ \/ __| __| |/ __|
 | |_| | | (_| | (_| | | | | (_) \__ \ |_| | (__
 |____/|_|\__,_|\__, |_| |_|\___/|___/\__|_|\___|
                |___/           Reseau - Windows

==============================================================
  INFORMATIONS SYSTEME
==============================================================
Nom de la machine    : PC-HENRIO
Systeme d'exploitation: Microsoft Windows 11 Pro
...

==============================================================
  CONFIGURATION RESEAU
==============================================================
--- Ethernet ---
  Adresse MAC        : AA-BB-CC-DD-EE-FF
  Adresse IP         : 192.168.1.10
  Masque (CIDR)      : /24
  Passerelle         : 192.168.1.1
  Serveurs DNS       : 192.168.1.1, 8.8.8.8
...

==============================================================
  TEST DE CONNECTIVITE
==============================================================
  [OK] Passerelle locale (192.168.1.1)
  [OK] DNS Google (8.8.8.8)
  [OK] Google.com (google.com)
  [OK] Cloudflare DNS (1.1.1.1)
```

## Prérequis

### Windows
- PowerShell 5.0 ou supérieur
- Droits administrateur (recommandé)

### Linux
- Bash
- Outils : `ip`, `ping`, `ss` ou `netstat`
- Droits root pour certaines infos (sudo)

## Cas d'utilisation

- **Diagnostic de panne réseau** : Vérifier rapidement la config IP et la connectivité
- **Audit de sécurité** : Voir les ports ouverts et connexions actives
- **Documentation** : État des lieux d'une machine avant intervention
- **Support technique** : Récupérer les infos réseau d'un utilisateur

## Structure du projet

```
diagnostic-reseau/
├── README.md           # Documentation
├── diagnostic.ps1      # Script Windows (PowerShell)
└── diagnostic.sh       # Script Linux (Bash)
```

## Compétences démontrées

- Scripting PowerShell et Bash
- Administration réseau (TCP/IP, DNS, DHCP)
- Diagnostic et troubleshooting
- Documentation technique
