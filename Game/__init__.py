from Pack import Deck


class Player:
    """
    This is a player.
    """

    def __init__(self):
        self.cards = []

    def get_player_hand(self):
        return " - ".join(map(lambda x: getattr(x, "name"), self.cards))


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
        self.deck.shuffle()
        self.deck.cut()
        self.deal()

    # Exercice 4
    def deal(self):  # <-- TODO Implement this method
        """
        Deal 5 cards to each player.
        """
        for _ in range(5):
            for player in self.players:
                player.cards.append(self.deck.draw())

    def print_players_hands(self):
        for player in self.players:
            print(f"Player {self.players.index(player)}: [{player.get_player_hand()}]")
