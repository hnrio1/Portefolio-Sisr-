# Fiche de veille — Faille XSS sur pfSense

**Date de publication :** 14/11/2023
**Date de consultation :** 20/11/2025
**Auteur de la veille :** Henrio Chambal
**Source :** NVD — https://nvd.nist.gov/vuln/detail/CVE-2023-42326
**Référence CVE :** CVE-2023-42326

---

## Résumé

Une vulnérabilité de type **Cross-Site Scripting (XSS)** a été découverte dans l'interface web de **pfSense CE et pfSense Plus**. Un attaquant authentifié peut injecter du code JavaScript malveillant via certains paramètres de l'interface, ce qui peut mener au vol de session administrateur.

## Systèmes / produits concernés

- pfSense CE < 2.7.1
- pfSense Plus < 23.09.1

## Niveau de gravité

- **Score CVSS :** 8.8 / 10
- **Criticité :** Important
- **Exploitation observée :** Non (mais preuve de concept disponible)

## Description technique

L'interface web de pfSense ne filtre pas correctement certaines entrées utilisateur dans les pages de configuration réseau. Un utilisateur ayant un accès (même limité) peut injecter du code JavaScript qui s'exécutera dans le navigateur de l'administrateur. Cela peut permettre de voler les cookies de session et de prendre le contrôle total du pare-feu.

## Impact potentiel

- Vol de session administrateur du pare-feu
- Modification des règles de filtrage (ouverture de ports, désactivation de la sécurité)
- Pivot vers le réseau interne

## Impact pour une infrastructure SISR

- **pfSense est utilisé en TP StadiumCompany** pour le pare-feu et le portail captif
- **Priorité : HAUTE** — mettre à jour pfSense et restreindre l'accès à l'interface web

## Correctif / mitigation recommandés

- **Mise à jour** vers pfSense CE 2.7.1 ou pfSense Plus 23.09.1
- Restreindre l'accès à l'interface web de pfSense (uniquement depuis le LAN admin)
- Utiliser HTTPS et des mots de passe forts
- Activer l'authentification à deux facteurs si disponible

## Lien avec MITRE ATT&CK

- Tactique : **Privilege Escalation**
- Technique : **T1059.007 — JavaScript**

## Ma synthèse personnelle

pfSense est un outil que j'utilise régulièrement en TP (portail captif, VPN, firewall). Savoir que l'interface web peut être vulnérable m'a fait prendre conscience qu'il ne faut jamais exposer une interface d'administration sur un réseau non sécurisé. En TP, on a tendance à tout laisser accessible, mais en production c'est une erreur grave.

