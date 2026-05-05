# StadiumCompany — Réalisations Professionnelles

Dossier des **Réalisations Professionnelles** pour l'épreuve E6 du BTS SIO SISR.

**StadiumCompany** est une entreprise gérant un grand stade multi-événements (matchs, concerts, salons). Mes deux réalisations s'articulent autour des **hôtesses d'accueil** qui scannent les billets dans les tribunes : la première met en place le socle réseau, la seconde apporte les services applicatifs.

---

## Réalisation Professionnelle n°1 — Réseau Scanners Tribunes

> **Outils principaux : Active Directory, Cisco, Wi-Fi, Windows Server 2022**

<span class="tech-badge">Active Directory</span> <span class="tech-badge">VLAN</span> <span class="tech-badge">Cisco 2821</span> <span class="tech-badge">Catalyst 2960</span> <span class="tech-badge">Wi-Fi AIR-CAP3502I</span> <span class="tech-badge">GPO</span>

L'objectif est de mettre en place une **infrastructure Wi-Fi dédiée** au personnel d'accueil pour scanner les billets et orienter les spectateurs dans les tribunes.

**Mes réalisations :**

- VLAN 50 « Accueil » isolé avec adressage **172.20.5.0/24** et trunk 802.1Q
- Routage inter-VLAN sur le routeur **Cisco 2821** et configuration du switch **Catalyst 2960**
- Déploiement des bornes Wi-Fi **Cisco AIR-CAP3502I** diffusant le SSID **Host-Wifi** sur les tribunes
- Création de l'OU et du groupe Active Directory **« Accueil-Tribunes »**
- Déploiement d'une **GPO** pour le mappage automatique du lecteur réseau **H:** vers la base des plans de placement

[:material-file-document-outline: Fiche descriptive RP1](./RP1_Pages_Officielles.pdf){ target="_blank" } &nbsp; [:material-file-pdf-box: Documentation technique RP1 (42 pages)](./RP1_Documentation_Technique.pdf){ target="_blank" }

---

## Réalisation Professionnelle n°2 — Gestion Smartphones et Coordination

> **Outils principaux : GLPI, OCS Inventory, Zimbra, Nagios**

<span class="tech-badge">GLPI</span> <span class="tech-badge">OCS Inventory</span> <span class="tech-badge">Zimbra</span> <span class="tech-badge">Nagios</span>

L'objectif est de **gérer le parc de smartphones prêtés aux hôtesses** et de **faciliter la communication** des équipes pendant les événements.

**Mes réalisations :**

- Déploiement d'**OCS Inventory** avec l'agent OCS Mobile sur les smartphones pour l'inventaire automatique
- Mise en place de **GLPI** pour le suivi des incidents (perte, casse) et le traitement des tickets ITIL
- Création d'une liste de diffusion **accueil@stadiumcompany.com** sur **Zimbra** pour les briefings d'avant-match
- Ajout des bornes Wi-Fi des tribunes dans **Nagios** pour superviser leur disponibilité en temps réel

[:material-file-document-outline: Fiche descriptive RP2](./RP2_Pages_Officielles.pdf){ target="_blank" } &nbsp; [:material-file-pdf-box: Documentation technique RP2 (75 pages)](./RP2_Documentation_Technique.pdf){ target="_blank" }
