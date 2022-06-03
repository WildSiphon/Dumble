from random import randint, shuffle

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
    def shuffle(self):
        """
        Shuffle the deck.
        """
        shuffle(self.cards)

    # Exercice 2
    def cut(self, cut_id: int = None):
        """
        Cut the deck.
        """
        deck_range = (0, self.size)

        # TODO log this
        if (cut_id is None) or (cut_id not in range(*deck_range)):
            cut_id = randint(*deck_range)

        self.cards = self.cards[cut_id:] + self.cards[:cut_id]

    # Exercice 3
    def draw(self) -> Card:
        """
        Draw a card.
        """
        # The card on top of the deck is the last one
        return self.cards.pop()

    @property
    def size(self) -> int:
        return len(self.cards)

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        """
        This function is the representation of the deck.
        """
        stats = f"The deck has {len(self.cards)} cards:\n"
        cards = "\n".join([f" - {card.name}" for card in self.cards])
        return stats + cards + "\n"
