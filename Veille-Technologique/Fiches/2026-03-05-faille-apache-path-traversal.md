# Fiche de veille — Vulnérabilité Path Traversal sur Apache HTTP Server

**Date de publication :** 04/10/2021 (résurgence en 2025-2026)
**Date de consultation :** 05/03/2026
**Auteur de la veille :** Henrio Chambal
**Source :** CERT-FR — https://www.cert.ssi.gouv.fr/alerte/CERTFR-2021-ALE-018/
**Référence CVE :** CVE-2021-41773

---

## Résumé

Une vulnérabilité de type **path traversal** dans Apache HTTP Server 2.4.49 permet à un attaquant d'accéder à des fichiers en dehors du répertoire web, voire d'exécuter du code à distance si mod_cgi est activé. La faille est triviale à exploiter et a été massivement utilisée dans la nature.

## Systèmes / produits concernés

- Apache HTTP Server 2.4.49 et 2.4.50
- Tous les OS (Linux, Windows)

## Niveau de gravité

- **Score CVSS :** 9.8 / 10
- **Criticité :** Critique
- **Exploitation observée :** Oui (exploitée massivement dès la publication)

## Description technique

Apache 2.4.49 a introduit un nouveau mécanisme de normalisation des URL qui contient un bug. En utilisant un encodage spécial des caractères `../` (comme `%2e%2e/`), un attaquant peut contourner les restrictions de répertoire et lire n'importe quel fichier sur le serveur (ex: `/etc/passwd`). Si `mod_cgi` est activé, il peut aussi exécuter des commandes système.

## Impact potentiel

- Lecture de fichiers sensibles (mots de passe, configuration, clés privées)
- Exécution de commandes à distance (si mod_cgi actif)
- Compromission totale du serveur web

## Impact pour une infrastructure SISR

- **Apache est utilisé en TP StadiumCompany** et dans le déploiement Nextcloud au stage Pasteur
- **Priorité : CRITIQUE** — vérifier la version d'Apache et mettre à jour

## Correctif / mitigation recommandés

- **Mise à jour** vers Apache 2.4.51 ou supérieur
- Désactiver mod_cgi si non nécessaire
- Vérifier les directives `Require all denied` sur les répertoires sensibles
- Surveiller les logs d'accès pour détecter les tentatives de path traversal (`%2e%2e`)

## Lien avec MITRE ATT&CK

- Tactique : **Initial Access**
- Technique : **T1190 — Exploit Public-Facing Application**

## Ma synthèse personnelle

Cette faille m'a frappé par sa simplicité : un simple `curl` avec des caractères encodés suffit pour lire `/etc/passwd`. En stage Pasteur j'ai déployé Apache avec Ansible, et cette CVE m'a rappelé l'importance de toujours vérifier les versions des services qu'on installe. Une version obsolète peut transformer un serveur sécurisé en porte ouverte.

