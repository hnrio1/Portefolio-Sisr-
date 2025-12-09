# Déploiement Nextcloud avec Ansible

> **Auteur** : Henrio Chambal - BTS SIO 2 SISR
> **Projet** : Stage - Automatisation d'infrastructure
> **Environnement** : VMware Workstation, Ubuntu Server/Desktop

## Objectif du projet

Automatiser le déploiement d'une plateforme **Nextcloud** (cloud privé) à l'aide d'**Ansible**, un outil d'automatisation Infrastructure as Code (IaC).

Nextcloud est une solution open-source de partage et synchronisation de fichiers, alternative à Google Drive ou Dropbox.

## Architecture

```
┌─────────────────────────┐         SSH          ┌─────────────────────────┐
│   ANSIBLE-CONTROL       │ ───────────────────► │   NEXTCLOUD-SERVER      │
│   Ubuntu Server         │                      │   Ubuntu Desktop        │
│   192.168.146.135       │                      │   192.168.146.136       │
│                         │                      │                         │
│   - Ansible             │                      │   - Apache2             │
│   - Playbooks YAML      │                      │   - MariaDB             │
│                         │                      │   - PHP                 │
│                         │                      │   - Nextcloud           │
└─────────────────────────┘                      └─────────────────────────┘
```

## Stack technique

| Composant | Rôle |
|-----------|------|
| **Ansible** | Automatisation du déploiement |
| **Apache2** | Serveur web |
| **MariaDB** | Base de données |
| **PHP** | Langage côté serveur |
| **Nextcloud** | Application cloud |
| **UFW** | Pare-feu |
| **Fail2ban** | Protection contre les attaques |

## Fichiers du projet

```
nextcloud-ansible/
├── README.md                    # Documentation
├── inventory/
│   └── hosts                    # Inventaire des machines
└── playbooks/
    └── deploy_nextcloud.yml     # Playbook de déploiement
```

## Configuration de l'inventaire

Fichier `/etc/ansible/hosts` :

```ini
[nextcloud]
192.168.146.136 ansible_user=henrio
```

## Playbook de déploiement

Le playbook `deploy_nextcloud.yml` automatise :

1. **Mise à jour du système** (apt update)
2. **Installation des paquets** (Apache, MariaDB, PHP, extensions)
3. **Démarrage des services** (Apache, MariaDB)
4. **Création de la base de données** Nextcloud
5. **Création de l'utilisateur** MariaDB
6. **Téléchargement** de Nextcloud
7. **Configuration** d'Apache (VirtualHost)
8. **Permissions** sur les fichiers

### Extrait du playbook

```yaml
---
- name: Deploiement complet de Nextcloud
  hosts: nextcloud
  become: yes

  vars:
    nextcloud_version: "latest"
    db_name: nextcloud_db
    db_user: nextcloud_user
    db_password: 'MotDePasse123'

  tasks:
    - name: Mise a jour du cache APT
      apt:
        update_cache: yes

    - name: Installer Apache, MariaDB, PHP et dependances
      apt:
        name:
          - apache2
          - mariadb-server
          - php
          - php-mysql
          - php-gd
          - php-xml
          - php-mbstring
          - php-curl
          - php-zip
          - php-intl
          - libapache2-mod-php
        state: present

    - name: Demarrer Apache
      service:
        name: apache2
        state: started
        enabled: yes
```

## Commandes Ansible utilisées

```bash
# Tester la connexion aux machines
ansible nextcloud -m ping

# Lancer le playbook
ansible-playbook ~/ansible/playbooks/deploy_nextcloud.yml

# Lancer avec mot de passe sudo
ansible-playbook deploy_nextcloud.yml --ask-become-pass
```

## Configuration SSH

```bash
# Générer une clé SSH
ssh-keygen

# Copier la clé vers le serveur cible
ssh-copy-id henrio@192.168.146.136

# Tester la connexion
ssh henrio@192.168.146.136
```

## Sécurisation du serveur

### Pare-feu (UFW)

```bash
sudo apt install ufw -y
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw enable
```

### Fail2ban

```bash
sudo apt install fail2ban -y
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

## Résultat

Après déploiement, Nextcloud est accessible via :

```
http://192.168.146.136
```

Configuration initiale :
- Créer un compte administrateur
- Base de données : MySQL/MariaDB
- Utilisateur DB : `nextcloud_user`
- Nom de la base : `nextcloud_db`
- Serveur : `localhost`

## Problèmes rencontrés et solutions

| Problème | Solution |
|----------|----------|
| PHP 8.4 non compatible | Utiliser Nextcloud version `latest` (30+) |
| Timeout SSH Ansible | Configurer `NOPASSWD` dans sudoers |
| Erreur base de données | Recréer l'utilisateur MariaDB avec les bons privilèges |
| Page Apache par défaut | Désactiver le site par défaut : `a2dissite 000-default.conf` |

## Compétences acquises

- **Ansible** : Playbooks, inventaires, modules (apt, service, file, copy)
- **Linux** : Administration Ubuntu Server, gestion des services
- **Apache** : Configuration VirtualHost, modules
- **MariaDB** : Création BDD, utilisateurs, privilèges
- **Sécurité** : Pare-feu UFW, Fail2ban, clés SSH
- **Infrastructure as Code** : Automatisation, reproductibilité

## Concepts clés

### Ansible

- **Agentless** : Pas besoin d'installer d'agent sur les machines cibles
- **Idempotent** : Peut être exécuté plusieurs fois sans effet secondaire
- **YAML** : Format lisible pour les playbooks
- **SSH** : Communication sécurisée avec les machines

### Infrastructure as Code (IaC)

Avantages :
- Déploiement reproductible
- Documentation automatique
- Versioning possible (Git)
- Réduction des erreurs humaines
