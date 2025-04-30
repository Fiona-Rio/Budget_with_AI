"""
Module de visualisation des dépenses.

Ce module contient les fonctions nécessaires pour créer des visualisations
graphiques des données de dépenses.
"""

import pandas as pd
import matplotlib.pyplot as plt


def afficher_graphiques():
    """
    Crée et affiche des graphiques pour visualiser les dépenses.

    Cette fonction:
    1. Charge les données depuis le fichier CSV
    2. Crée un graphique en barres des dépenses par catégorie et par mois
    3. Configure les titres, légendes et étiquettes
    4. Affiche le graphique
    """
    # Chargement des données
    print("Chargement des données pour visualisation...")
    df = pd.read_csv("data/depenses.csv")

    # Création du graphique en barres
    print("Création du graphique des dépenses mensuelles...")

    # La méthode plot() de pandas permet de créer facilement des graphiques
    # Paramètres:
    # - x="mois": utilise la colonne 'mois' pour l'axe des x
    # - y=[...]: liste des colonnes à représenter sur l'axe des y
    # - kind="bar": type de graphique (ici, un graphique en barres)
    df.plot(x="mois", y=["alimentation", "transport", "loisirs", "total"], kind="bar")

    # Configuration du graphique
    # Ajout d'un titre
    plt.title("Dépenses mensuelles")

    # Rotation des étiquettes de l'axe x pour une meilleure lisibilité
    # Sans cette rotation, les étiquettes peuvent se chevaucher
    plt.xticks(rotation=45)

    # Ajustement automatique de la mise en page pour éviter que des éléments
    # soient coupés ou se chevauchent
    plt.tight_layout()

    # Ajout d'une légende (créée automatiquement par pandas.plot)

    # Sauvegarde du graphique (optionnel)
    plt.savefig("depenses_mensuelles.png")
    print("Graphique sauvegardé sous 'depenses_mensuelles.png'")

    # Affichage du graphique
    # La fonction show() ouvre une fenêtre avec le graphique
    plt.show()

    # Création d'un deuxième graphique: répartition des dépenses (camembert)
    print("Création du graphique de répartition des dépenses...")

    # Calcul des totaux par catégorie
    totaux = [df['alimentation'].sum(), df['transport'].sum(), df['loisirs'].sum()]
    categories = ['Alimentation', 'Transport', 'Loisirs']

    # Création d'une nouvelle figure
    plt.figure(figsize=(8, 8))

    # Création du graphique circulaire
    plt.pie(totaux, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title('Répartition des dépenses par catégorie')
    plt.axis('equal')  # Égalisation des axes pour un cercle parfait

    # Sauvegarde et affichage
    plt.savefig("repartition_depenses.png")
    print("Graphique sauvegardé sous 'repartition_depenses.png'")
    plt.show()


# Si ce fichier est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    print("Test du module de visualisation")
    afficher_graphiques()