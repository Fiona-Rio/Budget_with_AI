"""
Module d'initialisation de la base de données.

Ce module contient les fonctions nécessaires pour créer et initialiser
la base de données SQLite à partir des données CSV.
"""

import sqlite3
import pandas as pd


def creer_db():
    """
    Crée et initialise la base de données à partir du fichier CSV.

    Cette fonction:
    1. Charge les données depuis le fichier CSV
    2. Transforme les données du format large au format long
    3. Crée une base de données SQLite
    4. Insère les données transformées dans la base
    """
    print("Initialisation de la base de données...")

    # Chargement du fichier CSV
    print("Chargement des données depuis le fichier CSV...")
    df = pd.read_csv("data/depenses.csv")

    # Affichage des données chargées
    print("\nDonnées chargées (format original):")
    print(df.head())  # Affiche les 5 premières lignes

    # Transformation : passage du format large au format long
    # Le format large: une ligne par mois, une colonne par catégorie
    # Le format long: une ligne par combinaison mois-catégorie
    print("\nTransformation des données en format long...")

    # La méthode melt() "déplie" les données
    # Paramètres:
    # - id_vars: colonnes à conserver telles quelles
    # - value_vars: colonnes à transformer en paires clé-valeur
    # - var_name: nom de la colonne qui contiendra les noms des anciennes colonnes
    # - value_name: nom de la colonne qui contiendra les valeurs
    df_long = df.melt(
        id_vars=["mois"],  # colonne fixe
        value_vars=["alimentation", "transport", "loisirs"],  # colonnes à "déplier"
        var_name="categorie",  # nouvelle colonne pour les noms des catégories
        value_name="montant"  # nouvelle colonne pour les montants
    )

    # Affichage des données transformées
    print("\nDonnées transformées (format long):")
    print(df_long.head())

    # Connexion à SQLite
    # Création ou connexion à la base de données
    print("\nConnexion à la base de données SQLite...")
    conn = sqlite3.connect("db/budget.db")

    # Insérer dans la base dans la table 'depenses'
    # to_sql() convertit un DataFrame en table SQL
    # Paramètres:
    # - "depenses": nom de la table à créer
    # - conn: connexion à la base de données
    # - if_exists: que faire si la table existe déjà (ici, la remplacer)
    # - index: faut-il inclure l'index du DataFrame comme colonne (ici, non)
    print("Insertion des données dans la table 'depenses'...")
    df_long.to_sql("depenses", conn, if_exists="replace", index=False)

    # Création d'une deuxième table 'depenses_par_mois' pour conserver le format original
    print("Création de la table 'depenses_par_mois'...")
    df.to_sql("depenses_par_mois", conn, if_exists="replace", index=False)

    # Vérification de l'insertion
    cursor = conn.cursor()

    # Compter le nombre de lignes dans la table 'depenses'
    cursor.execute("SELECT COUNT(*) FROM depenses")
    nb_lignes = cursor.fetchone()[0]
    print(f"Nombre de lignes dans la table 'depenses': {nb_lignes}")

    # Compter le nombre de lignes dans la table 'depenses_par_mois'
    cursor.execute("SELECT COUNT(*) FROM depenses_par_mois")
    nb_lignes_par_mois = cursor.fetchone()[0]
    print(f"Nombre de lignes dans la table 'depenses_par_mois': {nb_lignes_par_mois}")

    # Fermeture de la connexion
    conn.close()
    print("Base de données initialisée avec succès!")


# Si ce fichier est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    creer_db()