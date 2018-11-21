package com.github.brunoroque06.decisiontreeplayer.tree;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;

public class DecisionTree {
  private final NodeFactory nodeFactory;
  private Node root;

  public DecisionTree(final NodeFactory nodeFactory) {
    this.nodeFactory = nodeFactory;
  }

  public Square estimateBestMove(final Board board, final int depth) {
    root = nodeFactory.instantiateRoot(board);
    generateLeaves(root, depth - 1);

    return findBestMove();
  }

  private void generateLeaves(final Node parent, final int depth) {
    final var squares = parent.getPossibleMoves();

    for (final Square square : squares) {
      final var newLeaf = instantiateLeaf(parent, square);

      if (isBranchComplete(depth, newLeaf)) {
        newLeaf.estimateMinimax(root.getState());
      } else {
        generateLeaves(newLeaf, depth - 1);
      }
    }
    parent.updateMinimax();
  }

  private Node instantiateLeaf(final Node parent, final Square squarePlayed) {
    final var board = parent.cloneBoard();
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
