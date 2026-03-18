import pandas as pd

ANCIEN_FICHIER = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION\LM EXCEL\extraction_lettres_mission_V4.xlsx"
NOUVEAU_FICHIER = r"C:\Users\henri\Desktop\extraction_nouveau_dossier_FINAL.xlsx"
FICHIER_SORTIE = r"C:\Users\henri\Desktop\COURS 2025\STAGE CECCA\MISSION\LETTRE DE MISSION\LM EXCEL\extraction_lettres_mission_V5.xlsx"

print("Lecture des fichiers...")
df_ancien = pd.read_excel(ANCIEN_FICHIER)
df_nouveau = pd.read_excel(NOUVEAU_FICHIER)

print(f"  - Ancien fichier: {len(df_ancien)} lignes")
print(f"  - Nouveau fichier: {len(df_nouveau)} lignes")

# Fusionner les deux DataFrames
df_final = pd.concat([df_ancien, df_nouveau], ignore_index=True)

print(f"  - Total après fusion: {len(df_final)} lignes")

# Sauvegarder
df_final.to_excel(FICHIER_SORTIE, index=False)

print(f"\n{'='*50}")
print(f"TERMINE!")
print(f"  - Fichier: {FICHIER_SORTIE}")
