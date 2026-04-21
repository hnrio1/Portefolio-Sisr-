import pandas as pd
import re

FICHIER_ENTREE = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION\LM EXCEL\extraction_lettres_mission_V3.xlsx"
FICHIER_SORTIE = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION\LM EXCEL\extraction_lettres_mission_V4.xlsx"

# Dictionnaire des mois
MOIS = {
    'janvier': '01', 'février': '02', 'fevrier': '02', 'mars': '03',
    'avril': '04', 'mai': '05', 'juin': '06', 'juillet': '07',
    'août': '08', 'aout': '08', 'septembre': '09', 'octobre': '10',
    'novembre': '11', 'décembre': '12', 'decembre': '12'
}

def convertir_date(date_val):
    """Convertit une date en format JJ/MM/AAAA."""
    if pd.isna(date_val):
        return "Non trouvé"

    date_str = str(date_val).replace('\n', ' ').replace('\r', ' ').strip()

    if "Non trouvé" in date_str or date_str == "" or date_str == "nan":
        return "Non trouvé"

    # Format datetime: "2013-11-05 00:00:00" -> "05/11/2013"
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})\s+\d{2}:\d{2}:\d{2}$', date_str)
    if match:
        annee = match.group(1)
        mois = match.group(2)
        jour = match.group(3)
        return f"{jour}/{mois}/{annee}"

    # Format datetime sans heure: "2013-11-05"
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_str)
    if match:
        annee = match.group(1)
        mois = match.group(2)
        jour = match.group(3)
        return f"{jour}/{mois}/{annee}"

    # Format JJ/MM/AAAA ou JJ-MM-AAAA ou JJ.MM.AAAA
    match = re.match(r'^(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{4})$', date_str)
    if match:
        jour = match.group(1).zfill(2)
        mois = match.group(2).zfill(2)
        annee = match.group(3)
        return f"{jour}/{mois}/{annee}"

    # Format texte: "1er juillet 2019" ou "15 mars 2023" ou "31 décembre 2014"
    match = re.match(r'^(\d{1,2})(?:er|ère|ere|ème|eme)?\s+([a-zéûôè]+)\s+(\d{4})$', date_str.lower())
    if match:
        jour = match.group(1).zfill(2)
        mois_texte = match.group(2)
        annee = match.group(3)
        if mois_texte in MOIS:
            mois = MOIS[mois_texte]
            return f"{jour}/{mois}/{annee}"

    # Si on ne peut pas convertir, retourner tel quel
    return date_str


def main():
    print(f"Lecture de: {FICHIER_ENTREE}")

    df = pd.read_excel(FICHIER_ENTREE)

    print(f"Nombre de lignes avant: {len(df)}")

    col_debut = 'Debut Exercice'
    col_fin = 'Fin Exercice'

    # Convertir en string
    df[col_debut] = df[col_debut].astype(str)
    df[col_fin] = df[col_fin].astype(str)

    # Supprimer les lignes avec "Non trouvé"
    lignes_avant = len(df)

    mask = ~(df[col_debut].str.contains('Non trouvé', na=False) |
             df[col_fin].str.contains('Non trouvé', na=False))

    df_clean = df[mask].copy()

    lignes_supprimees = lignes_avant - len(df_clean)
    print(f"Lignes supprimées (Non trouvé): {lignes_supprimees}")

    # Convertir les dates au format JJ/MM/AAAA
    df_clean[col_debut] = df_clean[col_debut].apply(convertir_date)
    df_clean[col_fin] = df_clean[col_fin].apply(convertir_date)

    # Sauvegarder
    df_clean.to_excel(FICHIER_SORTIE, index=False)

    print(f"\n{'='*50}")
    print(f"TERMINE!")
    print(f"  - Lignes supprimées: {lignes_supprimees}")
    print(f"  - Lignes gardées: {len(df_clean)}")
    print(f"  - Fichier: {FICHIER_SORTIE}")


if __name__ == "__main__":
    main()
