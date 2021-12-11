package com.github.brunoroque06.games.players.tree;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.Piece;

public class LeafsFactory<T extends Piece> {

  Leaf<T> createRoot(final Board<T> board) {
    return new Leaf<>(board);
  }

  Leaf<T> create(final Board<T> board, final Coordinate move) {
    return new Leaf<>(board, move);
  }
}
