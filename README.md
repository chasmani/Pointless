# Pointless
Game theory applications to BBC's Pointless, in particular modelling the number of new teams each epsiode as a Markov process. Truly a pointless endeavour. 

**die.py**
Models a 6 sided die and records the number of occurences of each result when rolled a changeable number of times. This predicatble model was used to develop and test the recording of statistics, for use in the more complex pointless model.

**pointless.py**
Models the number of new teams on each episode of the show Pointless. 

*Considers the following rules:*
- There are 4 teams on each show.
- Teams have 2 chances to win, so can appear in 2 concurrent shows. 
- Teams that win are replaced by a new team.
- Teams that fail to win after 2 appearances are replaced by a new team. 

It is possible for the number of new teams on a show to be between 1 and 4 inclusive, and each state is (eventually) reachable from every other state.

This program models the process of teams appearing on the show by considering a random winner of each show. 
This gives a numerical result for the percentage chance of each possible number of teams. 

Running the simulation over 10,000,000 shows gives numerical ratios of: 

1 new team   -  0.11
2 new teams  -  0.51
3 new teams  -  0.34
4 new teams  -  0.29

**Further work**
It would be interesting to build the same model and predict the percentages mathematically.
It would be interesting to compare this result with actual empirical data.
