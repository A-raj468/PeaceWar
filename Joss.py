from Random import Random
import random

p=0.01
class Joss(Random):
    """Represents a player which plays according to the "joss" strategy in the "Peace-War Game" \n
    A tit-for-tat player starts off with PEACE but if the opponent plays WAR it will punish the opponent in next round by playing WAR \n
    Similarly, it will cooperate with the opponent if it plays PEACE by playing PEACE next turn \n
    But, it has a tendency to play WAR even when the opponent played PEACE previously, although with a small probability
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
        if self.oppPrevMove == "PEACE":
            return "WAR" if random.random() < p else "PEACE"
        return self.oppPrevMove
