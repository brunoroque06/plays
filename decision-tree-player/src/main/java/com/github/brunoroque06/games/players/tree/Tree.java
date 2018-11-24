package com.github.brunoroque06.games.players.tree;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.Piece;
import com.github.brunoroque06.games.game.Game;

public class Tree<T extends Piece> {
  private final LeafsFactory<T> leafsFactory;
  private final Game<T> game;

  public Tree(final LeafsFactory<T> leafsFactory, final Game<T> game) {
    this.leafsFactory = leafsFactory;
    this.game = game;
  }

  Coordinate findBestMove(final Board<T> board, final int depth) {
    if (board.isEmpty()) {
      return new Coordinate(1, 1);
    }
    final var root = leafsFactory.createRoot(board);
    createLeafs(root, depth - 1);
    return root.findBestLeaf();
  }

  private void createLeafs(final Leaf<T> parent, final int depth) {
    final var possibleMoves = parent.getBoard().getEmptyCoordinates();
    for (final var move : possibleMoves) {
      final var leaf = createLeaf(parent, move);
      if (isBranchComplete(depth, leaf)) {
        final var evaluation = game.evaluatePosition(leaf.getBoard());
        leaf.setEvaluation(evaluation);
      } else {
        createLeafs(leaf, depth - 1);
      }
    }
    parent.updateEvaluation();
  }

  private Leaf<T> createLeaf(final Leaf<T> parent, final Coordinate move) {
    final var board = parent.getBoard().shallowClone();
    board.playMove(move);
    final var leaf = leafsFactory.create(board, move);
    parent.addLeaf(leaf);
    return leaf;
  }

  private boolean isBranchComplete(final int depth, final Leaf<T> leaf) {
    return depth == 0 || game.isOver(leaf.getBoard());
  }
}
