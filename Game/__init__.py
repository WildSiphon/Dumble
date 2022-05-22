from Pack import Deck


class Player:
    """
    This is a player.
    """

    def __init__(self):
        self.cards = []

    def get_player_hand(self):
        return " - ".join(self.cards)


class Game:
    """
    Main class which process the game.
    """

    def __init__(self, nb_players: int = 2):
        # List of players playing dumble
        self.players = [Player() for _ in range(nb_players)]

        # The deck of cards
        self.deck = Deck()

    def start(self):
        """
        Start the game by initializing the deck and the player's hands.
        """
        self.deck.generate()
        self.deck.shuffle()  # This method was implemented during Exercice 1
        self.deck.cut()  # This method was implemented during Exercice 2
        self.deal()  # You need to implement this method for Exercice 4

    # Exercice 4
    def deal(self):  # <-- TODO Implement this method
        """
        Deal 5 cards to each player.
        """
        pass

    def print_players_hands(self):
        for player in self.players:
            print(
                f"Player {self.players.index(player)}: " f"[{player.get_player_hand()}]"
            )
