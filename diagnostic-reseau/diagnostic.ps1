#==============================================================================
# Script de Diagnostic Reseau - Windows PowerShell
# Auteur : Henrio Chambal - BTS SIO SISR
# Description : Audit rapide de la configuration reseau d'une machine Windows
#==============================================================================

# Couleurs pour l'affichage
function Write-Header {
    param([string]$Text)
    Write-Host ""
    Write-Host "==============================================================" -ForegroundColor Cyan
    Write-Host "  $Text" -ForegroundColor Cyan
    Write-Host "==============================================================" -ForegroundColor Cyan
}

function Write-SubHeader {
    param([string]$Text)
    Write-Host ""
    Write-Host "--- $Text ---" -ForegroundColor Yellow
}

# En-tete du script
Clear-Host
Write-Host ""
Write-Host "  ____  _                             _   _      " -ForegroundColor Green
Write-Host " |  _ \(_) __ _  __ _ _ __   ___  ___| |_(_) ___ " -ForegroundColor Green
Write-Host " | | | | |/ _' |/ _' | '_ \ / _ \/ __| __| |/ __|" -ForegroundColor Green
Write-Host " | |_| | | (_| | (_| | | | | (_) \__ \ |_| | (__ " -ForegroundColor Green
Write-Host " |____/|_|\__,_|\__, |_| |_|\___/|___/\__|_|\___|" -ForegroundColor Green
Write-Host "                |___/           Reseau - Windows " -ForegroundColor Green
Write-Host ""
Write-Host "  Auteur : Henrio Chambal - BTS SIO SISR" -ForegroundColor DarkGray
Write-Host "  Date   : $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')" -ForegroundColor DarkGray

#==============================================================================
# 1. INFORMATIONS SYSTEME
#==============================================================================
Write-Header "INFORMATIONS SYSTEME"

$OS = Get-CimInstance Win32_OperatingSystem
$Computer = Get-CimInstance Win32_ComputerSystem

Write-Host "Nom de la machine    : $($Computer.Name)" -ForegroundColor White
Write-Host "Systeme d'exploitation: $($OS.Caption)" -ForegroundColor White
Write-Host "Version              : $($OS.Version)" -ForegroundColor White
Write-Host "Domaine/Workgroup    : $($Computer.Domain)" -ForegroundColor White
Write-Host "Utilisateur actuel   : $env:USERNAME" -ForegroundColor White

#==============================================================================
# 2. CONFIGURATION RESEAU
#==============================================================================
Write-Header "CONFIGURATION RESEAU"

$Adapters = Get-NetAdapter | Where-Object { $_.Status -eq "Up" }

foreach ($Adapter in $Adapters) {
    Write-SubHeader $Adapter.Name

    $IPConfig = Get-NetIPAddress -InterfaceIndex $Adapter.ifIndex -ErrorAction SilentlyContinue | Where-Object { $_.AddressFamily -eq "IPv4" }
    $Gateway = Get-NetRoute -InterfaceIndex $Adapter.ifIndex -ErrorAction SilentlyContinue | Where-Object { $_.DestinationPrefix -eq "0.0.0.0/0" }
    $DNS = Get-DnsClientServerAddress -InterfaceIndex $Adapter.ifIndex -ErrorAction SilentlyContinue | Where-Object { $_.AddressFamily -eq 2 }

    Write-Host "  Adresse MAC        : $($Adapter.MacAddress)" -ForegroundColor White
    Write-Host "  Adresse IP         : $($IPConfig.IPAddress)" -ForegroundColor White
    Write-Host "  Masque (CIDR)      : /$($IPConfig.PrefixLength)" -ForegroundColor White
    Write-Host "  Passerelle         : $($Gateway.NextHop)" -ForegroundColor White
    Write-Host "  Serveurs DNS       : $($DNS.ServerAddresses -join ', ')" -ForegroundColor White
    Write-Host "  Vitesse            : $($Adapter.LinkSpeed)" -ForegroundColor White
}

#==============================================================================
# 3. TEST DE CONNECTIVITE
#==============================================================================
Write-Header "TEST DE CONNECTIVITE"

$TestTargets = @(
    @{Name="Passerelle locale"; Target=$Gateway.NextHop},
    @{Name="DNS Google"; Target="8.8.8.8"},
    @{Name="Google.com"; Target="google.com"},
    @{Name="Cloudflare DNS"; Target="1.1.1.1"}
)

foreach ($Test in $TestTargets) {
    if ($Test.Target) {
        $Result = Test-Connection -ComputerName $Test.Target -Count 1 -Quiet -ErrorAction SilentlyContinue
        if ($Result) {
            Write-Host "  [OK] $($Test.Name) ($($Test.Target))" -ForegroundColor Green
        } else {
            Write-Host "  [ECHEC] $($Test.Name) ($($Test.Target))" -ForegroundColor Red
        }
    }
}

#==============================================================================
# 4. PORTS EN ECOUTE
#==============================================================================
Write-Header "PORTS EN ECOUTE (TCP)"

$Listeners = Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
    Select-Object LocalPort, @{Name="Process";Expression={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} |
    Sort-Object LocalPort -Unique |
    Select-Object -First 15

Write-Host ""
Write-Host "  Port`t`tProcessus" -ForegroundColor Yellow
Write-Host "  ----`t`t---------" -ForegroundColor Yellow
foreach ($Listener in $Listeners) {
    Write-Host "  $($Listener.LocalPort)`t`t$($Listener.Process)" -ForegroundColor White
}

#==============================================================================
# 5. SERVICES RESEAU
#==============================================================================
Write-Header "SERVICES RESEAU"

$NetworkServices = @("Dhcp", "Dnscache", "LanmanServer", "LanmanWorkstation", "W32Time", "WinRM")

foreach ($ServiceName in $NetworkServices) {
    $Service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue
    if ($Service) {
        $Status = if ($Service.Status -eq "Running") { "[OK]" } else { "[ARRET]" }
        $Color = if ($Service.Status -eq "Running") { "Green" } else { "Red" }
        Write-Host "  $Status $($Service.DisplayName)" -ForegroundColor $Color
    }
}

#==============================================================================
# 6. TABLE ARP
#==============================================================================
Write-Header "TABLE ARP (5 dernieres entrees)"

$ArpTable = Get-NetNeighbor -ErrorAction SilentlyContinue |
    Where-Object { $_.State -eq "Reachable" -or $_.State -eq "Permanent" } |
    Select-Object -First 5

Write-Host ""
Write-Host "  Adresse IP`t`tAdresse MAC`t`t`tEtat" -ForegroundColor Yellow
Write-Host "  ----------`t`t-----------`t`t`t----" -ForegroundColor Yellow
foreach ($Entry in $ArpTable) {
    Write-Host "  $($Entry.IPAddress)`t$($Entry.LinkLayerAddress)`t$($Entry.State)" -ForegroundColor White
}

#==============================================================================
# 7. CONNEXIONS ACTIVES
#==============================================================================
Write-Header "CONNEXIONS ACTIVES (TCP Established)"

$Connections = Get-NetTCPConnection -State Established -ErrorAction SilentlyContinue |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, @{Name="Process";Expression={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} |
    Select-Object -First 10

Write-Host ""
foreach ($Conn in $Connections) {
    Write-Host "  $($Conn.LocalAddress):$($Conn.LocalPort) <-> $($Conn.RemoteAddress):$($Conn.RemotePort) [$($Conn.Process)]" -ForegroundColor White
}

#==============================================================================
# FIN DU DIAGNOSTIC
#==============================================================================
Write-Host ""
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "  DIAGNOSTIC TERMINE - $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')" -ForegroundColor Cyan
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""

# Pause pour voir les resultats
Read-Host "Appuyez sur Entree pour quitter"
