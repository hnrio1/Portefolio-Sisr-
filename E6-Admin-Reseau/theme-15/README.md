# Thème 15 - StadiumCompany

Dossier des Réalisations Professionnelles pour l'épreuve E6 (Administration des systèmes et des réseaux) du BTS SIO SISR.

Contexte : infrastructure réseau, supervision et gestion de parc pour la société fictive **StadiumCompany** (gestion et administration d'événements sportifs).

## Réalisations Professionnelles

### RP1 - Réseau Scanners Tribunes
[RP1_Documentation_Technique.pdf](./RP1_Documentation_Technique.pdf) — 42 pages

Infrastructure Wi-Fi et gestion des comptes pour les hôtesses d'accueil utilisant des smartphones scanners dans les tribunes.

Contient les 2 parties qui composent la solution :

1. **VLAN 50 & Bornes Wi-Fi Tribunes** — Configuration du VLAN dédié (172.20.5.0/24), trunk 802.1Q, routage inter-VLAN et déploiement des bornes Wi-Fi
2. **Active Directory & GPO** — Création du groupe et de l'UO "Accueil-Tribunes", déploiement d'une GPO pour le mappage du lecteur H

### RP2 - Gestion Smartphones et Coordination
[RP2_Documentation_Technique.pdf](./RP2_Documentation_Technique.pdf) — 75 pages

Documentation technique du RP2 (la page de garde et la fiche descriptive officielles sont dans le dossier physique).

Contient les 3 services qui composent la solution :

1. **OCS Inventory & GLPI** — Gestion de parc smartphones + tickets ITIL (27 étapes)
2. **Nagios Core** — Supervision des bornes Wi-Fi des tribunes (30 étapes)
3. **Zimbra** — Messagerie collaborative pour les briefings (14 étapes)

Chaque étape est numérotée, expliquée et accompagnée de sa capture d'écran.
