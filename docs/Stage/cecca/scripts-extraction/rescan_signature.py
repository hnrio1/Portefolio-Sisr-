import os
import re
import pandas as pd
import pdfplumber
import pytesseract
from pdf2image import convert_from_path

TESSERACT_PATH = r"C:\Users\henri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-25.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

FICHIER_CSV = r"C:\Users\henri\Desktop\extraction_nouveau_dossier.csv"


def extraire_texte_pdf(chemin_pdf):
    """Extrait le texte d'un PDF."""
    texte = ""
    try:
        with pdfplumber.open(chemin_pdf) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    texte += t + "\n"
    except:
        pass

    if texte.strip():
        return texte

    # OCR si pas de texte
    try:
        images = convert_from_path(chemin_pdf, poppler_path=POPPLER_PATH, dpi=200)
        for img in images:
            t = pytesseract.image_to_string(img, lang='fra+eng')
            if t:
                texte += t + "\n"
    except:
        pass

    return texte


def extraire_date_signature(texte):
    """Extrait la date de signature avec les nouveaux patterns."""
    date_jj_mm_aaaa = r'\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4}'
    date_texte = r'\d{1,2}(?:er|ère|ere|ème|eme)?\s+(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre)\s+\d{4}'
    date_pattern = f'({date_jj_mm_aaaa}|{date_texte})'

    # PATTERN 1: "[Ville], le [date]"
    pattern_ville_le = r'[A-ZÀ-Ü][a-zà-ü]+(?:ville|sur|les|en|la|le|aux)?[,\s]+le\s+' + date_pattern
    match = re.search(pattern_ville_le, texte)
    if match:
        return match.group(1).strip()

    # PATTERN 2: "[VILLE], le [date]"
    pattern_ville_maj = r'[A-ZÀ-Ü]{2,}[,\s]+le\s+' + date_pattern
    match = re.search(pattern_ville_maj, texte)
    if match:
        return match.group(1).strip()

    # PATTERN 3: "Fait à [ville], le [date]"
    pattern_fait = r'[Ff]ait\s+[àa]\s+\w+[,\s]+le\s*' + date_pattern
    match = re.search(pattern_fait, texte, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # PATTERN 4: "Fait le [date]"
    pattern_fait2 = r'[Ff]ait\s+le\s*' + date_pattern
    match = re.search(pattern_fait2, texte, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # PATTERN 5: "Signé le [date]"
    pattern_signe = r'[Ss]ign[ée]\s+le\s*' + date_pattern
    match = re.search(pattern_signe, texte, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # PATTERN 6: "Date : [date]"
    pattern_date = r'[Dd]ate\s*:\s*' + date_pattern
    match = re.search(pattern_date, texte, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # PATTERN 7: "en date du [date]"
    pattern_en_date = r'en date du\s*' + date_pattern
    match = re.search(pattern_en_date, texte, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # PATTERN 8: "Le [date]" en début de phrase
    pattern_le = r'\.\s*[Ll]e\s+' + date_pattern
    match = re.search(pattern_le, texte)
    if match:
        return match.group(1).strip()

    # PATTERN 9: "A [ville], le [date]"
    pattern_a_ville = r'[AÀ]\s+\w+[,\s]+le\s*' + date_pattern
    match = re.search(pattern_a_ville, texte, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    return "Non trouvé"


def main():
    print(f"Lecture de: {FICHIER_CSV}")
    df = pd.read_csv(FICHIER_CSV, sep=';', encoding='utf-8-sig')

    # Trouver les lignes avec "Non trouvé" dans Date Signature
    mask_non_trouve = df['Date Signature'] == 'Non trouvé'
    nb_non_trouve = mask_non_trouve.sum()

    print(f"Fichiers à rescanner: {nb_non_trouve}")
    print("-" * 60)

    trouve = 0
    erreurs = 0

    for idx in df[mask_non_trouve].index:
        chemin = df.loc[idx, 'Chemin']
        fichier = df.loc[idx, 'Fichier']

        print(f"Rescan: {fichier[:45]}...", end=" ")

        if not os.path.exists(chemin):
            print("[FICHIER INTROUVABLE]")
            erreurs += 1
            continue

        texte = extraire_texte_pdf(chemin)
        if texte:
            date_signature = extraire_date_signature(texte)
            if date_signature != "Non trouvé":
                df.loc[idx, 'Date Signature'] = date_signature
                trouve += 1
                print(f"[TROUVÉ: {date_signature}]")
            else:
                print("[TOUJOURS NON TROUVÉ]")
        else:
            print("[ERREUR LECTURE]")
            erreurs += 1

    # Sauvegarder le CSV mis à jour
    df.to_csv(FICHIER_CSV, sep=';', index=False, encoding='utf-8-sig')

    print("-" * 60)
    print(f"TERMINE!")
    print(f"  - Nouvelles dates trouvées: {trouve}")
    print(f"  - Toujours non trouvées: {nb_non_trouve - trouve - erreurs}")
    print(f"  - Erreurs: {erreurs}")


if __name__ == "__main__":
    main()
