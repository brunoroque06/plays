package com.github.brunoroque06.games.players;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Square;
import com.github.brunoroque06.games.tree.DecisionTree;

public class DecisionTreePlayer implements Player {
  private final DecisionTree decisionTree;
  private final int depthToCalculate;

  public DecisionTreePlayer(final DecisionTree decisionTree, final int depthToCalculate) {
    this.decisionTree = decisionTree;
    this.depthToCalculate = depthToCalculate;
  }

  @Override
  public Square chooseMove(final Board board) {
    return decisionTree.estimateBestMove(board, depthToCalculate);
  }
}
