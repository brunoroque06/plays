package com.github.brunoroque06.decisiontreeplayer.tree;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;
import java.util.List;

public class DecisionTree {
  private final NodeFactory nodeFactory;
  private Node root;

  public DecisionTree(final NodeFactory nodeFactory) {
    this.nodeFactory = nodeFactory;
  }

  public Square estimateBestMove(final Board board, final int depthToCalculate) {
    root = nodeFactory.instantiateRoot(board);
    generateLeaves(root, depthToCalculate - 1);

    return findBestMove();
  }

  private void generateLeaves(final Node parent, final int depth) {
    final List<Square> squares = parent.getPossibleMoves();

    for (final Square square : squares) {
      final Node newLeaf = instantiateLeaf(parent, square);

      if (isBranchComplete(depth, newLeaf)) {
        newLeaf.estimateMinimax(root.getState());
      } else {
        generateLeaves(newLeaf, depth - 1);
      }
    }
    parent.updateMinimax();
  }

  private Node instantiateLeaf(final Node parent, final Square squarePlayed) {
    final Board board = parent.cloneBoard();
    board.playPieceAndUpdateState(squarePlayed);

    return nodeFactory.instantiateNode(board, squarePlayed, parent);
  }

  private boolean isBranchComplete(final int depth, final Node node) {
    return depth == 0 || node.isGameWonOrDrawn();
  }

  private Square findBestMove() {
    return isBoardEmpty() ? new Square(1, 1) : findBestLeaf().getMove();
  }

  private boolean isBoardEmpty() {
    return root.isBoardEmpty();
  }

  private Node findBestLeaf() {
    return root.getBestLeaf();
  }
}
