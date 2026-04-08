import pandas as pd

FICHIER = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION\LM EXCEL\extraction_lettres_mission_V3.xlsx"

df = pd.read_excel(FICHIER)

print("Colonnes:", list(df.columns))
print(f"\nNombre total de lignes: {len(df)}")

# Trouver les colonnes de dates
col_debut = None
col_fin = None

for col in df.columns:
    col_lower = str(col).lower()
    if 'debut' in col_lower or 'début' in col_lower:
        col_debut = col
    if 'fin' in col_lower:
        col_fin = col

print(f"\nColonne début: {col_debut}")
print(f"Colonne fin: {col_fin}")

# Compter les "Non trouvé"
df[col_debut] = df[col_debut].astype(str)
df[col_fin] = df[col_fin].astype(str)

non_trouve_debut = df[col_debut].str.contains('Non trouvé', na=False).sum()
non_trouve_fin = df[col_fin].str.contains('Non trouvé', na=False).sum()
non_trouve_total = (df[col_debut].str.contains('Non trouvé', na=False) | df[col_fin].str.contains('Non trouvé', na=False)).sum()

print(f"\nNon trouvé dans début: {non_trouve_debut}")
print(f"Non trouvé dans fin: {non_trouve_fin}")
print(f"Lignes avec au moins un 'Non trouvé': {non_trouve_total}")

# Afficher les premières valeurs pour voir le format
print(f"\n--- Exemples de dates début ---")
print(df[col_debut].head(20).tolist())

print(f"\n--- Exemples de dates fin ---")
print(df[col_fin].head(20).tolist())
