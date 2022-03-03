# Decision Tree Player

This project consists of a tic-tac-toe decision tree player. After the tree is created, the minimax decision rule is used to pick the best leaf. In order to correctly estimate the minimax indexes, a breadth first search (BFS), bottom up, is performed.

## Results

When the decision tree player (DTP) was facing a dummy-player (DP, random moves, purely stochastic), it got the following results:

- ~98% win rate when playing first;
- ~80% win rate when playing second;
- 0% loss rate.

As expected, it does not lose. Either DP blunders and the game is won by DTP, or he does not and the game ends in a draw.

For the results above, DTP was calculating 6 moves ahead (his next move, +5 moves) for every position. When calculating only 5 moves ahead (or less), he would lose some games, specially if DP was the first to play (~10% for 5 moves ahead).

Consider the following initial position:

| &nbsp; | &nbsp; | &nbsp; |
| :----: | :----: | :----: |
| &nbsp; | **X**  | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |

If the player with the `O` pieces does not play in one of the 4 corners, he will, for example, lose to the following position:

| **X**  | **X** | **O** |
| :----: | :---: | :---: |
| **O**  | **X** |
| &nbsp; | **X** | **O** |

This variation is forced, and explains the 6 moves that the DTP needs to calculate in order not to lose. There are other positions that lead to the same result.
