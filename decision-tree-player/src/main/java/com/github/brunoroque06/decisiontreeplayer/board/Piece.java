package com.github.brunoroque06.decisiontreeplayer.board;

public enum Piece {
  X,
  O,
  Default;

  boolean isDefault() {
    return this == Piece.Default;
  }
}
