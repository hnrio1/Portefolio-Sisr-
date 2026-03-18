# TP Zimbra - Serveur de Messagerie

## Description

Déploiement d'un serveur de messagerie **Zimbra** intégré à l'infrastructure Active Directory et pfSense du projet StadiumCompany.

## Objectifs

- Installer et configurer Zimbra sur Ubuntu Server
- Intégrer le serveur de messagerie au DNS Active Directory
- Configurer les règles de pare-feu (pfSense) pour la DMZ
- Permettre l'envoi et la réception d'emails en interne

## Technologies utilisées

- **Zimbra** - Suite de messagerie collaborative
- **Ubuntu Server** - Système d'exploitation
- **Active Directory / DNS** - Résolution de noms et intégration domaine
- **pfSense** - Pare-feu (règles LAN/DMZ)

## Étapes principales

1. Configuration réseau et DNS (hostname, resolv.conf)
2. Création de l'enregistrement DNS sur le serveur AD
3. Installation de Zimbra
4. Configuration des règles de pare-feu LAN ↔ DMZ
5. Test de la messagerie

## Compétences mobilisées

- Administration système Linux
- Gestion DNS (Active Directory)
- Configuration de pare-feu
- Déploiement de services de messagerie

## Fichiers

- `TP_ZIMBRA_CHAMBAL_Henrio.pdf` - Compte rendu complet du TP avec captures d'écran
