# Dispositif de veille technologique

**Auteur :** Henrio Chambal — BTS SIO 2 SISR
**Sujet :** Vulnérabilités et menaces de cybersécurité impactant les infrastructures SISR

---

## Objectifs

- Rester informé des vulnérabilités critiques (CVE) affectant les systèmes que j'administre
- Anticiper les correctifs à appliquer sur une infrastructure
- Développer ma culture cybersécurité pour mon orientation future (analyste SOC)

---

## Sources

### Source principale : CERT-FR (ANSSI)

Le **CERT-FR**, rattaché à l'**ANSSI**, est le centre gouvernemental français de veille et d'alerte en cybersécurité. Ses bulletins sont la référence pour tout professionnel travaillant sur une infrastructure française.

- [cert.ssi.gouv.fr](https://www.cert.ssi.gouv.fr/) — alertes, avis, bulletins d'actualité

### Sources complémentaires

| Source | Lien | Intérêt |
|--------|------|---------|
| **Bleeping Computer** | [bleepingcomputer.com](https://www.bleepingcomputer.com/) | Actualité cybersécurité internationale |
| **The Hacker News** | [thehackernews.com](https://thehackernews.com/) | Synthèses des incidents cybersécurité |
| **NVD (CVE Details)** | [nvd.nist.gov](https://nvd.nist.gov/) | Base de données officielle des CVE |

---

## Outil de veille : Google Alerts

J'utilise **Google Alerts** pour recevoir automatiquement par mail les articles liés à mes sujets de veille. Trois alertes sont configurées :

- `cybersécurité vulnérabilité`
- `CERT-FR ANSSI`
- `CVE critical vulnerability`

Les alertes arrivent directement dans ma boîte Gmail, ce qui me permet de ne rien rater sans devoir consulter chaque site manuellement.

---

## Méthode

**Routine hebdomadaire (~20 min/semaine) :**

1. Lecture des alertes reçues par mail
2. Consultation des nouveaux bulletins sur cert.ssi.gouv.fr
3. Sélection des infos pertinentes pour un environnement SISR
4. Rédaction d'une fiche de veille en Markdown dans le dossier `Fiches/`

**Critères de sélection :** je retiens une info si elle concerne un système que j'administre (Windows Server, Linux, pfSense, Apache, Active Directory, OpenSSH).

---

## Format des fiches

Chaque fiche contient : **titre + CVE**, **date**, **source**, **résumé**, **systèmes concernés**, **score CVSS**, **correctif recommandé**, **ma synthèse personnelle**.
