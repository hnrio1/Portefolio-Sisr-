# Épreuve E6 — Administration des systèmes et des réseaux

Cette épreuve, **spécifique à l'option SISR**, présente mes deux **Réalisations Professionnelles** réalisées dans le cadre du projet **StadiumCompany**.

---

## Contexte StadiumCompany

**StadiumCompany** est une entreprise spécialisée dans la gestion d'un grand stade multi-événements qui accueille matchs, concerts et salons professionnels. L'entreprise emploie 170 personnes à temps plein et fait appel à 80 intérimaires lors des événements, répartis sur trois sites : le Stade, la Billetterie et le Magasin.

L'entreprise fait appel au prestataire **NetworkingCompany** pour la mise en place de ses solutions systèmes et réseaux.

Mes deux réalisations s'articulent autour des **hôtesses d'accueil** qui scannent les billets dans les tribunes : la première met en place le **socle réseau et l'authentification**, la seconde apporte les **services applicatifs** (gestion de parc, supervision et communication).

---

## Mes deux Réalisations Professionnelles

<div class="grid cards" markdown>

-   :material-wifi: __Réseau Scanners Tribunes__

    Infrastructure réseau Wi-Fi pour les hôtesses d'accueil avec smartphones scanners.

    **Outils principaux :** Active Directory, Cisco, Wi-Fi

    - VLAN 50 dédié (172.20.5.0/24) + trunk 802.1Q
    - Bornes Wi-Fi Cisco AIR-CAP3502I (SSID Host-Wifi)
    - Active Directory : OU « Accueil-Tribunes », groupe, GPO mappage lecteur H

    [:octicons-arrow-right-24: Voir la réalisation](theme-15/README.md)

-   :material-cellphone-link: __Gestion Smartphones et Coordination__

    Gestion du parc de smartphones et coordination des équipes pendant les événements.

    **Outils principaux :** GLPI, OCS Inventory, Zimbra, Nagios

    - OCS Inventory + GLPI : inventaire smartphones + tickets ITIL
    - Zimbra : liste de diffusion accueil@stadiumcompany.com
    - Nagios : supervision des bornes Wi-Fi des tribunes

    [:octicons-arrow-right-24: Voir la réalisation](theme-15/README.md)

</div>
