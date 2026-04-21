# Scripts d'Extraction de Données - Stage CECCA

## Description

Suite de scripts Python développés lors de mon stage au cabinet comptable **CECCA** pour automatiser le recensement et l'extraction de données depuis environ **2 800 dossiers clients** stockés sur la plateforme cloud Leviia.

## Contexte

Le cabinet utilisait la plateforme Leviia pour stocker les documents clients, mais l'absence de filtres de recherche efficaces rendait le recensement des lettres de mission extrêmement chronophage. J'ai développé ces scripts pour automatiser l'extraction des informations clés depuis les fichiers PDF.

## Fonctionnalités

- **Extraction automatique** des données depuis des PDF (texte natif + OCR pour les scans)
- **Détection intelligente** des numéros SIREN via regex multi-patterns
- **Extraction des dates** d'exercice et de signature
- **Diagnostic d'erreurs** et validation des données extraites
- **Nettoyage et fusion** des fichiers CSV/Excel générés
- **Gestion des chemins longs** Windows (>260 caractères)

## Technologies utilisées

- **Python 3** - Langage de programmation
- **pdfplumber** - Extraction de texte PDF
- **pytesseract** - OCR (reconnaissance optique de caractères)
- **pdf2image / Poppler** - Conversion PDF vers image
- **regex** - Patterns d'extraction avancés
- **csv** - Export des résultats

## Scripts principaux

| Script | Rôle |
|--------|------|
| `extraction_lettres_mission.py` | Extraction des données des lettres de mission (SIREN, dates d'exercice) |
| `extraction_nouveau_dossier.py` | Version améliorée avec extraction des dates de signature |
| `diagnostic_erreurs.py` | Analyse et diagnostic des erreurs d'extraction |
| `diagnostic_signature.py` | Vérification des signatures dans les PDF |
| `nettoyer_csv.py` | Nettoyage des données CSV |
| `nettoyer_excel.py` | Nettoyage des données Excel |
| `fusionner_excel.py` | Fusion de plusieurs fichiers Excel |
| `rescan_signature.py` | Re-scan ciblé des PDF sans signature détectée |

## Résultats

- Automatisation d'une tâche qui prenait **1,5 semaine manuellement**
- Traitement de **~2 800 dossiers clients**
- Support des PDF natifs et scannés (OCR)
- Proposition de solutions d'amélioration pour la gestion documentaire du cabinet

## Compétences mobilisées

- Développement Python
- Traitement automatisé de documents (PDF, OCR)
- Expressions régulières avancées
- Analyse de données
- Proposition de solutions techniques en contexte professionnel

## Fichiers

- `Compte_Rendu_Leviia.md` - Compte rendu de mission avec analyse et recommandations
