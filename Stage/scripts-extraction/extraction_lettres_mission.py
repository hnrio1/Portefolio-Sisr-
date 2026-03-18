import os
import re
import csv

# Configuration Tesseract et Poppler
TESSERACT_PATH = r"C:\Users\henri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-25.11.0\Library\bin"

# Essayer d'importer pdfplumber
try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

# Essayer d'importer les outils OCR
try:
    import pytesseract
    from pdf2image import convert_from_path
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    HAS_OCR = True
except ImportError:
    HAS_OCR = False
    print("ATTENTION: OCR non disponible. Installez: pip install pytesseract pdf2image")

if not HAS_PDFPLUMBER and not HAS_OCR:
    print("ERREUR: Aucune bibliothèque PDF installée.")
    exit(1)

# Chemin du dossier principal
DOSSIER_PRINCIPAL = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION"

# Fichier de sortie CSV
FICHIER_SORTIE = r"C:\Users\henri\Desktop\extraction_lettres_mission.csv"


def extraire_texte_pdf_normal(chemin_pdf):
    """Extrait le texte d'un fichier PDF avec pdfplumber."""
    texte = ""
    try:
        with pdfplumber.open(chemin_pdf) as pdf:
            for page in pdf.pages:
                contenu = page.extract_text()
                if contenu:
                    texte += contenu + "\n"
    except Exception as e:
        pass
    return texte.strip()


def extraire_texte_pdf_ocr(chemin_pdf):
    """Extrait le texte d'un PDF scanné avec OCR."""
    texte = ""
    try:
        # Convertir PDF en images
        images = convert_from_path(chemin_pdf, poppler_path=POPPLER_PATH, dpi=200)

        # OCR sur chaque image
        for image in images:
            contenu = pytesseract.image_to_string(image, lang='fra+eng')
            if contenu:
                texte += contenu + "\n"
    except Exception as e:
        print(f"    Erreur OCR: {str(e)[:50]}")
    return texte.strip()


def extraire_texte_pdf(chemin_pdf):
    """Extrait le texte d'un PDF (normal ou scanné)."""
    # D'abord essayer la méthode normale (rapide)
    if HAS_PDFPLUMBER:
        texte = extraire_texte_pdf_normal(chemin_pdf)
        if texte:
            return texte, "normal"

    # Si pas de texte, essayer l'OCR (lent)
    if HAS_OCR:
        texte = extraire_texte_pdf_ocr(chemin_pdf)
        if texte:
            return texte, "ocr"

    return "", "erreur"


def extraire_siren(texte):
    """Extrait le numéro SIREN (9 chiffres) du texte."""
    patterns = [
        r'(?:RCS|R\.C\.S|Registre du Commerce)[^\d]*(\d{3}[\s\.]?\d{3}[\s\.]?\d{3})',
        r'(?:immatricul|SIREN|n°)[^\d]*(\d{3}[\s\.]?\d{3}[\s\.]?\d{3})',
        r'sous le n[°o]\s*(\d{3}[\s\.]?\d{3}[\s\.]?\d{3})',
        r'sous le\s+(\d{3}[\s\.]?\d{3}[\s\.]?\d{3})',
    ]

    for pattern in patterns:
        match = re.search(pattern, texte, re.IGNORECASE)
        if match:
            siren = re.sub(r'[\s\.]', '', match.group(1))
            if len(siren) == 9 and siren.isdigit():
                return siren

    match = re.search(r'\b(\d{3}[\s\.]?\d{3}[\s\.]?\d{3})\b', texte)
    if match:
        siren = re.sub(r'[\s\.]', '', match.group(1))
        if len(siren) == 9:
            return siren

    return "Non trouvé"


def extraire_dates_exercice(texte):
    """Extrait les dates de début et fin d'exercice."""
    debut = "Non trouvé"
    fin = "Non trouvé"

    date_jj_mm_aaaa = r'\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4}'
    date_texte = r'\d{1,2}(?:er|ère|ere)?\s+(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre)\s+\d{4}'
    date_pattern = f'({date_jj_mm_aaaa}|{date_texte})'

    # PATTERN 1: "commençant le ... se terminant le ..."
    pattern_exercice = r'commen[çc]ant le\s*[":]*\s*' + date_pattern + r'.*?(?:se )?terminant le\s*[":]*\s*' + date_pattern
    match = re.search(pattern_exercice, texte, re.IGNORECASE | re.DOTALL)
    if match:
        debut = match.group(1).strip()
        fin = match.group(2).strip()
        return debut, fin

    # PATTERN 2: "du ... au ..."
    pattern_du_au = r'(?:exercice|période|comptes?).*?du\s+' + date_pattern + r'\s+au\s+' + date_pattern
    match = re.search(pattern_du_au, texte, re.IGNORECASE | re.DOTALL)
    if match:
        debut = match.group(1).strip()
        fin = match.group(2).strip()
        return debut, fin

    # PATTERN 3: Deux dates sur la même ligne
    pattern_deux_dates = r'(' + date_jj_mm_aaaa + r')\s+(' + date_jj_mm_aaaa + r')'
    matches = re.findall(pattern_deux_dates, texte)
    if matches:
        debut = matches[0][0].strip()
        fin = matches[0][1].strip()
        return debut, fin

    # PATTERN 4: Recherche séparée
    pattern_debut = r'commen[çc]ant le\s*[":]*\s*' + date_pattern
    pattern_fin = r'(?:se )?terminant le\s*[":]*\s*' + date_pattern

    match_debut = re.search(pattern_debut, texte, re.IGNORECASE)
    match_fin = re.search(pattern_fin, texte, re.IGNORECASE)

    if match_debut:
        debut = match_debut.group(1).strip()
    if match_fin:
        fin = match_fin.group(1).strip()

    # PATTERN 5: "à compter du"
    if debut == "Non trouvé":
        pattern_compter = r'[àa] compter du\s*' + date_pattern
        match_compter = re.search(pattern_compter, texte, re.IGNORECASE)
        if match_compter:
            debut = match_compter.group(1).strip()

    # PATTERN 6: "depuis le"
    if debut == "Non trouvé":
        pattern_depuis = r'depuis le\s*' + date_pattern
        match_depuis = re.search(pattern_depuis, texte, re.IGNORECASE)
        if match_depuis:
            debut = match_depuis.group(1).strip()

    # PATTERN 7: "exercice" suivi d'une date
    if debut == "Non trouvé" and fin == "Non trouvé":
        pattern_exercice_date = r'exercice[^\d]*(' + date_jj_mm_aaaa + r')'
        match_ex = re.search(pattern_exercice_date, texte, re.IGNORECASE)
        if match_ex:
            debut = match_ex.group(1).strip()

    # PATTERN 8: "clos le" ou "clôturé le"
    if fin == "Non trouvé":
        pattern_clos = r'(?:clos|clôtur[ée]|clotur[ée])\s+le\s*' + date_pattern
        match_clos = re.search(pattern_clos, texte, re.IGNORECASE)
        if match_clos:
            fin = match_clos.group(1).strip()

    # PATTERN 9: "31/12/XXXX"
    if fin == "Non trouvé":
        pattern_fin_annee = r'(31[/\-\.]\s*12[/\-\.]\s*\d{4}|31\s+d[ée]cembre\s+\d{4})'
        match_fin_annee = re.search(pattern_fin_annee, texte, re.IGNORECASE)
        if match_fin_annee:
            fin = match_fin_annee.group(1).strip()

    return debut, fin


def extraire_nom_client(chemin_fichier):
    """Extrait le nom du client depuis le nom du fichier."""
    nom_fichier = os.path.basename(chemin_fichier)
    nom_fichier = os.path.splitext(nom_fichier)[0]

    nom = nom_fichier
    mots_a_enlever = ['LETTRE DE MISSION', 'CECCA ETOILE', 'SIGNEE', 'SIGNED',
                       'COEXPAU', 'MAVRICK', '(signed)', '_', '-', 'LM']
    for mot in mots_a_enlever:
        nom = nom.replace(mot, ' ')

    nom = ' '.join(nom.split()).strip()
    return nom if nom else nom_fichier


def main():
    resultats = []
    fichiers_traites = 0
    fichiers_ocr = 0
    erreurs = 0

    print(f"Parcours du dossier: {DOSSIER_PRINCIPAL}")
    print(f"OCR disponible: {HAS_OCR}")
    print("-" * 60)

    # Parcourir tous les fichiers PDF
    for racine, dossiers, fichiers in os.walk(DOSSIER_PRINCIPAL):
        for fichier in fichiers:
            if fichier.lower().endswith('.pdf'):
                chemin_complet = os.path.join(racine, fichier)

                print(f"Traitement: {fichier[:45]}...", end=" ")

                # Extraire le texte du PDF
                texte, methode = extraire_texte_pdf(chemin_complet)

                if texte:
                    nom_client = extraire_nom_client(chemin_complet)
                    siren = extraire_siren(texte)
                    date_debut, date_fin = extraire_dates_exercice(texte)

                    resultats.append({
                        'Nom Client': nom_client,
                        'SIREN': siren,
                        'Debut Exercice': date_debut,
                        'Fin Exercice': date_fin,
                        'Fichier': fichier,
                        'Chemin': chemin_complet
                    })
                    fichiers_traites += 1

                    if methode == "ocr":
                        fichiers_ocr += 1
                        print("[OCR OK]")
                    else:
                        print("[OK]")
                else:
                    print("[ERREUR]")
                    erreurs += 1

    # Écrire le fichier CSV
    print("-" * 60)
    print(f"Écriture du fichier CSV: {FICHIER_SORTIE}")

    with open(FICHIER_SORTIE, 'w', newline='', encoding='utf-8-sig') as csvfile:
        colonnes = ['Nom Client', 'SIREN', 'Debut Exercice', 'Fin Exercice', 'Fichier', 'Chemin']
        writer = csv.DictWriter(csvfile, fieldnames=colonnes, delimiter=';')

        writer.writeheader()
        for resultat in resultats:
            writer.writerow(resultat)

    print("-" * 60)
    print(f"TERMINE!")
    print(f"  - Fichiers traités (normal): {fichiers_traites - fichiers_ocr}")
    print(f"  - Fichiers traités (OCR): {fichiers_ocr}")
    print(f"  - Total traités: {fichiers_traites}")
    print(f"  - Erreurs: {erreurs}")
    print(f"  - Résultats: {FICHIER_SORTIE}")


if __name__ == "__main__":
    main()
