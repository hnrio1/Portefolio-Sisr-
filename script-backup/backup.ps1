#==============================================================================
# Script de Backup Automatise - Windows PowerShell
# Auteur : Henrio Chambal - BTS SIO SISR
# Description : Sauvegarde de dossiers avec compression et rotation
#==============================================================================

# === CONFIGURATION ===
$SourcePath = "C:\Users\$env:USERNAME\Documents"      # Dossier a sauvegarder
$DestinationPath = "C:\Backup"                        # Dossier de destination
$BackupName = "backup"                                # Prefixe du nom de fichier
$MaxBackups = 5                                       # Nombre de backups a conserver

# === FONCTIONS ===

function Write-Log {
    param([string]$Message, [string]$Type = "INFO")
    $Date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Color = switch ($Type) {
        "INFO"    { "White" }
        "SUCCESS" { "Green" }
        "WARNING" { "Yellow" }
        "ERROR"   { "Red" }
    }
    Write-Host "[$Date] [$Type] $Message" -ForegroundColor $Color
}

# === SCRIPT PRINCIPAL ===

# En-tete
Clear-Host
Write-Host ""
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "                    SCRIPT DE BACKUP                          " -ForegroundColor Cyan
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""

# Verifier que le dossier source existe
if (-Not (Test-Path $SourcePath)) {
    Write-Log "Le dossier source n'existe pas : $SourcePath" "ERROR"
    exit 1
}

# Creer le dossier de destination s'il n'existe pas
if (-Not (Test-Path $DestinationPath)) {
    Write-Log "Creation du dossier de destination : $DestinationPath" "INFO"
    New-Item -ItemType Directory -Path $DestinationPath -Force | Out-Null
}

# Generer le nom du fichier avec la date
$Date = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$BackupFileName = "${BackupName}_${Date}.zip"
$BackupFullPath = Join-Path $DestinationPath $BackupFileName

# Afficher les infos
Write-Log "Source       : $SourcePath" "INFO"
Write-Log "Destination  : $BackupFullPath" "INFO"

# Creer le backup
Write-Log "Compression en cours..." "INFO"
try {
    Compress-Archive -Path "$SourcePath\*" -DestinationPath $BackupFullPath -Force
    $Size = (Get-Item $BackupFullPath).Length / 1MB
    Write-Log "Backup cree avec succes ! Taille : $([math]::Round($Size, 2)) MB" "SUCCESS"
} catch {
    Write-Log "Erreur lors de la compression : $_" "ERROR"
    exit 1
}

# Rotation des backups (supprimer les anciens)
Write-Log "Verification de la rotation des backups..." "INFO"
$Backups = Get-ChildItem -Path $DestinationPath -Filter "${BackupName}_*.zip" | Sort-Object CreationTime -Descending

if ($Backups.Count -gt $MaxBackups) {
    $ToDelete = $Backups | Select-Object -Skip $MaxBackups
    foreach ($File in $ToDelete) {
        Write-Log "Suppression de l'ancien backup : $($File.Name)" "WARNING"
        Remove-Item $File.FullName -Force
    }
}

# Resume
Write-Host ""
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "                    BACKUP TERMINE                            " -ForegroundColor Cyan
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Log "Backups conserves : $([math]::Min($Backups.Count, $MaxBackups)) / $MaxBackups" "INFO"
Write-Host ""

# Liste des backups existants
Write-Host "Backups disponibles :" -ForegroundColor Yellow
Get-ChildItem -Path $DestinationPath -Filter "${BackupName}_*.zip" |
    Sort-Object CreationTime -Descending |
    ForEach-Object {
        $Size = [math]::Round($_.Length / 1MB, 2)
        Write-Host "  - $($_.Name) ($Size MB)" -ForegroundColor White
    }

Write-Host ""
Read-Host "Appuyez sur Entree pour quitter"
