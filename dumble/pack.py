import logging
from random import randint, shuffle

from dumble.rules import Colors, Rules

logger = logging.getLogger("dumblog")


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

    @property
    def id(self):
        return f"{self.rank[0].upper()}{self.suit[0].upper()}"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.id


class Deck:
    """
    The undealt portion of the pack which will be used in the game.
    Before dealing, a deck is the whole pack of cards.
    """

    def __init__(self, pack: int = 52):
        self.pack = pack

        self.rules = Rules()

        self.cards = []

    def generate(self):
        """(Re)Generate a pack of cards following the game's rules."""
        if self.cards:
            logger.debug("Current deck is not empty.")
            self.cards = []
            logger.debug("Current deck erased.")

        for suit in self.rules.suits:
            for rank in self.rules.ranks:
                self.cards.append(Card(rank, suit[0], suit[1]))

        logger.info(f"New {self.size} sorted cards deck generated.")

    def shuffle(self):
        """Shuffle the deck."""
        shuffle(self.cards)
        logger.info("Deck shuffled.")

    def cut(self, cut_id: int = None):
        """Cut the deck."""
        deck_range = (0, self.size)

        if (cut_id is None) or (cut_id not in range(*deck_range)):
            logger.debug(f'Cut index must be in range {deck_range}, not "{cut_id}".')
            cut_id = randint(*deck_range)
            logger.debug(f"Random index ({cut_id}) will be used instead.")

        self.cards = self.cards[cut_id:] + self.cards[:cut_id]
        logger.info(f"Deck cut at index {cut_id}.")

    def draw(self) -> Card:
        """Draw a card. The card on top of the deck is the last one."""
        return self.cards.pop()

    @property
    def size(self) -> int:
        """The size of the deck is the number of cards in it."""
        return len(self.cards)

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        stats = f"The deck has {len(self.cards)} cards:\n"
        cards = "\n".join([f" - {card.name}" for card in self.cards])
        return stats + cards + "\n"
