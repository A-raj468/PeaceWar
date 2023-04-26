from Random import Random

class User(Random):
    """Represents a player which plays according to the user input in the "Peace-War Game" \n
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

    def move(self) -> str:
        """Select a move based on the user input

        :return: A move chosen by the user
        :rtype: str
        """
        print("0) PEACE")
        print("1) WAR")
        myMove = int(input("Choose your move(0/1): "))
        while(myMove != 0 and myMove != 1):
            myMove = int(input("Please enter a valid move(0/1): "))
        return "PEACE" if myMove == 0 else "WAR"
