import argparse
import logging

from dumble.game import Game
from dumble.logging import LOGGING_LEVEL_LIST
from dumble.logging.configuration import ConfigureLogger


def exercice_1():
    """
    Exercice 1: Compter le nombre de points en main
    """
    print("\n-=== Exercice 1: Count current players points ===-")

    # Démarre une partie
    game = Game(nb_players=2)
    game.start()

    # Affiche les cartes en main de chaque joueur et leur nombre de points
    game.print_players_hands()
    # Calculer le nombre de points <dumble/game/game.py ligne 31>


def exercice_2():
    """
    Exercice 2: Trier les cartes de chaque joueur
    """
    print("\n-=== Exercice 2: Sort players hand ===-")
    game = Game(nb_players=3)
    game.start()

    # Affiche les cartes en main de chaque joueur et leur nombre de points
    game.print_players_hands()
    # Trier les cartes <dumble/game/game.py ligne 27>


def main():
    """
    EXERCICES:
    1. Compter le nombre de points en main
    2. Trier les cartes de chaque joueur
    """
    exercice_1()
    exercice_2()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play Dumble or simulate games.")
    parser.add_argument(
        "--log",
        type=str.upper,
        help='choose logging level (default is "INFO")',
        choices=LOGGING_LEVEL_LIST,
        default="INFO",
    )
    args = parser.parse_args()

    # Create logger at the correct level
    ConfigureLogger(console_level=args.log)
    logger = logging.getLogger("dumblog")

    main()
