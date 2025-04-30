"""
Programme principal du projet Budget IA.

Ce script coordonne l'exécution des différents modules du projet:
- Initialisation de la base de données
- Analyse statistique des dépenses
- Visualisation graphique
- Prédiction des dépenses futures

Il propose également une interface utilisateur simple en ligne de commande.
"""

import os
import sys
from db.init_db import creer_db
from analysis.stats import moyenne_depenses
from analysis.visualisation import afficher_graphiques
from prediction.model import entrainer_et_predire


def afficher_menu():
    """Affiche le menu principal du programme."""
    print("\n" + "=" * 50)
    print("BUDGET IA - ANALYSE INTELLIGENTE DE VOS DÉPENSES")
    print("=" * 50)

    print("\nQue souhaitez-vous faire ?")
    print("1. Initialiser/réinitialiser la base de données")
    print("2. Analyser les statistiques des dépenses")
    print("3. Visualiser les dépenses avec des graphiques")
    print("4. Prédire les dépenses futures")
    print("5. Exécuter tout le pipeline d'analyse")
    print("0. Quitter")

    choix = input("\nVotre choix (0-5) : ")
    return choix


def executer_avec_gestion_erreurs(fonction, message_succes):
    """
    Exécute une fonction avec gestion des erreurs.

    Args:
        fonction: La fonction à exécuter
        message_succes: Message à afficher en cas de succès
    """
    try:
        print("=" * 50)
        resultat = fonction()
        print("=" * 50)
        print(message_succes)
        return resultat
    except Exception as e:
        print("=" * 50)
        print(f"ERREUR: {str(e)}")
        print("Veuillez vérifier vos fichiers et réessayer.")
        return None


def verifier_fichiers():
    """Vérifie si les fichiers et dossiers nécessaires existent."""
    # Vérification du dossier data
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Dossier 'data' créé.")

    # Vérification du fichier CSV
    if not os.path.exists("data/depenses.csv"):
        print("ATTENTION: Le fichier 'data/depenses.csv' n'existe pas.")
        return False

    # Vérification du dossier db
    if not os.path.exists("db"):
        os.makedirs("db")
        print("Dossier 'db' créé.")

    return True


def interface_cli():
    """Interface utilisateur en ligne de commande."""
    while True:
        choix = afficher_menu()

        if choix == "0":
            print("\nMerci d'avoir utilisé Budget IA. À bientôt!")
            break

        elif choix == "1":
            executer_avec_gestion_erreurs(
                creer_db,
                "Base de données initialisée avec succès."
            )

        elif choix == "2":
            executer_avec_gestion_erreurs(
                moyenne_depenses,
                "Analyse statistique des dépenses terminée."
            )

        elif choix == "3":
            executer_avec_gestion_erreurs(
                afficher_graphiques,
                "Visualisation des dépenses terminée."
            )

        elif choix == "4":
            model = executer_avec_gestion_erreurs(
                entrainer_et_predire,
                "Prédiction des dépenses terminée."
            )

            if model is not None:
                print("\nVoulez-vous essayer une prédiction personnalisée ? (o/n)")
                if input().lower() == "o":
                    try:
                        # Récupération des entrées utilisateur
                        alim = float(input("Dépenses alimentation (€) : "))
                        trans = float(input("Dépenses transport (€) : "))
                        loisirs = float(input("Dépenses loisirs (€) : "))

                        # Prédiction
                        prediction = model.predict([[alim, trans, loisirs]])
                        print(f"\nTotal prédit : {prediction[0]:.2f} €")

                    except ValueError:
                        print("Erreur : veuillez entrer des nombres valides.")

        elif choix == "5":
            print("\nExécution du pipeline d'analyse complet...")

            # Vérification des fichiers nécessaires
            if not verifier_fichiers():
                print("Impossible d'exécuter le pipeline complet.")
                continue

            # Exécution séquentielle des modules
            executer_avec_gestion_erreurs(creer_db, "Étape 1: Base de données initialisée.")
            executer_avec_gestion_erreurs(moyenne_depenses, "Étape 2: Analyse statistique terminée.")
            executer_avec_gestion_erreurs(afficher_graphiques, "Étape 3: Visualisation terminée.")
            executer_avec_gestion_erreurs(entrainer_et_predire, "Étape 4: Prédiction terminée.")

            print("\nPipeline d'analyse complet exécuté avec succès!")

        else:
            print("Choix non valide. Veuillez entrer un nombre entre 0 et 5.")


if __name__ == "__main__":
    print("Démarrage du programme Budget IA...")

    # Vérification initiale des fichiers
    verifier_fichiers()

    # Lancement de l'interface utilisateur
    interface_cli()