from Rules import Colors, Rules


class Card:
    """
    Simple card.
    """

    def __init__(self, rank, suit: str, color: Colors):
        self.rank = str(rank)
        self.suit = suit
        self.color = color

        self.value = rank if isinstance(rank, int) else 10

    @property
    def name(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    The undealt portion of the pack which will be used in the game.
    Before dealing, a deck is the whole pack of cards.
    """

    def __init__(self, pack: int = 52):
        self.pack = pack

        self.rules = Rules()

        self.cards = []
        self.generate()

    def generate(self):
        """
        (Re)Generate a pack of cards following the game's rules
        """
        for suit in self.rules.suits:
            for rank in self.rules.ranks:
                self.cards.append(Card(rank, suit[0], suit[1]))

    # Exercice 1
    def shuffle(self):  # <-- TODO Implement this method
        """
        Shuffle the deck.
        """
        pass

    # Exercice 2
    def cut(self):  # <-- TODO Implement this method
        """
        Cut the deck.
        """
        pass

    # Exercice 3
    def draw(self) -> Card:  # <-- TODO Implement this method
        """
        Draw a card.
        """
        return Card("Ace", "spades", Colors.BLACK)

    def __repr__(self):
        """
        This function is the representation of the deck.
        """
        stats = f"The deck has {len(self.cards)} cards:\n"
        cards = "\n".join([f" - {card.name}" for card in self.cards])
        return stats + cards + "\n"
