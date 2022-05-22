from Game import Game
from Pack import Deck


# Fonction utilitaire pour les exercices 1, 2 & 3
def create_deck():
    print("\nCreating a new deck...\n")

    # Génère un nouveau paquet de cartes trié
    deck = Deck()

    # Affiche la représentation du paquet
    print(deck)

    return deck


def exercice_1():
    """
    Exercice 1: Mélanger un paquet de cartes
    """
    deck = create_deck()
    print("Shuffling the deck...\n")

    # Mélange le paquet <Pack/__init__.py ligne 42>
    deck.shuffle()  # <-- TODO implement this method

    # Affiche la représentation du paquet mélangé
    print(deck)


def exercice_2():
    """
    Exercice 2: Couper un paquet de cartes
    """
    deck = create_deck()
    print("Cutting the deck...\n")

    # Coupe le paquet <Pack/__init__.py ligne 49>
    deck.cut()  # <-- TODO implement this method

    # Affiche la représentation du nouveau paquet
    print(deck)


def exercice_3():
    """
    Exercice 3: Piocher une carte dans un paquet
    """
    deck = create_deck()
    print("Drawing a card...")

    # Pioche une carte <Pack/__init__.py ligne 56>
    card = deck.draw()  # <-- TODO implement this method
    print(f'Drawed card is "{card.name}"\n')

    # Vérifie si la carte piochée est toujours dans la paquet
    print(f'Is "{card.name}" still in deck ?')
    print(f"> {card.name in [card.name for card in deck.cards]}")


def exercice_4():
    """
    Exercice 4: Distribuer cinq cartes à chaque joueur
    """
    print("Game 1: Two players")
    # Only two players
    game = Game(nb_players=2)
    game.start()
    game.print_players_hands()

    print("\nGame 2: Five players")
    # What about 5 players ?
    game = Game(nb_players=5)
    game.start()
    game.print_players_hands()


def main():
    """
    EXERCICES:
    1. Mélanger les cartes
    2. Couper les cartes
    3. Distribuer les cartes
    """
    # exercice_1()
    # exercice_2()
    # exercice_3()
    exercice_4()


if __name__ == "__main__":
    main()
