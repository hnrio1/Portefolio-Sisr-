import pandas as pd
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import re

TESSERACT_PATH = r"C:\Users\henri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-25.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# Lire le fichier CSV pour trouver les "Non trouvé"
df = pd.read_csv(r"C:\Users\henri\Desktop\extraction_nouveau_dossier.csv", sep=';', encoding='utf-8-sig')

# Filtrer les lignes avec "Non trouvé" dans Date Signature
non_trouves = df[df['Date Signature'] == 'Non trouvé']

print(f"Nombre de fichiers sans date de signature: {len(non_trouves)}")
print("="*60)

# Analyser les 5 premiers pour voir le texte
count = 0
for idx, row in non_trouves.iterrows():
    if count >= 5:
        break

    chemin = row['Chemin']
    print(f"\n{'='*60}")
    print(f"Fichier: {row['Fichier']}")
    print(f"{'='*60}")

    # Extraire le texte
    texte = ""
    try:
        with pdfplumber.open(chemin) as pdf:
            for page in pdf.pages[:2]:  # Juste les 2 premières pages
                t = page.extract_text()
                if t:
                    texte += t + "\n"
    except:
        try:
            images = convert_from_path(chemin, poppler_path=POPPLER_PATH, dpi=150, first_page=1, last_page=2)
            for img in images:
                t = pytesseract.image_to_string(img, lang='fra+eng')
                if t:
                    texte += t + "\n"
        except Exception as e:
            print(f"Erreur: {e}")
            continue

    # Chercher des mots-clés liés à la date
    lignes_interessantes = []
    for ligne in texte.split('\n'):
        ligne_lower = ligne.lower()
        if any(mot in ligne_lower for mot in ['fait', 'sign', 'date', 'paris', 'lyon', 'marseille', 'le ', 'établi']):
            lignes_interessantes.append(ligne.strip())

    print("\nLignes potentiellement intéressantes:")
    for ligne in lignes_interessantes[:15]:
        if ligne:
            print(f"  -> {ligne}")

    count += 1

print("\n" + "="*60)
print("Analyse terminée. Regardez les patterns ci-dessus pour améliorer la détection.")
