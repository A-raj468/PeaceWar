from Random import Random

class Pacifist(Random):
    """Represents a player which plays according to the "pacifist" strategy in the "Peace-War Game" \n
    A pacifist always chooses PEACE over WAR
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

    def move(self) -> str:
        """Select a move based on the "pacifist" strategy

        :return: A move chosen based on the "pacifist" strategy
        :rtype: str
        """
        return "PEACE"
