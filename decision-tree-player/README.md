# Decision Tree Player

This project consists of a tic-tac-toe decision tree player (`DecisionTreePlayer`). In order to assess which move (branch) leads to the best position, the minimax decision rule is used. This rule states that a player should always make the best move possible, and that he should except his opponent to do the same.

When creating the decision tree, recursion was used for both leafs instantiation and for the estimation of the minimax index of each (parent) leaf. In order to correctly estimate minimax indexes, a breadth first search (BFS) bottom up is performed.

## Results

When `DecisionTreePlayer` was facing a `DummyPlayer` (random moves, purely stochastic), he got the following results:

* ~98% win rate when playing first;
* ~80% win rate when playing second.

As expected, he does not lose. Either `DummyPlayer` blunders and the game is won by `DecisionTreePlayer`, or he does not and the game ends in a draw. Worth noting that `DecisionTreePlayer` is deterministic. When there is more than one "optimal" move, he always picks the first one.

For the results above, `DecisionTreePlayer` was calculating 6 moves ahead (his next move, +5 moves) for every position. When calculating only 5 moves ahead (or less), he would lose some games, specially if `DummyPlayer` was the first to play (~10% for 5 moves ahead).

Consider the following initial position:

&nbsp; | &nbsp; | &nbsp;
 :---: | :---:  | :---:
&nbsp; | **X**  | &nbsp;
&nbsp; | &nbsp; | &nbsp;

If the player with the `O` pieces does not play in one of the 4 corners, he will lose to the following position for example:

**X** | **X** | **O**
:---: | :---: | :---:
**O** | **X** |
&nbsp;| **X** | **O**

This variation is forced, and explains the 6 moves that the `DecisionTreePlayer` needs to calculate in order not to lose. There are other positions that lead to the same result.
