package com.github.brunoroque06.games.tictactoe;

import com.github.brunoroque06.games.board.Piece;

public enum TicTacToePiece implements Piece {
  WHITE,
  BLACK,
  EMPTY;

  @Override
  public boolean isWhite() {
    return this == WHITE;
  }
}
