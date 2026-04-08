import csv
import re

FICHIER_ENTREE = r"C:\Users\henri\Desktop\extraction_lettres_mission.csv"
FICHIER_SORTIE = r"C:\Users\henri\Desktop\extraction_lettres_mission_clean.csv"

# Dictionnaire des mois
MOIS = {
    'janvier': '01', 'février': '02', 'fevrier': '02', 'mars': '03',
    'avril': '04', 'mai': '05', 'juin': '06', 'juillet': '07',
    'août': '08', 'aout': '08', 'septembre': '09', 'octobre': '10',
    'novembre': '11', 'décembre': '12', 'decembre': '12'
}

def convertir_date(date_str):
    """Convertit une date en format JJ/MM/AAAA."""
    if not date_str or date_str == "Non trouvé":
        return "Non trouvé"

    # Nettoyer les retours à la ligne
    date_str = date_str.replace('\n', ' ').replace('\r', ' ').strip()

    # Si déjà au bon format (JJ/MM/AAAA ou JJ-MM-AAAA ou JJ.MM.AAAA)
    match = re.match(r'^(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{4})$', date_str)
    if match:
        jour = match.group(1).zfill(2)
        mois = match.group(2).zfill(2)
        annee = match.group(3)
        return f"{jour}/{mois}/{annee}"

    # Format avec année sur 2 chiffres
    match = re.match(r'^(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{2})$', date_str)
    if match:
        jour = match.group(1).zfill(2)
        mois = match.group(2).zfill(2)
        annee = match.group(3)
        # Convertir en 4 chiffres (supposer 19xx si > 50, sinon 20xx)
        if int(annee) > 50:
            annee = "19" + annee
        else:
            annee = "20" + annee
        return f"{jour}/{mois}/{annee}"

    # Format texte: "1er janvier 2024" ou "15 mars 2023"
    match = re.match(r'^(\d{1,2})(?:er|ère|ere|ème|eme)?\s+([a-zéûô]+)\s+(\d{4})$', date_str.lower())
    if match:
        jour = match.group(1).zfill(2)
        mois_texte = match.group(2)
        annee = match.group(3)

        if mois_texte in MOIS:
            mois = MOIS[mois_texte]
            return f"{jour}/{mois}/{annee}"

    # Format avec espace dans la date (ex: "31 12 2024")
    match = re.match(r'^(\d{1,2})\s+(\d{1,2})\s+(\d{4})$', date_str)
    if match:
        jour = match.group(1).zfill(2)
        mois = match.group(2).zfill(2)
        annee = match.group(3)
        return f"{jour}/{mois}/{annee}"

    # Si on ne peut pas convertir, retourner tel quel
    return date_str


def main():
    lignes_gardees = []
    lignes_supprimees = 0

    print(f"Lecture de: {FICHIER_ENTREE}")

    with open(FICHIER_ENTREE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            debut = row.get('Debut Exercice', '').replace('\n', ' ').replace('\r', ' ').strip()
            fin = row.get('Fin Exercice', '').replace('\n', ' ').replace('\r', ' ').strip()

            # Supprimer si "Non trouvé" dans début OU fin
            if "Non trouvé" in debut or "Non trouvé" in fin:
                lignes_supprimees += 1
                print(f"  Supprimé: {row.get('Nom Client', '')[:40]} (debut={debut}, fin={fin})")
                continue

            # Convertir les dates au format JJ/MM/AAAA
            row['Debut Exercice'] = convertir_date(debut)
            row['Fin Exercice'] = convertir_date(fin)

            lignes_gardees.append(row)

    print(f"\nÉcriture de: {FICHIER_SORTIE}")

    with open(FICHIER_SORTIE, 'w', newline='', encoding='utf-8-sig') as f:
        colonnes = ['Nom Client', 'SIREN', 'Debut Exercice', 'Fin Exercice', 'Fichier', 'Chemin']
        writer = csv.DictWriter(f, fieldnames=colonnes, delimiter=';')
        writer.writeheader()

        for row in lignes_gardees:
            writer.writerow(row)

    print(f"\n{'='*50}")
    print(f"TERMINE!")
    print(f"  - Lignes supprimées: {lignes_supprimees}")
    print(f"  - Lignes gardées: {len(lignes_gardees)}")
    print(f"  - Fichier: {FICHIER_SORTIE}")


if __name__ == "__main__":
    main()
