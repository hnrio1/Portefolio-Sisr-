# COMPTE RENDU DE MISSION
## Analyse de l'utilisation de Leviia et propositions d'amélioration

---

**Auteur :** [Ton nom]
**Date :** 27 novembre 2025
**Tuteur :** [Nom du tuteur]
**Durée de la mission :** 1,5 semaine
**Objet :** Recensement des lettres de mission comptables

---

## 1. Contexte de la mission

Dans le cadre de ma mission au sein du cabinet, j'ai été chargé de recenser l'ensemble des lettres de mission des comptables. Cette tâche a nécessité une semaine et demie de travail, durant laquelle j'ai pu identifier plusieurs dysfonctionnements liés à l'utilisation de la plateforme Leviia.

**Périmètre concerné :**
- Environ 2 800 clients
- Organisation par équipe : Team → Manager → Comptable → Dossiers clients

---

## 2. Problèmes identifiés

### 2.1 Absence de filtres de recherche efficaces

La plateforme Leviia ne propose pas de système de filtrage avancé permettant de rechercher des documents par type, date ou mots-clés. Chaque recherche doit être effectuée manuellement, dossier par dossier.

**Impact :** Temps de recherche considérablement allongé. Une tâche qui aurait pu prendre quelques heures a nécessité plus d'une semaine.

### 2.2 Arborescence peu claire

L'organisation actuelle repose sur une structure hiérarchique (Team → Manager → Comptable → Client) qui, bien que logique sur le papier, devient difficile à naviguer avec un volume de 2 800 clients.

**Impact :** Difficulté à localiser rapidement un dossier client spécifique.

### 2.3 Nombreux doublons

De nombreux fichiers existent en plusieurs exemplaires dans différents emplacements, sans indication claire de la version à jour.

**Impact :**
- Confusion sur le document de référence
- Espace de stockage utilisé inutilement
- Risque d'utiliser une version obsolète

### 2.4 Absence de convention de nommage

Chaque collaborateur nomme ses fichiers selon ses propres habitudes, rendant la recherche par nom de fichier inefficace.

**Impact :** Impossibilité d'exploiter la recherche textuelle de manière fiable.

---

## 3. Solutions proposées

### 3.1 Solution A : Optimisation de l'organisation actuelle (sans changement d'outil)

Cette approche consiste à améliorer l'utilisation de Leviia sans changer de plateforme.

**Actions recommandées :**

1. **Mettre en place une convention de nommage stricte**
   - Format proposé : `[NomClient]_[TypeDocument]_[Année].pdf`
   - Exemple : `DUPONT_LettredeMission_2025.pdf`

2. **Restructurer l'arborescence**
   ```
   📁 CLIENTS
      📁 A-E
         📁 [NomClient_NuméroClient]
            📁 01_Lettres_de_mission
            📁 02_Bilans
            📁 03_Fiscal
            📁 04_Social
      📁 F-J
      📁 K-O
      📁 P-T
      📁 U-Z
   ```

3. **Purger les doublons existants**
   - Identifier et supprimer les fichiers en double
   - Définir une règle : un seul fichier définitif par document

**Avantages :** Aucun coût supplémentaire, mise en place rapide
**Limites :** Ne résout pas l'absence de filtres de recherche natifs

---

### 3.2 Solution B : Migration vers une nouvelle solution cloud

Plusieurs alternatives existent sur le marché, mieux adaptées aux besoins d'un cabinet comptable de cette envergure.

| Solution | Points forts | Points faibles | Coût estimé |
|----------|--------------|----------------|-------------|
| **Zeendoc** | GED spécialisée comptabilité, OCR automatique, recherche puissante, workflows de validation | Coût plus élevé, temps de migration | €€€ |
| **MyCompanyFiles** | Conçu pour les cabinets comptables, portail client intégré | Moins de flexibilité | €€ |
| **SharePoint (Microsoft 365)** | Filtres avancés, métadonnées personnalisables, intégration Office | Configuration complexe | Inclus si abonnement Microsoft 365 |
| **Google Workspace** | Recherche très performante, OCR intégré, interface intuitive | Moins orienté "métier comptable" | € |

**Recommandation :** Pour un cabinet de 2 800 clients, **Zeendoc** ou **SharePoint** semblent les plus adaptés. Zeendoc offre des fonctionnalités métier spécifiques à la comptabilité, tandis que SharePoint s'intègre parfaitement si le cabinet utilise déjà Microsoft 365.

---

### 3.3 Solution C : Mise en place d'un NAS (Network Attached Storage)

Un NAS est un serveur de stockage local accessible par tous les collaborateurs via le réseau du cabinet.

**Fonctionnement :**
- Stockage centralisé sur des disques durs internes au cabinet
- Accès via le réseau local ou à distance (VPN / application dédiée)
- Moteur de recherche intégré avec indexation des fichiers

**Modèles recommandés :**
- Synology DS423+ (4 baies, évolutif)
- QNAP TS-464

**Avantages :**
- Capacité de stockage évolutive (ajout de disques)
- Recherche rapide grâce à l'indexation locale
- Contrôle total des données (pas de dépendance à un prestataire externe)
- Coût maîtrisé sur le long terme (pas d'abonnement mensuel)

**Inconvénients :**
- Investissement initial : 500 € à 1 500 € selon la configuration
- Nécessite une gestion technique (mises à jour, sauvegardes)
- Accès à distance moins fluide qu'une solution 100% cloud

**Recommandation :** Solution pertinente si le cabinet souhaite internaliser la gestion des données et dispose d'une ressource technique pour la maintenance.

---

## 4. Tableau comparatif des solutions

| Critère | Optimisation Leviia | Zeendoc / SharePoint | NAS |
|---------|---------------------|----------------------|-----|
| Coût | Aucun | Abonnement mensuel | Investissement initial |
| Temps de mise en place | Court | Moyen (migration) | Moyen |
| Recherche avancée | ❌ Non | ✅ Oui | ✅ Oui |
| Adapté à 2800 clients | ⚠️ Limité | ✅ Oui | ✅ Oui |
| Accès à distance | ✅ Oui | ✅ Oui | ⚠️ Possible (VPN) |
| Maintenance | Aucune | Par le prestataire | En interne |

---

## 5. Recommandation finale

Au regard des problèmes identifiés et du volume de clients à gérer (2 800), je recommande une approche en deux temps :

### Court terme (immédiat)
- Mettre en place une **convention de nommage** pour tous les nouveaux documents
- Lancer un **nettoyage des doublons** progressif
- Sensibiliser les équipes aux bonnes pratiques de classement

### Long terme (à planifier)
- Évaluer une **migration vers Zeendoc ou SharePoint** pour bénéficier de fonctionnalités de recherche et de gestion documentaire adaptées à un cabinet de cette taille
- Alternativement, étudier la mise en place d'un **NAS** si le cabinet souhaite internaliser le stockage

---

## 6. Conclusion

La mission de recensement des lettres de mission a mis en lumière plusieurs axes d'amélioration dans la gestion documentaire du cabinet. Les solutions proposées permettront, selon l'option retenue, d'optimiser significativement le temps de recherche et la fiabilité des données.

Je reste à disposition pour approfondir l'une ou l'autre de ces pistes.

---

**[Ton nom]**
**[Date]**
