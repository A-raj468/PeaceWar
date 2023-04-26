#       |PEACE| WAR |
# PEACE | 3,3 | 0,4 |
# WAR   | 4,0 | 1,1 |

points = {
    ("PEACE", "PEACE"):(3,3),
    ("PEACE", "WAR"):(0,4),
    ("WAR", "PEACE"):(4,0),
    ("WAR", "WAR"):(1,1)
}

PRINT_INFO = 0

from Random import Random
from Pacifist import Pacifist
from Warmonger import Warmonger
from TitForTat import TitForTat
from Grudger import Grudger
from ForgivingTitForTat import ForgivingTitForTat
from Joss import Joss

from User import User

from random import choice
players = [Random, Pacifist, Warmonger, TitForTat, Grudger, ForgivingTitForTat, Joss]
n = 100*2
# players.append(User)
# n = int(input("Enter number of rounds: "))

total_scores = {x.__name__ : [0,0] for x in players}
k = 1000*10

for t in range(k):
    player0 = choice(players)()
    player1 = choice(players)()


    for i in range(n):
        move0 = player0.move()
        move1 = player1.move()
        player0.updatePrevMove(move1)
        player1.updatePrevMove(move0)

        score = points[(move0, move1)]

        if(PRINT_INFO):
            print(f"Player 1 chose {move0}")
            print(f"Player 2 chose {move1}")
            print(f"Scores this round: {score}")

        player0.increase_score(score[0])
        player1.increase_score(score[1])

    p0Name = type(player0).__name__
    p1Name = type(player1).__name__

    if PRINT_INFO:
        print("Player | Score")
        print(f"{p0Name} | {player0.score}")
        print(f"{p1Name} | {player1.score}")

    total_scores[p0Name][0] = total_scores[p0Name][0] + player0.score
    total_scores[p1Name][0] = total_scores[p1Name][0] + player1.score

    total_scores[p0Name][1] = total_scores[p0Name][1] + 1
    total_scores[p1Name][1] = total_scores[p1Name][1] + 1

if PRINT_INFO:
    print(total_scores)

avg_score = {name : score[0] / score[1] for name, score in total_scores.items()}

avg_score = dict(sorted(avg_score.items(), key= lambda x : x[1]))

print(f"Strategy: AvgScore")
for name, score in avg_score.items():
    print(f"{name}: {score}")