import random

MoveList = ["PEACE", "WAR"]    
class Random:
    """Reprsents a player which plays "randomly" in the "Peace-War Game"
    """
    def __init__(self):
        """Constructor
        """
        self.oppPrevMove = "PEACE"
        self.score = 0

    def updatePrevMove(self, opponentMove:str):
        """Updates previous move in memory

        :param opponentMove: Opponent's current move
        :type opponentMove: str
        """
        self.oppPrevMove = opponentMove

    def move(self) -> str:
        """Select a move randomly

        :return: A move chosen randomly
        :rtype: str
        """
        return random.choice(MoveList)

    def increase_score(self, amount:int):
        """Increases score of the player

        :param amount: amount by which to increase the score
        :type amount: int
        """
        self.score = self.score + amount