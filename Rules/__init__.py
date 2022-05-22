from enum import Enum, auto


class Colors(Enum):
    """
    Custom colors for the game.
    """

    RED = auto()
    BLACK = auto()


class Rules:
    """
    All rules that apply to the pack of cards.
    """

    def __init__(self, min_num: int = 2, max_num: int = 10):
        self.numerals = range(min_num, max_num + 1)
        self.courts = ["Jack", "Queen", "King", "Ace"]
        self.suits = {
            ("clubs", Colors.BLACK),
            ("spades", Colors.BLACK),
            ("hearts", Colors.RED),
            ("diamonds", Colors.RED),
        }

    @property
    def ranks(self):
        """
        A generator to iterate on the cards rank.
        """
        for numeral in self.numerals:
            yield numeral
        for court in self.courts:
            yield court
