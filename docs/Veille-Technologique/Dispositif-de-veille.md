# Dispositif de veille technologique

**Auteur :** Henrio Chambal — BTS SIO 2 SISR
**Période :** Année scolaire 2025-2026
**Sujet :** Vulnérabilités et menaces de cybersécurité impactant les infrastructures SISR

---

## 1. Objectifs de ma veille

- **Rester informé** des vulnérabilités critiques (CVE) affectant les systèmes que j'administre en formation et en stage
- **Anticiper** les correctifs à appliquer sur une infrastructure
- **Développer** ma culture cybersécurité pour mon orientation future (analyste SOC)
- **Comprendre** l'impact métier d'une vulnérabilité sur une infrastructure réelle

## 2. Sources utilisées

J'ai sélectionné des sources **officielles et complémentaires** pour avoir une vue à la fois institutionnelle et pragmatique de l'actualité cybersécurité.

### Source principale : CERT-FR (ANSSI)

| Élément | Détail |
|---------|--------|
| Site | https://www.cert.ssi.gouv.fr/ |
| Type | Alertes, avis, bulletins d'actualité |
| Fréquence | Quotidienne (plusieurs bulletins par semaine) |
| Fiabilité | **Source officielle ANSSI** — autorité française en cybersécurité |
| Format | Pages web + flux RSS |

**Pourquoi le CERT-FR ?**
Le CERT-FR est le centre gouvernemental de veille, d'alerte et de réponse aux attaques informatiques en France. Ses bulletins sont la référence absolue pour tout professionnel travaillant sur une infrastructure française.

### Sources secondaires

| Source | Lien | Intérêt |
|--------|------|---------|
| **LeMagIT** | https://www.lemagit.fr/ | Actualité IT française, angle métier et retour d'expérience |
| **Bleeping Computer** | https://www.bleepingcomputer.com/ | Actualité internationale, souvent en avance sur les attaques en cours |
| **The Hacker News** | https://thehackernews.com/ | Synthèses claires des incidents cybersécurité |
| **NVD (CVE Details)** | https://nvd.nist.gov/ | Base de données nationale américaine des CVE |

## 3. Outils de veille

### Google Alerts (outil principal)
J'utilise **Google Alerts** pour recevoir automatiquement par mail les articles liés à mes sujets de veille. Trois alertes sont configurées :

- **"cybersécurité vulnérabilité"** — actualités françaises sur les failles de sécurité
- **"CERT-FR ANSSI"** — bulletins officiels de l'agence nationale de cybersécurité
- **"CVE critical vulnerability"** — couverture internationale des vulnérabilités critiques

Les alertes arrivent directement dans ma boîte Gmail, ce qui me permet de ne rien rater sans devoir consulter chaque site manuellement.

### Consultation directe des sources
En complément de Google Alerts, je consulte régulièrement ces sites en favoris :
- **cert.ssi.gouv.fr** — alertes et avis officiels du CERT-FR
- **bleepingcomputer.com** — actualité cybersécurité internationale

### Prises de notes — Markdown / Git
Pour chaque information jugée pertinente, je crée une **fiche de veille** au format Markdown dans le dossier `Fiches/` de ce portfolio. Le format Markdown me permet de versionner mes notes sur Git et d'avoir une traçabilité dans le temps.

## 4. Méthode et fréquence

### Routine hebdomadaire (~20-30 minutes par semaine)

1. **Consultation des nouveaux bulletins** via Feedly (10 min)
2. **Sélection** des informations pertinentes pour un environnement SISR
3. **Rédaction d'une fiche** pour chaque information retenue (10 min par fiche)
4. **Archivage** dans le dossier `Fiches/` avec date de publication

### Critères de sélection

Je retiens une information si elle concerne au moins l'un de ces domaines :
- Systèmes que j'administre en formation/stage (Windows Server, Debian, Ubuntu, pfSense)
- Services courants en entreprise (Apache, MariaDB, OpenSSH, Active Directory)
- Vulnérabilités critiques ou à forte médiatisation
- Nouvelles techniques d'attaque documentées dans MITRE ATT&CK

## 5. Format de mes fiches de veille

Chaque fiche contient les éléments suivants :

- **Titre** et **numéro CVE** si applicable
- **Date** du bulletin et **date de consultation**
- **Source** (lien direct)
- **Résumé** de la vulnérabilité / information
- **Systèmes concernés**
- **Niveau de gravité** (critique / important / modéré)
- **Impact métier** : quelle conséquence sur une infrastructure type StadiumCompany ?
- **Correctif / mitigation** recommandés
- **Ma synthèse personnelle** : ce que j'en retiens

Un modèle vierge est disponible : [Fiches/MODELE-fiche.md](./Fiches/MODELE-fiche.md)

---

**Dispositif mis en place depuis :** septembre 2025
**Révision :** en continu
