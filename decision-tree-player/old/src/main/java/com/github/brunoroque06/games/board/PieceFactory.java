package com.github.brunoroque06.games.board;

public interface PieceFactory<T extends Piece> {

  T getWhite();

  T getBlack();

  T getEmpty();
}
