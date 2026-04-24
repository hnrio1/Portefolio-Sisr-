# Veille Technologique

**Sujet :** Suivi des alertes de cybersécurité du CERT-FR (ANSSI).

<span class="tech-badge">CERT-FR</span> <span class="tech-badge">ANSSI</span> <span class="tech-badge">Google Alerts</span>

---

## Méthode

J'utilise **Google Alerts** avec 3 alertes configurées (`cybersécurité vulnérabilité`, `CERT-FR ANSSI`, `CVE critical vulnerability`) qui m'envoient automatiquement les articles par mail. En complément, je consulte le site du [CERT-FR](https://www.cert.ssi.gouv.fr/) pour les bulletins officiels de l'ANSSI.

**Routine hebdomadaire (~20 min) :** lecture des alertes → sélection des infos qui concernent mes systèmes (Windows Server, Linux, pfSense, Apache, AD, SSH) → rédaction d'une fiche de veille.

---

## Résultats

<div class="grid cards" markdown>

-   :material-ssh: __regreSSHion — OpenSSH__

    CVE-2024-6387 — Exécution de code en root à distance sur SSH, score CVSS 8.1.

    [:octicons-arrow-right-24: Lire la fiche](Fiches/2025-09-15-faille-openssh.md)

-   :material-microsoft-windows: __Zerologon — Active Directory__

    CVE-2020-1472 — Prise de contrôle du domaine AD sans mot de passe, score CVSS 10.0.

    [:octicons-arrow-right-24: Lire la fiche](Fiches/2026-01-10-faille-windows-ad.md)

</div>
