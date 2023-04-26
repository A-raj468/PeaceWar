from Random import Random
import random

p = 0.01
class ForgivingTitForTat(Random):
    """Represents a player which plays according to a "forgiving tit-for-tat" strategy in the "Peace-War Game" \n
    A tit-for-tat player starts off with PEACE but if the opponent plays WAR it will punish the opponent in next round by playing WAR \n
    But, it can sometimes spare the opponent, although with a small probability
    Similarly, it will cooperate with the opponent if it plays PEACE by playing PEACE next turn
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

    def move(self) -> str:
        """Select a move based on the "tit-for-tat" strategy

        :return: A move chosen based on the "tit-for-tat" strategy
        :rtype: str
        """
        if self.oppPrevMove == "WAR":
            return "PEACE" if random.random() < p else "WAR"
        return self.oppPrevMove
