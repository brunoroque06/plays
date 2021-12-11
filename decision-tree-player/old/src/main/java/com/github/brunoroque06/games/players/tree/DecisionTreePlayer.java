package com.github.brunoroque06.games.players.tree;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.Piece;
import com.github.brunoroque06.games.players.Player;

public class DecisionTreePlayer<T extends Piece> implements Player<T> {
  private final Tree<T> tree;
  private final int depth;

  public DecisionTreePlayer(final Tree<T> tree, final int depth) {
    this.tree = tree;
    this.depth = depth;
  }

  @Override
  public Coordinate chooseMove(final Board<T> board) {
    return tree.findBestMove(board, depth);
  }
}
