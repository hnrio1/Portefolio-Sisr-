import pdfplumber

# PDF avec "Non trouvé" pour les dates
pdf_path = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION\CECCA ETOILE\TEAM SIMBOU\ALEXIANE\#AP FOOD\ADMINISRTATIF\LETTRE DE MISSION\AP FOOD_ LETTRE DE MISSION CECCA ETOILE SIGNEE.pdf"

print("Extraction du texte du PDF...")
print("=" * 80)

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        texte = page.extract_text()
        if texte:
            print(f"\n--- PAGE {i+1} ---\n")
            print(texte)
        else:
            print(f"\n--- PAGE {i+1} : VIDE ou IMAGE ---\n")

print("\n" + "=" * 80)
print("FIN")
