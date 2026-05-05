# Épreuve E5 — Support et mise à disposition de services informatiques

Cette épreuve regroupe l'ensemble de mes réalisations autour de l'**infrastructure**, des **services aux utilisateurs**, de la **cybersécurité** et de mes **deux stages** en entreprise.

<span class="tech-badge">Active Directory</span> <span class="tech-badge">pfSense</span> <span class="tech-badge">Nagios</span> <span class="tech-badge">Zimbra</span> <span class="tech-badge">Snort</span> <span class="tech-badge">VPN IPsec</span> <span class="tech-badge">Ansible</span> <span class="tech-badge">Python</span>

---

## Tableau de synthèse

[:material-table: Voir le tableau de synthèse](../Tableau-de-synthese/README.md){ .md-button .md-button--primary }

---

## Infrastructure & Réseau

<div class="grid cards" markdown>

-   :material-server: __Active Directory__

    Domaine Windows Server 2022, DNS, DHCP, GPO et OU.

    [:octicons-arrow-right-24: Voir le TP](active-directory/README.md)

-   :material-shield: __Pare-feu pfSense__

    7 TPs : installation, sécurité, LDAP, portail captif, Snort, OpenVPN.

    [:octicons-arrow-right-24: Voir le TP](pfsense/README.md)

-   :material-content-duplicate: __Redondance & Haute dispo__

    HAProxy + HeartBeat sur Debian 12 pour la continuité de service.

    [:octicons-arrow-right-24: Voir le TP](mission-4-haproxy-heartbeat/README.md)

-   :material-stadium: __Missions StadiumCompany__

    Missions 1, 2 et 3 du projet StadiumCompany (VLAN, sécurité, parc).

    [:octicons-arrow-right-24: Voir les missions](missions-stadiumcompany/README.md)

</div>

---

## Services aux utilisateurs

<div class="grid cards" markdown>

-   :material-chart-line: __Supervision Nagios__

    Surveillance en continu des serveurs et services réseau.

    [:octicons-arrow-right-24: Voir le TP](nagios/README.md)

-   :material-email: __Messagerie Zimbra__

    Serveur de messagerie collaborative intégré à l'AD.

    [:octicons-arrow-right-24: Voir le TP](zimbra/README.md)

-   :material-console: __SSH__

    Accès distant sécurisé par clés RSA.

    [:octicons-arrow-right-24: Voir le TP](ssh/README.md)

-   :material-wifi-lock: __RADIUS WiFi (802.1X)__

    Authentification forte WiFi via NPS et certificats AD CS.

    [:octicons-arrow-right-24: Voir le TP](mission-6-radius-wifi/README.md)

</div>

---

## Cybersécurité

<div class="grid cards" markdown>

-   :material-radar: __Snort IDS / IPS__

    Détection et prévention d'intrusion sur le trafic réseau.

    [:octicons-arrow-right-24: Voir le TP](../E7-Cybersecurite/snort-ids/README.md)

-   :material-vpn: __VPN Site-to-Site (IPsec)__

    Interconnexion sécurisée de deux sites distants.

    [:octicons-arrow-right-24: Voir le TP](../E7-Cybersecurite/vpn-site-to-site/README.md)

</div>

---

## Stages

<div class="grid cards" markdown>

-   :material-flask: __Institut Pasteur__ — Juin/Juillet 2025

    Déploiement automatisé Nextcloud avec **Ansible** + sécurisation Linux (UFW, Fail2ban, SSH).

    [:octicons-arrow-right-24: Voir le stage](../Stage/pasteur/nextcloud-ansible/README.md)

-   :material-calculator: __Cabinet CECCA__ — Nov/Déc 2025

    Gestion vulnérabilités CVE, cartographie cloud Scaleway, automatisation **Python OCR**.

    [:octicons-arrow-right-24: Voir le stage](../Stage/cecca/scripts-extraction/README.md)

</div>
