# PeaceWar

Simulates the game of Peace War, which is a variant of iterated prisoner's dilemma, for multiple strategies.

### Strategies

1. Random: Plays randomly
2. Pacifist: Always chooses peace
3. Warmonger: Always chooses war
4. TitForTat: Punishes opponent for chosing war in the next turn, otherwise choses peace
5. Grudger: Holds a grudge against player who plays war, after which it always plays war
6. ForgivingTitForTat: Same as TitForTat, but war can be overlooked as mistake with a small probability
7. Joss: Same as TitForTat, but has a tendency to cause war in times of peace
