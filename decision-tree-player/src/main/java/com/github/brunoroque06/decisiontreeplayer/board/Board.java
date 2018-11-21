package com.github.brunoroque06.decisiontreeplayer.board;

import java.util.ArrayList;
import java.util.List;

public class Board {
  private final int row;
  private final int col;
  private final Piece[] board;
  private final State state;

  public Board(final int numberRows, final int numberCols, final State state) {
    board = new Piece[numberRows * numberCols];
    row = numberRows;
    col = numberCols;
    this.state = state;
    emptyBoard();
  }

  private void emptyBoard() {
    for (var i = 0; i < board.length; i++) {
      board[i] = Piece.Default;
    }
  }

  int getRows() {
    return row;
  }

  int getCols() {
    return col;
  }

  public State getStatus() {
    return state;
  }

  public void resetBoard() {
    emptyBoard();
    state.restart();
  }

  public void playPieceAndUpdateState(final Square square) {
    final var pieceToPlay = state.whichPieceToPlay();
    playPiece(square, pieceToPlay);
    updateStatus();
  }

  public void playPiece(final Square square, final Piece piece) {
    final var index = squareToIndex(square);
    canPieceBePlaced(index);
    board[index] = piece;
  }

  int squareToIndex(final Square square) {
    return isSquareValid(square) ? square.getRow() * col + square.getCol() : -1;
  }

  private boolean isSquareValid(final Square square) {
    return square.getRow() >= 0
        && square.getCol() >= 0
        && square.getRow() < row
        && square.getCol() < col;
  }

  private void canPieceBePlaced(final int index) throws IndexOutOfBoundsException {
    if (!board[index].isDefault()) {
      throw new IndexOutOfBoundsException();
    }
  }

  void updateStatus() {
    state.update(this);
  }

  public boolean isBoardEmpty() {
    for (final var piece : board) {
      if (!isSquareEmpty(piece)) {
        return false;
      }
    }
    return true;
  }

  private boolean isSquareEmpty(final Piece piece) {
    return piece == Piece.Default;
  }

  boolean isBoardFull() {
    int numberEmptySquares = 0;
    for (final Piece piece : board) {
      if (piece.isDefault()) {
        numberEmptySquares++;
        break;
      }
    }
    return numberEmptySquares == 0;
  }

  public Board cloneBoard() {
    final Board newBoard = new Board(getRows(), getCols(), state.cloneState());

    for (int r = 0; r < newBoard.getRows(); r++) {
      for (int c = 0; c < newBoard.getCols(); c++) {
        newBoard.playPiece(new Square(r, c), getPiece(r, c));
      }
    }
    return newBoard;
  }

  public List<Square> estimateEmptySquares() {
    final List<Square> squares = new ArrayList<>();

    for (int r = 0; r < row; r++) {
      for (int c = 0; c < col; c++) {
        if (isSquareEmpty(getPiece(r, c))) {
          squares.add(new Square(r, c));
        }
      }
    }
    return squares;
  }

  public Piece getPiece(final int row, final int col) {
    return getPiece(new Square(row, col));
  }

  Piece getPiece(final Square square) {
    final var index = squareToIndex(square);
    return checkIndexValidity(index) ? board[index] : Piece.Default;
  }

  private boolean checkIndexValidity(final int index) {
    return index >= 0 && index < board.length;
  }
}
