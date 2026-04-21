import os
import pdfplumber
from PyPDF2 import PdfReader

DOSSIER_PRINCIPAL = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION"

def analyser_pdf(chemin):
    """Analyse un PDF pour comprendre pourquoi il ne peut pas être lu."""
    resultats = {
        'chemin': chemin,
        'nom': os.path.basename(chemin),
        'taille': 0,
        'nb_pages': 0,
        'pdfplumber_ok': False,
        'pypdf2_ok': False,
        'texte_pdfplumber': "",
        'texte_pypdf2': "",
        'est_image': False,
        'est_protege': False,
        'erreur': ""
    }

    try:
        resultats['taille'] = os.path.getsize(chemin)
    except:
        pass

    # Test avec pdfplumber
    try:
        with pdfplumber.open(chemin) as pdf:
            resultats['nb_pages'] = len(pdf.pages)
            texte = ""
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    texte += t
            resultats['texte_pdfplumber'] = texte[:500] if texte else ""
            resultats['pdfplumber_ok'] = bool(texte.strip())
    except Exception as e:
        resultats['erreur'] += f"pdfplumber: {str(e)[:100]}; "

    # Test avec PyPDF2
    try:
        with open(chemin, 'rb') as f:
            reader = PdfReader(f)
            if reader.is_encrypted:
                resultats['est_protege'] = True
            else:
                texte = ""
                for page in reader.pages:
                    t = page.extract_text()
                    if t:
                        texte += t
                resultats['texte_pypdf2'] = texte[:500] if texte else ""
                resultats['pypdf2_ok'] = bool(texte.strip())
    except Exception as e:
        resultats['erreur'] += f"pypdf2: {str(e)[:100]}; "

    # Déterminer si c'est probablement une image
    if not resultats['pdfplumber_ok'] and not resultats['pypdf2_ok'] and not resultats['est_protege']:
        resultats['est_image'] = True

    return resultats


def main():
    print("Recherche des PDF qui ne peuvent pas être lus...")
    print("=" * 80)

    erreurs = []
    total_pdf = 0

    for racine, dossiers, fichiers in os.walk(DOSSIER_PRINCIPAL):
        for fichier in fichiers:
            if fichier.lower().endswith('.pdf'):
                total_pdf += 1
                chemin = os.path.join(racine, fichier)

                # Test rapide avec pdfplumber
                try:
                    with pdfplumber.open(chemin) as pdf:
                        texte = ""
                        for page in pdf.pages:
                            t = page.extract_text()
                            if t:
                                texte += t
                        if not texte.strip():
                            erreurs.append(chemin)
                except:
                    erreurs.append(chemin)

    print(f"Total PDF: {total_pdf}")
    print(f"PDF avec erreurs: {len(erreurs)}")
    print("=" * 80)

    # Analyser les erreurs en détail
    stats = {
        'images': 0,
        'proteges': 0,
        'autres': 0
    }

    print("\nAnalyse détaillée des erreurs...\n")

    for i, chemin in enumerate(erreurs[:20]):  # Analyser les 20 premiers
        print(f"\n--- Fichier {i+1}/{len(erreurs)} ---")
        print(f"Nom: {os.path.basename(chemin)}")

        result = analyser_pdf(chemin)

        print(f"Taille: {result['taille']} bytes")
        print(f"Pages: {result['nb_pages']}")
        print(f"Protégé: {result['est_protege']}")
        print(f"Probablement image/scan: {result['est_image']}")

        if result['est_protege']:
            stats['proteges'] += 1
        elif result['est_image']:
            stats['images'] += 1
        else:
            stats['autres'] += 1

        if result['erreur']:
            print(f"Erreurs: {result['erreur']}")

        if result['texte_pypdf2'] and not result['texte_pdfplumber']:
            print("-> PyPDF2 peut lire ce fichier!")
            print(f"Extrait: {result['texte_pypdf2'][:200]}...")

    print("\n" + "=" * 80)
    print("RÉSUMÉ (sur les 20 premiers analysés):")
    print(f"  - PDF scannés (images): {stats['images']}")
    print(f"  - PDF protégés: {stats['proteges']}")
    print(f"  - Autres erreurs: {stats['autres']}")

    # Sauvegarder la liste des fichiers en erreur
    with open(r"C:\Users\henri\Desktop\fichiers_erreurs.txt", 'w', encoding='utf-8') as f:
        f.write(f"Total: {len(erreurs)} fichiers en erreur\n\n")
        for chemin in erreurs:
            f.write(chemin + "\n")

    print(f"\nListe complète sauvegardée dans: C:\\Users\\henri\\Desktop\\fichiers_erreurs.txt")


if __name__ == "__main__":
    main()
