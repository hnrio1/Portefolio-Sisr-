import os
import pdfplumber
import pytesseract
from pdf2image import convert_from_path

TESSERACT_PATH = r"C:\Users\henri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-25.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

DOSSIER = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION\Dossier\Tous les fichiers\CECCA"

erreurs = []
succes = []

print("Analyse des fichiers PDF...")
print("=" * 60)

for racine, dossiers, fichiers in os.walk(DOSSIER):
    for fichier in fichiers:
        if fichier.lower().endswith('.pdf'):
            chemin = os.path.join(racine, fichier)

            # Test pdfplumber
            texte_normal = ""
            try:
                with pdfplumber.open(chemin) as pdf:
                    for page in pdf.pages:
                        t = page.extract_text()
                        if t:
                            texte_normal += t
            except Exception as e:
                pass

            if texte_normal.strip():
                succes.append((fichier, "pdfplumber"))
                continue

            # Test OCR
            texte_ocr = ""
            try:
                images = convert_from_path(chemin, poppler_path=POPPLER_PATH, dpi=150)
                for img in images:
                    t = pytesseract.image_to_string(img, lang='fra+eng')
                    if t:
                        texte_ocr += t
            except Exception as e:
                erreurs.append((fichier, chemin, f"OCR Error: {str(e)[:80]}"))
                continue

            if texte_ocr.strip():
                succes.append((fichier, "OCR"))
            else:
                erreurs.append((fichier, chemin, "Aucun texte extrait (PDF vide ou illisible)"))

print(f"\nSUCCÈS: {len(succes)} fichiers")
print(f"ERREURS: {len(erreurs)} fichiers")

print("\n" + "=" * 60)
print("LISTE DES FICHIERS EN ERREUR:")
print("=" * 60)

for nom, chemin, raison in erreurs:
    print(f"\nFichier: {nom}")
    print(f"Chemin: {chemin}")
    print(f"Raison: {raison}")
