# Fiche de veille — Élévation de privilèges Active Directory (Zerologon)

**Date de publication :** 11/08/2020 (redécouverte et exploitée activement en 2025)
**Date de consultation :** 10/01/2026
**Auteur de la veille :** Henrio Chambal
**Source :** CERT-FR — https://www.cert.ssi.gouv.fr/alerte/CERTFR-2020-ALE-020/
**Référence CVE :** CVE-2020-1472

---

## Résumé

**Zerologon** est une vulnérabilité critique dans le protocole **Netlogon** de Windows Server. Elle permet à un attaquant ayant un accès réseau au contrôleur de domaine de **devenir administrateur du domaine Active Directory** sans aucun identifiant. Malgré un correctif disponible depuis 2020, des systèmes non patchés sont encore exploités en 2025.

## Systèmes / produits concernés

- Windows Server 2008 R2 à 2019
- Tout contrôleur de domaine Active Directory non patché

## Niveau de gravité

- **Score CVSS :** 10.0 / 10
- **Criticité :** Critique (score maximum)
- **Exploitation observée :** Oui (utilisée par des groupes APT et des ransomwares)

## Description technique

Le protocole Netlogon utilise un chiffrement AES-CFB8 avec un vecteur d'initialisation (IV) fixé à zéro. En envoyant des requêtes avec des zéros, un attaquant peut, en moyenne après 256 tentatives, s'authentifier comme le contrôleur de domaine lui-même. Il peut ensuite changer le mot de passe du compte machine du DC et prendre le contrôle complet de l'Active Directory.

## Impact potentiel

- **Compromission totale du domaine Active Directory**
- Accès à tous les comptes utilisateurs et machines
- Déploiement de ransomware sur tout le réseau
- Vol massif de données

## Impact pour une infrastructure SISR

- **L'Active Directory est au cœur du TP StadiumCompany** (gestion des utilisateurs, GPO, DNS)
- **Priorité : CRITIQUE** — s'assurer que tous les DC sont patchés

## Correctif / mitigation recommandés

- **Appliquer le patch Microsoft** KB4571702 (août 2020)
- Activer le mode **"enforcement"** de Netlogon (obligatoire depuis février 2021)
- Surveiller les logs Netlogon (Event ID 5829) pour détecter les connexions vulnérables
- Segmenter le réseau pour limiter l'accès direct au DC

## Lien avec MITRE ATT&CK

- Tactique : **Privilege Escalation**
- Technique : **T1068 — Exploitation for Privilege Escalation**

## Ma synthèse personnelle

Zerologon est un cas d'école en cybersécurité : un score CVSS de 10/10, une exploitation triviale et un impact dévastateur. Ça m'a fait comprendre pourquoi les mises à jour Windows Server ne doivent jamais être reportées, surtout sur les contrôleurs de domaine. En TP Active Directory, on n'y pense pas, mais en entreprise un DC non patché peut compromettre tout le SI en quelques secondes.

