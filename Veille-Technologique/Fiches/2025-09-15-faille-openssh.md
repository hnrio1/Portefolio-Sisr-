# Fiche de veille — Vulnérabilité critique OpenSSH (regreSSHion)

**Date de publication :** 01/07/2024
**Date de consultation :** 15/09/2025
**Auteur de la veille :** Henrio Chambal
**Source :** CERT-FR — https://www.cert.ssi.gouv.fr/alerte/CERTFR-2024-ALE-009/
**Référence CVE :** CVE-2024-6387

---

## Résumé

Une vulnérabilité critique a été découverte dans OpenSSH, baptisée **regreSSHion**. Elle permet à un attaquant non authentifié d'exécuter du code arbitraire à distance avec les privilèges root sur les serveurs Linux utilisant OpenSSH. C'est la première faille critique sur OpenSSH depuis 18 ans.

## Systèmes / produits concernés

- OpenSSH versions 8.5p1 à 9.7p1
- Toutes les distributions Linux utilisant glibc (Debian, Ubuntu, CentOS, etc.)
- **Non affecté :** OpenBSD, Windows

## Niveau de gravité

- **Score CVSS :** 8.1 / 10
- **Criticité :** Critique
- **Exploitation observée :** Oui (preuve de concept publique)

## Description technique

La faille est un **race condition** dans le gestionnaire de signal de sshd. En envoyant des connexions spécialement conçues au serveur SSH, un attaquant peut provoquer une corruption mémoire et exécuter du code en tant que root, sans aucune authentification nécessaire.

## Impact potentiel

- **Prise de contrôle totale du serveur** (root)
- Vol de données, installation de malware, pivot vers le réseau interne
- Extrêmement dangereux car SSH est exposé sur presque tous les serveurs Linux

## Impact pour une infrastructure SISR

- **Serveurs Linux en stage CECCA et en TP** : tous les serveurs avec SSH exposé sont concernés
- **Priorité : URGENTE** — mise à jour immédiate requise

## Correctif / mitigation recommandés

- **Mise à jour** vers OpenSSH 9.8p1 ou supérieur
- En attendant le patch : limiter le nombre de connexions SSH simultanées via `MaxStartups` dans sshd_config
- Restreindre l'accès SSH par IP via le pare-feu (UFW, iptables)
- Utiliser Fail2ban pour limiter les tentatives de connexion

## Lien avec MITRE ATT&CK

- Tactique : **Initial Access**
- Technique : **T1190 — Exploit Public-Facing Application**

## Ma synthèse personnelle

Cette faille m'a marqué car SSH est un service que j'utilise quotidiennement en TP et en stage. Ça montre qu'un service considéré comme sûr peut contenir des failles critiques. Ça renforce l'importance de la mise à jour régulière, ce que j'ai mis en pratique pendant mon stage CECCA lors de la gestion des vulnérabilités.

