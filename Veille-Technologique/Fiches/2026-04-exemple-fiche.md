# Fiche de veille — Exemple (à utiliser comme modèle rempli)

> **Note :** cette fiche est un **exemple pédagogique** montrant comment remplir une fiche de veille. Les fiches réelles seront datées de leur consultation effective et ajoutées au fur et à mesure de ma veille hebdomadaire.

---

**Date de publication :** (à compléter avec un bulletin réel consulté)
**Date de consultation :** (à compléter)
**Auteur de la veille :** Henrio Chambal
**Source :** CERT-FR — https://www.cert.ssi.gouv.fr/
**Type de bulletin :** Avis / Alerte

---

## Structure type à remplir

### Résumé
En 3 à 5 lignes, je résume l'information principale : quel produit est touché, quel type de vulnérabilité, quel est le risque.

### Systèmes concernés
Liste des produits et versions vulnérables (ex : Windows Server 2019, Apache 2.4.x, OpenSSH < 9.6).

### Niveau de gravité
Le CERT-FR et le NVD attribuent un score CVSS (de 0 à 10). Je note ce score et je classe en : Critique (9-10), Important (7-8.9), Modéré (4-6.9), Faible (<4).

### Description technique
Explication de la faille en termes simples : qu'est-ce qui est cassé, comment on peut l'exploiter.

### Impact potentiel
Les conséquences possibles : exécution de code à distance, élévation de privilèges, divulgation d'informations, déni de service, etc.

### Impact pour un environnement SISR type
- **Infra StadiumCompany** : est-ce qu'un de nos composants est touché ? (AD, pfSense, Apache, Debian, etc.)
- **Priorité de traitement** : urgent / normal / surveillé

### Correctif / mitigation
- Patch officiel : lien vers la page de l'éditeur
- Contournement si pas de patch disponible
- Recommandations complémentaires (durcissement, segmentation réseau, etc.)

### Lien avec MITRE ATT&CK
Si la vulnérabilité peut être rattachée à une technique ATT&CK, je l'indique ici.

### Ma synthèse personnelle
Ce que je retiens, en 2-3 lignes. Pourquoi cette info m'a intéressé, ce qu'elle m'apprend sur le métier.

### Compétences BTS SIO
Je coche les compétences du bloc 2 SISR concernées par cette information.

---

**Utilisation :** copier [MODELE-fiche.md](./MODELE-fiche.md), le renommer avec la date (format `AAAA-MM-JJ-titre-court.md`) et remplir chaque section.
