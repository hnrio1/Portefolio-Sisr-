# Étude : MITRE ATT&CK

**Auteur :** Henrio Chambal — BTS SIO 2 SISR

---

## C'est quoi ?

**MITRE ATT&CK** est une base de connaissances publique qui répertorie toutes les **techniques d'attaque connues** utilisées par les attaquants dans des cyberattaques réelles.

- Créé par **MITRE Corporation**
- Site : [attack.mitre.org](https://attack.mitre.org/)
- **Standard mondial** utilisé par les SOC et équipes de threat intelligence

---

## Comment c'est organisé

- **14 tactiques** = le "pourquoi" (Initial Access, Persistence, Privilege Escalation, Impact...)
- **200+ techniques** = le "comment" (T1566 Phishing, T1003 Credential Dumping...)

---

## Exemple concret : ransomware

| Étape | Tactique | Technique |
|-------|----------|-----------|
| Email piégé | Initial Access | T1566 Phishing |
| Vol des mots de passe AD | Credential Access | T1003 OS Credential Dumping |
| Propagation réseau | Lateral Movement | T1021 Remote Services |
| Chiffrement des fichiers | Impact | T1486 Data Encrypted for Impact |

---

## Pourquoi ça m'intéresse

Quand une CVE sort sur le CERT-FR, je cherche à quelle **technique ATT&CK** elle correspond. Ça me donne le **scénario d'attaque complet**, pas juste la faille isolée.

**Exemple :** regreSSHion (CVE-2024-6387) → **T1190 Exploit Public-Facing Application** dans **Initial Access**.
