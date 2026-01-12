# Mini projet Data Science
# Objectif : découvrir et analyser un dataset simple avec Python

import pandas as pd

# Exemple : charger un dataset CSV
df = pd.read_csv('dataset.csv')  # remplace 'dataset.csv' par ton fichier

# Afficher les 5 premières lignes
print(df.head())

# Afficher des informations sur le dataset
print(df.info())
print(df.describe())
