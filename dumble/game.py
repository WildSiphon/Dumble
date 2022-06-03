import logging

from dumble.pack import Deck

logger = logging.getLogger("dumblog")


class Player:
    """
    This is a player.
    """

    def __init__(self, name):
        self.name = str(name)
        self.cards = []

    def get_hand_id(self):
        return "|".join(map(repr, self.cards))

    def get_hand_str(self):
        return " - ".join(map(str, self.cards))

    def draw(self, card):
        self.cards.append(card)
        self.sort_cards()

    # Exercice 2
    def sort_cards(self):  # <-- TODO Implement this method
        pass

    # Exercice 1
    @property
    def points(self) -> int:  # <-- TODO Implement this method
        return 1000

    # Change player's hand display by (un)commenting code below
    def __repr__(self):

        # Use cards names
        # return self.get_hand_str()

        # Use cards ids
        return self.get_hand_id()


class Game:
    """
    Main class which process the game.
    """

    def __init__(self, nb_players: int = 2):
        # List of players playing dumble
        self.players = [Player(index) for index in range(nb_players)]

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

    def deal(self):
        """
        Deal 5 cards to each player.
        """
        NB_CARDS = 5

        for _ in range(NB_CARDS):
            for player in self.players:
                card = self.deck.draw()
                player.draw(card)
                logger.debug(f"{card.id} dealt to player {player.name}")
        logger.info(f"Dealt {NB_CARDS} cards to each player.")

    def print_players_hands(self):
        for player in self.players:
            print(f"Player {player.name} ({player.points} points): |{player}|")
