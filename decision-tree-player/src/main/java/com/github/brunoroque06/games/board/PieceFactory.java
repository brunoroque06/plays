package com.github.brunoroque06.games.board;

public interface PieceFactory<T> {

  T getWhite();

  T getBlack();

  T getEmpty();
}
