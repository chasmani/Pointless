# Pointless
Game theory applications to BBC's Pointless

**die.py**
Models a 6 sided die and records the numebr of occurences of each result when rolled a changeable number of times.

**pointless.py**
Models the number fo new teams on each episode of the show Pointless. 
Teams have 2 chances to win, so can appear in 2 concurrent shows. 
Teams that win ar replace by a new team.
Teams that fail to win after 2 appearances are replaced by a new team. 

The number fo new teams each episode can be represented as a Markov process.  

It is possible for the number fo new teams to be between 1 and 4.  

This program models the process of teams appearing on the sshow by considering a random winner of each show. 
This gives a numerical result for the percentage chance of each possible number of teams. 

Running the simulation over 10,000,000 shows gives numerical percentages of: 

1 new team   -  0.11%
2 new teams  -  0.51%
3 new teams  -  0.34%
4 new teams  -  0.29%

**Further work**
It would be interesting to build the same model and predict the percentages mathematically. 