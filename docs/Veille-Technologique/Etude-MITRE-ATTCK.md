# Étude approfondie : MITRE ATT&CK

**Auteur :** Henrio Chambal — BTS SIO 2 SISR
**Date de rédaction :** Avril 2026
**Type :** Étude d'une méthode / framework de cybersécurité

---

## 1. Introduction

Dans le cadre de ma veille sur les menaces et vulnérabilités cybersécurité, j'ai été amené à consulter régulièrement des références à un framework international appelé **MITRE ATT&CK**. Comme ce framework est devenu un standard dans les SOC et les équipes de threat intelligence, j'ai souhaité l'étudier plus en profondeur pour comprendre comment les professionnels de la cybersécurité classifient et analysent les attaques.

## 2. Présentation du framework

### Qu'est-ce que MITRE ATT&CK ?

**MITRE ATT&CK** (Adversarial Tactics, Techniques, and Common Knowledge) est une **base de connaissances** publique et gratuite qui documente les tactiques, techniques et procédures (TTPs) utilisées par les attaquants au cours de cyberattaques réelles.

- **Créé par :** MITRE Corporation (organisation à but non lucratif américaine)
- **Année de création :** 2013
- **Site officiel :** https://attack.mitre.org/
- **Licence :** Publique et gratuite

### Objectif

Fournir un **référentiel commun** à toute la communauté cybersécurité pour :
- Décrire de manière standardisée comment un attaquant agit
- Comparer des campagnes d'attaque entre elles
- Améliorer la détection et la défense
- Communiquer efficacement entre équipes (SOC, CERT, forensic)

## 3. Structure du framework

MITRE ATT&CK est organisé en 3 niveaux :

### 3.1 Tactiques (14 tactiques au total)

Les tactiques représentent **le "pourquoi"** : l'objectif de l'attaquant à un moment donné.

| # | Tactique | Description |
|---|----------|-------------|
| 1 | **Reconnaissance** | Collecter des informations sur la cible |
| 2 | **Resource Development** | Préparer l'infrastructure d'attaque |
| 3 | **Initial Access** | Obtenir un premier point d'entrée |
| 4 | **Execution** | Exécuter du code malveillant |
| 5 | **Persistence** | Maintenir l'accès dans le temps |
| 6 | **Privilege Escalation** | Obtenir des droits plus élevés |
| 7 | **Defense Evasion** | Éviter la détection |
| 8 | **Credential Access** | Voler des identifiants |
| 9 | **Discovery** | Explorer l'environnement cible |
| 10 | **Lateral Movement** | Se déplacer sur le réseau |
| 11 | **Collection** | Rassembler les données d'intérêt |
| 12 | **Command and Control** | Communiquer avec l'attaquant |
| 13 | **Exfiltration** | Extraire les données |
| 14 | **Impact** | Perturber ou détruire |

### 3.2 Techniques (plus de 200 techniques)

Les techniques représentent **le "comment"** : les méthodes concrètes utilisées pour réaliser une tactique.

**Exemple :** Pour la tactique **Initial Access**, les techniques incluent :
- T1566 — **Phishing** (hameçonnage)
- T1190 — **Exploit Public-Facing Application** (exploitation d'une application exposée)
- T1078 — **Valid Accounts** (utilisation de comptes valides)
- T1195 — **Supply Chain Compromise** (attaque sur la chaîne d'approvisionnement)

### 3.3 Sous-techniques

Certaines techniques sont déclinées en sous-techniques plus précises.

**Exemple :** T1566 Phishing se décompose en :
- T1566.001 — Spearphishing Attachment
- T1566.002 — Spearphishing Link
- T1566.003 — Spearphishing via Service

## 4. Exemple concret : analyse d'une attaque avec ATT&CK

Prenons un scénario classique : **une attaque par ransomware sur une PME**.

| Étape de l'attaque | Tactique ATT&CK | Technique |
|--------------------|------------------|-----------|
| L'attaquant envoie un email piégé | Initial Access | T1566.001 Spearphishing Attachment |
| L'utilisateur ouvre une pièce jointe Word avec macro | Execution | T1204.002 Malicious File |
| Le malware s'installe et se lance au démarrage | Persistence | T1547.001 Registry Run Keys |
| Escalade via une faille locale | Privilege Escalation | T1068 Exploitation for Privilege Escalation |
| Désactivation de l'antivirus | Defense Evasion | T1562.001 Disable Security Tools |
| Vol des identifiants AD | Credential Access | T1003 OS Credential Dumping |
| Propagation aux autres machines | Lateral Movement | T1021 Remote Services |
| Chiffrement des fichiers | Impact | T1486 Data Encrypted for Impact |

Cette grille de lecture permet à un analyste SOC de **reconstruire une attaque** et de mieux la comprendre, puis de vérifier si les mêmes TTPs ont déjà été observés ailleurs.

## 5. Utilisation concrète en SISR / SOC

### Pour un administrateur SISR

- **Durcissement** : chaque technique ATT&CK s'accompagne de **contre-mesures** (mitigations) et de **détections** recommandées. Exemple : pour contrer T1003 (OS Credential Dumping), MITRE recommande d'activer Credential Guard sur Windows, de limiter les droits administrateur, etc.
- **Priorisation** : connaître les techniques les plus utilisées permet de prioriser les défenses.

### Pour un analyste SOC

- **Détection** : les règles de détection dans un SIEM (comme Wazuh, Splunk, Sentinel) peuvent être mappées à des techniques ATT&CK.
- **Threat Intelligence** : les rapports sur des groupes d'attaquants (APT) listent les techniques qu'ils utilisent. Exemple : le groupe APT28 utilise principalement T1566, T1078, T1003...
- **Reporting** : en cas d'incident, parler en termes ATT&CK standardise la communication entre équipes.

## 6. Outils associés

| Outil | Description |
|-------|-------------|
| **ATT&CK Navigator** | Visualisation interactive des techniques sur une matrice colorée |
| **CAR (Cyber Analytics Repository)** | Bibliothèque d'analyses de détection mappées à ATT&CK |
| **ATT&CK Workbench** | Outil de gestion et d'extension personnalisée du framework |

## 7. Apport pour mon parcours SISR / cybersécurité

Étudier MITRE ATT&CK m'a apporté :

1. **Un vocabulaire commun** avec les professionnels de la cybersécurité
2. **Une grille de lecture structurée** pour analyser un incident
3. **Une meilleure compréhension** de ce qu'un SOC fait au quotidien
4. **Des idées concrètes de durcissement** pour les infrastructures que je déploie en TP

## 8. Conclusion

MITRE ATT&CK est devenu un **standard incontournable** dans le monde de la cybersécurité défensive. Pour un étudiant SISR visant un poste en SOC, maîtriser ce framework est un réel atout professionnel et un point fort à mentionner à un entretien.

Ma veille technologique s'appuie désormais sur cette grille pour **contextualiser les vulnérabilités** publiées par le CERT-FR : quand une nouvelle CVE sort, je cherche à comprendre à quelles tactiques et techniques ATT&CK elle peut être associée.

---

## Sources consultées

- Site officiel MITRE ATT&CK — https://attack.mitre.org/
- ATT&CK Navigator — https://mitre-attack.github.io/attack-navigator/
- Documentation MITRE — https://attack.mitre.org/resources/
- LeMagIT, articles sur ATT&CK — https://www.lemagit.fr/
