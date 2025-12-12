# Script de Backup Automatisé

> **Auteur** : Henrio Chambal - BTS SIO 2 SISR
> **Environnement** : Windows (PowerShell) / Linux (Bash)

## Description

Scripts de sauvegarde automatisée avec compression et rotation des anciens backups. Utile pour sauvegarder des dossiers importants (documents, configurations, projets).

## Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| Compression | Archive les fichiers en .zip (Windows) ou .tar.gz (Linux) |
| Horodatage | Ajoute la date et l'heure au nom du fichier |
| Rotation | Supprime automatiquement les anciens backups |
| Logs | Affiche les étapes en temps réel |

## Configuration

Modifie les variables en haut du script selon tes besoins :

### PowerShell (Windows)

```powershell
$SourcePath = "C:\Users\$env:USERNAME\Documents"   # Dossier a sauvegarder
$DestinationPath = "C:\Backup"                     # Dossier de destination
$BackupName = "backup"                             # Prefixe du nom
$MaxBackups = 5                                    # Nombre de backups a conserver
```

### Bash (Linux)

```bash
SOURCE_PATH="/home/$USER/Documents"    # Dossier a sauvegarder
DEST_PATH="/home/$USER/Backup"         # Dossier de destination
BACKUP_NAME="backup"                   # Prefixe du nom
MAX_BACKUPS=5                          # Nombre de backups a conserver
```

## Utilisation

### Windows (PowerShell)

```powershell
# Ouvrir PowerShell et naviguer vers le dossier
cd C:\chemin\vers\script-backup

# Executer le script
.\backup.ps1
```

### Linux (Bash)

```bash
# Rendre le script executable
chmod +x backup.sh

# Executer le script
./backup.sh
```

## Aperçu

```
==============================================================
                    SCRIPT DE BACKUP
==============================================================

[2024-12-09 15:30:00] [INFO] Source       : C:\Users\henrio\Documents
[2024-12-09 15:30:00] [INFO] Destination  : C:\Backup\backup_2024-12-09_15-30-00.zip
[2024-12-09 15:30:00] [INFO] Compression en cours...
[2024-12-09 15:30:05] [SUCCESS] Backup cree avec succes ! Taille : 150.5 MB
[2024-12-09 15:30:05] [INFO] Verification de la rotation des backups...
[2024-12-09 15:30:05] [WARNING] Suppression de l'ancien backup : backup_2024-12-01_10-00-00.zip

==============================================================
                    BACKUP TERMINE
==============================================================

Backups disponibles :
  - backup_2024-12-09_15-30-00.zip (150.5 MB)
  - backup_2024-12-08_15-30-00.zip (149.2 MB)
  - backup_2024-12-07_15-30-00.zip (148.8 MB)
```

## Automatisation (optionnel)

### Windows - Planificateur de tâches

1. Ouvrir le **Planificateur de tâches**
2. Créer une tâche de base
3. Déclencheur : quotidien, hebdomadaire, etc.
4. Action : Démarrer un programme
   - Programme : `powershell.exe`
   - Arguments : `-ExecutionPolicy Bypass -File "C:\chemin\vers\backup.ps1"`

### Linux - Cron

```bash
# Editer la crontab
crontab -e

# Ajouter une ligne pour backup quotidien a 2h du matin
0 2 * * * /chemin/vers/backup.sh
```

## Structure du projet

```
script-backup/
├── README.md       # Documentation
├── backup.ps1      # Script Windows (PowerShell)
└── backup.sh       # Script Linux (Bash)
```

## Compétences démontrées

- Scripting PowerShell et Bash
- Gestion de fichiers et compression
- Automatisation de tâches système
- Rotation de logs/backups
