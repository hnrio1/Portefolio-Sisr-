# Étude : MITRE ATT&CK

**Auteur :** Henrio Chambal — BTS SIO 2 SISR
**Type :** Étude d'un framework de cybersécurité

---

## Qu'est-ce que MITRE ATT&CK ?

**MITRE ATT&CK** est une base de connaissances publique qui répertorie toutes les **techniques d'attaque connues** utilisées par les attaquants dans des cyberattaques réelles.

- Créé par **MITRE Corporation** (organisation à but non lucratif)
- Site officiel : [attack.mitre.org](https://attack.mitre.org/)
- C'est le **standard mondial** utilisé par les SOC et les équipes de threat intelligence

---

## Comment c'est structuré

Le framework est organisé en 3 niveaux :

1. **Tactiques** (14 au total) — le "pourquoi" : l'objectif de l'attaquant
2. **Techniques** (200+) — le "comment" : les méthodes utilisées
3. **Sous-techniques** — variantes précises d'une technique

### Les 14 tactiques

| Tactique | Objectif |
|----------|----------|
| Reconnaissance | Collecter des informations sur la cible |
| Resource Development | Préparer l'infrastructure d'attaque |
| **Initial Access** | Obtenir un premier point d'entrée |
| Execution | Exécuter du code malveillant |
| **Persistence** | Maintenir l'accès dans le temps |
| **Privilege Escalation** | Obtenir des droits plus élevés |
| Defense Evasion | Éviter la détection |
| **Credential Access** | Voler des identifiants |
| Discovery | Explorer l'environnement cible |
| **Lateral Movement** | Se déplacer sur le réseau |
| Collection | Rassembler les données d'intérêt |
| Command and Control | Communiquer avec l'attaquant |
| Exfiltration | Extraire les données |
| **Impact** | Perturber ou détruire |

---

## Exemple : attaque ransomware étape par étape

| Étape | Tactique | Technique |
|-------|----------|-----------|
| Email piégé | Initial Access | T1566 Phishing |
| Pièce jointe ouverte | Execution | T1204 User Execution |
| Malware persistant | Persistence | T1547 Boot Autostart |
| Vol des mots de passe AD | Credential Access | T1003 OS Credential Dumping |
| Propagation réseau | Lateral Movement | T1021 Remote Services |
| Chiffrement des fichiers | Impact | T1486 Data Encrypted for Impact |

---

## Pourquoi c'est utile

- **Vocabulaire commun** avec les pros de la cybersécurité
- **Grille de lecture** pour analyser un incident
- Chaque technique a des **contre-mesures** associées (utile pour durcir une infra)
- Les rapports sur les **groupes APT** listent les techniques qu'ils utilisent

---

## Apport pour ma veille

Quand une nouvelle CVE sort sur le CERT-FR, je cherche à quelles **tactiques/techniques ATT&CK** elle peut être associée. Ça me permet de comprendre le **scénario d'attaque complet** et pas juste la faille isolée.

**Exemple :** la CVE-2024-6387 (regreSSHion sur OpenSSH) → **T1190 Exploit Public-Facing Application** dans la tactique **Initial Access**.
