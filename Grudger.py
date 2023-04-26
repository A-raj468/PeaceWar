from Random import Random

class Grudger(Random):
    """Represents a player which plays according to the "grudger" strategy in the "Peace-War Game" \n
    A grudger starts of with PEACE but if the opponent plays WAR even once it will hold a grudge and always play WAR after that
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

    def updatePrevMove(self, opponentMove: str):
        if self.oppPrevMove == "PEACE":
            self.oppPrevMove = opponentMove

    def move(self) -> str:
        """Select a move based on the "grudger" strategy

        :return: A move chosen based on the "tit-for-tat" strategy
        :rtype: str
        """
        return self.oppPrevMove
