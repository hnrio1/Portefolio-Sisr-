# Active Directory - DNS - DHCP (Windows Server)

> **Auteur** : Henrio Chambal - BTS SIO 2 SISR
> **Environnement** : VMware Workstation Pro, Windows Server 2022, Windows 10/11

## Objectif du projet

Mettre en place une infrastructure Windows Server complète pour une entreprise fictive (Stadium Company) :
- **Active Directory DS** : Gestion centralisée des utilisateurs et ordinateurs
- **DNS** : Résolution de noms pour le domaine
- **DHCP** : Attribution automatique des adresses IP
- **GPO** : Stratégies de groupe pour la gestion du parc

## Architecture

### Topologie réseau

```
                    ┌─────────────────────────┐
                    │     Serveur HERMES      │
                    │    Windows Server 2022  │
                    │      172.20.0.14/24     │
                    │                         │
                    │  - Active Directory DS  │
                    │  - DNS                  │
                    │  - DHCP                 │
                    └───────────┬─────────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
           ┌────────▼────────┐    ┌────────▼────────┐
           │   PC-Client-1   │    │   PC-Client-2   │
           │   Windows 10    │    │   Windows 11    │
           │   DHCP Client   │    │   DHCP Client   │
           └─────────────────┘    └─────────────────┘
```

### Adressage IP

| Machine | Hostname | IP | Rôle |
|---------|----------|-----|------|
| Serveur | HERMES | 172.20.0.14/24 | DC, DNS, DHCP |
| Client 1 | PC-Client-1 | DHCP (172.20.0.50-100) | Poste utilisateur |
| Client 2 | PC-Client-2 | DHCP (172.20.0.50-100) | Poste utilisateur |

### Informations du domaine

| Paramètre | Valeur |
|-----------|--------|
| Nom de domaine | stadiumcompany.com |
| Nom NetBIOS | STADIUMCOMPANY |
| Niveau fonctionnel | Windows Server 2016 |

---

## Partie 1 : Installation Windows Server

### Configuration initiale

1. **Installation de Windows Server 2022** (VMware)
2. **Configuration réseau statique** :
   - IP : 172.20.0.14
   - Masque : 255.255.255.0
   - DNS : 127.0.0.1 (lui-même)

3. **Renommer le serveur** :
```powershell
Rename-Computer -NewName "HERMES" -Restart
```

---

## Partie 2 : Active Directory Domain Services

### Installation du rôle AD DS

1. **Gestionnaire de serveur** → Ajouter des rôles et fonctionnalités
2. Sélectionner **Services AD DS**
3. Installer les fonctionnalités requises

### Promotion en contrôleur de domaine

1. Cliquer sur le drapeau de notification → **Promouvoir ce serveur...**
2. **Ajouter une nouvelle forêt** : `stadiumcompany.com`
3. Mot de passe DSRM : (à définir)
4. Terminer l'assistant et redémarrer

### Vérification

```powershell
# Vérifier le domaine
Get-ADDomain

# Vérifier le contrôleur de domaine
Get-ADDomainController
```

---

## Partie 3 : Configuration DNS

### Zone de recherche directe

La zone `stadiumcompany.com` est créée automatiquement lors de la promotion AD DS.

**Enregistrements créés automatiquement** :
- `HERMES.stadiumcompany.com` → 172.20.0.14

### Zone de recherche inversée

1. **Gestionnaire DNS** → Zones de recherche inversée
2. Nouvelle zone → Zone principale intégrée à AD
3. ID réseau : `172.20.0`

**Ajout d'un enregistrement PTR** :
- 14 → HERMES.stadiumcompany.com

### Test DNS

```powershell
# Résolution directe
nslookup HERMES.stadiumcompany.com

# Résolution inverse
nslookup 172.20.0.14
```

---

## Partie 4 : Configuration DHCP

### Installation du rôle DHCP

1. **Gestionnaire de serveur** → Ajouter des rôles
2. Sélectionner **Serveur DHCP**
3. Terminer la configuration post-installation

### Création de l'étendue

| Paramètre | Valeur |
|-----------|--------|
| Nom | Etendue_LAN |
| Plage d'adresses | 172.20.0.50 - 172.20.0.100 |
| Masque | 255.255.255.0 |
| Passerelle | 172.20.0.254 |
| Serveur DNS | 172.20.0.14 |
| Durée du bail | 8 jours |

### Autorisation DHCP

```powershell
# Autoriser le serveur DHCP dans AD
Add-DhcpServerInDC -DnsName "HERMES.stadiumcompany.com" -IPAddress 172.20.0.14
```

---

## Partie 5 : Structure Active Directory

### Unités d'Organisation (OU)

```
stadiumcompany.com
├── Direction
│   └── Utilisateurs direction
├── Comptabilite
│   └── Utilisateurs comptabilité
├── RH
│   └── Utilisateurs RH
├── Informatique
│   └── Utilisateurs IT
└── Ordinateurs
    └── Postes clients
```

### Création des OU (PowerShell)

```powershell
# Créer les OU
New-ADOrganizationalUnit -Name "Direction" -Path "DC=stadiumcompany,DC=com"
New-ADOrganizationalUnit -Name "Comptabilite" -Path "DC=stadiumcompany,DC=com"
New-ADOrganizationalUnit -Name "RH" -Path "DC=stadiumcompany,DC=com"
New-ADOrganizationalUnit -Name "Informatique" -Path "DC=stadiumcompany,DC=com"
New-ADOrganizationalUnit -Name "Ordinateurs" -Path "DC=stadiumcompany,DC=com"
```

### Création d'utilisateurs

```powershell
# Exemple : créer un utilisateur
New-ADUser -Name "Jean Dupont" `
    -GivenName "Jean" `
    -Surname "Dupont" `
    -SamAccountName "jdupont" `
    -UserPrincipalName "jdupont@stadiumcompany.com" `
    -Path "OU=Direction,DC=stadiumcompany,DC=com" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) `
    -Enabled $true
```

---

## Partie 6 : Stratégies de Groupe (GPO)

### GPO 1 : Fond d'écran entreprise

1. **Gestion des stratégies de groupe** → Créer une GPO
2. Nom : `GPO_FondEcran`
3. Configuration utilisateur → Stratégies → Modèles d'administration
4. Bureau → Bureau → Papier peint du Bureau
   - Activer
   - Chemin : `\\HERMES\Partage\wallpaper.jpg`
   - Style : Étirer

### GPO 2 : Mappage de lecteur réseau

1. Créer une GPO : `GPO_LecteurReseau`
2. Configuration utilisateur → Préférences → Paramètres Windows
3. Mappages de lecteurs → Nouveau
   - Lettre : `S:`
   - Chemin : `\\HERMES\Partage`

### GPO 3 : Restriction Panneau de configuration

1. Créer une GPO : `GPO_RestrictionPC`
2. Configuration utilisateur → Stratégies → Modèles d'administration
3. Panneau de configuration → Interdire l'accès au Panneau de configuration
   - Activer

### Application des GPO

```powershell
# Forcer la mise à jour des GPO sur un client
gpupdate /force

# Vérifier les GPO appliquées
gpresult /r
```

---

## Partie 7 : Jonction des clients au domaine

### Sur le poste client Windows

1. **Paramètres** → Système → À propos → Joindre un domaine
2. Entrer : `stadiumcompany.com`
3. S'authentifier avec un compte administrateur du domaine
4. Redémarrer

### Vérification

```powershell
# Sur le client
systeminfo | findstr /B "Domain"

# Sur le serveur
Get-ADComputer -Filter * | Select Name
```

---

## Partie 8 : Sites Active Directory

### Création du site "Paris"

1. **Sites et services Active Directory**
2. Sites → Nouveau site : `Paris`
3. Associer le sous-réseau 172.20.0.0/24

### Configuration du sous-réseau

1. Subnets → Nouveau sous-réseau
2. Préfixe : `172.20.0.0/24`
3. Associer au site : `Paris`

---

## Tests et validation

### Checklist de validation

- [ ] Le domaine `stadiumcompany.com` est opérationnel
- [ ] La résolution DNS fonctionne (directe et inverse)
- [ ] Les clients obtiennent une IP via DHCP
- [ ] Les clients peuvent rejoindre le domaine
- [ ] Les GPO s'appliquent correctement
- [ ] Les utilisateurs peuvent se connecter avec leurs comptes AD

### Commandes de diagnostic

```powershell
# Vérifier la réplication AD
repadmin /replsummary

# Tester la connectivité AD
dcdiag /v

# Vérifier les baux DHCP
Get-DhcpServerv4Lease -ScopeId 172.20.0.0

# Lister les ordinateurs du domaine
Get-ADComputer -Filter * -Properties IPv4Address | Select Name, IPv4Address
```

---

## Compétences acquises

- Installation et configuration de Windows Server 2022
- Déploiement d'Active Directory Domain Services
- Configuration des zones DNS (directe et inverse)
- Mise en place d'un serveur DHCP avec étendue
- Création d'une structure organisationnelle (OU)
- Déploiement de stratégies de groupe (GPO)
- Jonction de postes clients au domaine
- Gestion des sites Active Directory

---

## Technologies utilisées

- **OS Serveur** : Windows Server 2022
- **OS Clients** : Windows 10/11
- **Virtualisation** : VMware Workstation Pro
- **Services** : AD DS, DNS, DHCP
- **Outils** : PowerShell, Gestionnaire de serveur, GPMC
