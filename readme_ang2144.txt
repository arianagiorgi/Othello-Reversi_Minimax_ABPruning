Ariana Giorgi
ang2144
AI Project 2 - Othello Minimax/Alpha Beta Pruning
10/15/14

This engine is supplemental to set of files to accompany othello.py used for this assignment.

Both minimax and alpha beta pruning run in the default play time of 30 seconds at depth = 2 (defaulted in the program).
As a guide for the code, I found the minimax and alpha-beta pseudocode available from Wikipedia to be helpful:
Minimax: http://en.wikipedia.org/wiki/Minimax
Alpha-beta pruning: http://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

For the calculation of the heuristics, I referenced a paper published by the University of Washington, section 5.1:
http://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
In the paper, they discuss using coin parity, corners captured, mobility, and stability as a combination for the heuristi
c. In section 6.1 of the paper, they compare their evaluations of each heuristic independently.
I decided to incorporate all of the these aspects except stability. I figured calculating the stability for each piece on
 the board would waste too much time, especially since it seemed from the paper that stability and mobility had roughly t
he same influence on the number of coins won/lost.
In regards to the final value (the combination of the 3 heuristics), I weighted them simply as 3/2/1.. I wanted to priori
ze getting the corners more than anything, then mobility, then coin parity. For a future experiment, it would be interest
ing and perhaps more valuable to find the exact weights (on a scale of 0.0 to 1.0) for these heuristics.
However, for this project, the heuristic supplies enough information to successful beat the random and greedy agents cons
istently.