package com.github.brunoroque06.games.tictactoe;

import com.github.brunoroque06.games.board.PieceFactory;

public class TicTacToePieceFactory implements PieceFactory<TicTacToePiece> {

  public TicTacToePieceFactory() {}

  @Override
  public TicTacToePiece getWhite() {
    return TicTacToePiece.WHITE;
  }

  @Override
  public TicTacToePiece getBlack() {
    return TicTacToePiece.BLACK;
  }

  @Override
  public TicTacToePiece getEmpty() {
    return TicTacToePiece.EMPTY;
  }
}
