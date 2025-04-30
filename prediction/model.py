"""
Module de prédiction des dépenses.

Ce module contient les fonctions nécessaires pour entraîner un modèle
de régression linéaire et prédire les dépenses totales à partir des
catégories de dépenses.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def entrainer_et_predire():
    """
    Entraîne un modèle de régression linéaire sur les données de dépenses
    et effectue une prédiction d'exemple.

    Cette fonction:
    1. Charge les données depuis le fichier CSV
    2. Sépare les caractéristiques (X) et la cible (y)
    3. Divise les données en ensembles d'entraînement et de test
    4. Entraîne un modèle de régression linéaire
    5. Évalue la performance du modèle
    6. Effectue une prédiction sur un exemple
    """
    # Chargement des données
    print("Chargement des données de dépenses...")
    df = pd.read_csv("data/depenses.csv")

    # Préparation des caractéristiques (X) et de la cible (y)
    # X contient les variables explicatives (alimentation, transport, loisirs)
    X = df[["alimentation", "transport", "loisirs"]]
    # y contient la variable à prédire (total)
    y = df["total"]

    # Division des données en ensembles d'entraînement et de test
    # train_test_split permet de créer un ensemble pour entraîner le modèle
    # et un ensemble indépendant pour évaluer ses performances
    # test_size=0.2 signifie que 20% des données sont réservées pour le test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print(f"Données divisées en {len(X_train)} exemples d'entraînement et {len(X_test)} exemples de test")

    # Création et entraînement du modèle
    print("Entraînement du modèle de régression linéaire...")
    model = LinearRegression()
    # La méthode fit() entraîne le modèle sur les données
    model.fit(X_train, y_train)

    # Évaluation de la performance du modèle
    # score() retourne le coefficient de détermination R²
    # qui indique la proportion de la variance de y expliquée par le modèle
    score = model.score(X_test, y_test)
    # Affichage du score sous forme de pourcentage
    print("Précision du modèle :", round(score * 100, 2), "%")

    # Exemple de prédiction
    # Supposons que nous voulons prédire le total pour:
    # alimentation = 210€, transport = 105€, loisirs = 130€
    new_data = [[210, 105, 130]]
    # La méthode predict() utilise le modèle entraîné pour faire une prédiction
    prediction = model.predict(new_data)
    print("Dépenses prévues :", round(prediction[0], 2), "€")

    # Analyse des coefficients du modèle
    print("\nCoefficients du modèle :")
    for categorie, coefficient in zip(['Alimentation', 'Transport', 'Loisirs'], model.coef_):
        print(f"- {categorie} : {coefficient:.4f}")
    print(f"- Constante (intercept) : {model.intercept_:.4f}")

    return model


# Si ce fichier est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    print("Test du module de prédiction")
    entrainer_et_predire()