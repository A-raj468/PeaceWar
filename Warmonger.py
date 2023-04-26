from Random import Random

class Warmonger(Random):
    """Represents a player which plays according to the "warmonger" strategy in the "Peace-War Game" \n
    A warmonger always chooses WAR over PEACE
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

    def move(self) -> str:
        """Select a move based on the "warmonger" strategy

        :return: A move chosen based on the "warmonger" strategy
        :rtype: str
        """
        return "WAR"