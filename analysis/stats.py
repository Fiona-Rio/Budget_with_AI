"""
Module d'analyse statistique des dépenses.

Ce module contient les fonctions nécessaires pour calculer des statistiques
sur les données de dépenses stockées dans la base de données SQLite.
"""

import sqlite3


def moyenne_depenses():
    """
    Calcule et affiche la moyenne des dépenses totales.

    Cette fonction:
    1. Se connecte à la base de données SQLite
    2. Exécute une requête SQL pour calculer la moyenne des dépenses
    3. Affiche le résultat
    4. Ferme la connexion à la base de données
    """
    # Établissement de la connexion à la base de données
    # sqlite3.connect() ouvre une connexion à une base de données SQLite
    # Si la base n'existe pas, elle sera créée
    print("Connexion à la base de données...")
    conn = sqlite3.connect("db/budget.db")

    # Création d'un curseur pour exécuter des requêtes SQL
    # Un curseur est un objet qui permet d'interagir avec la base de données
    cursor = conn.cursor()

    # Exécution d'une requête SQL
    # Cette requête calcule la moyenne (AVG) des valeurs de la colonne 'total'
    # dans la table 'depenses'
    print("Calcul de la moyenne des dépenses...")
    cursor.execute("SELECT AVG(total) FROM depenses")

    # Récupération du résultat
    # fetchone() récupère une seule ligne de résultat (ici, juste la moyenne)
    # [0] extrait la première (et seule) valeur de cette ligne
    moyenne = cursor.fetchone()[0]
    print("Dépenses moyennes :", moyenne, "€")

    # Récupération de statistiques supplémentaires
    print("Calcul d'autres statistiques...")

    # Minimum des dépenses
    cursor.execute("SELECT MIN(total) FROM depenses")
    minimum = cursor.fetchone()[0]
    print("Dépenses minimales :", minimum, "€")

    # Maximum des dépenses
    cursor.execute("SELECT MAX(total) FROM depenses")
    maximum = cursor.fetchone()[0]
    print("Dépenses maximales :", maximum, "€")

    # Somme totale des dépenses
    cursor.execute("SELECT SUM(total) FROM depenses")
    somme = cursor.fetchone()[0]
    print("Somme totale des dépenses :", somme, "€")

    # Nombre de mois enregistrés
    cursor.execute("SELECT COUNT(*) FROM depenses")
    nb_mois = cursor.fetchone()[0]
    print("Nombre de mois enregistrés :", nb_mois)

    # Fermeture de la connexion à la base de données
    # C'est une bonne pratique de fermer la connexion après utilisation
    conn.close()
    print("Connexion à la base de données fermée")

    return moyenne


# Si ce fichier est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    print("Test du module de statistiques")
    moyenne_depenses()