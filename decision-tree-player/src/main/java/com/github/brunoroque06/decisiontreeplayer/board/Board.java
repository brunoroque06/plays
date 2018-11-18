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

  private void emptyBoard() {
    for (int i = 0; i < board.length; i++) {
      board[i] = Piece.Default;
    }
  }

  public Piece getPiece(final int row, final int col) {
    return getPiece(new Square(row, col));
  }

  Piece getPiece(final Square square) {
    final int index = squareToIndex(square);
    return checkIndexValidity(index) ? board[index] : Piece.Default;
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

  private boolean checkIndexValidity(final int index) {
    return index >= 0 && index < board.length;
  }

  public void playPieceAndUpdateState(final Square square) {
    final Piece pieceToPlay = state.estimatePieceToPlay();
    playPiece(square, pieceToPlay);
    updateStatus();
  }

  public void playPiece(final Square square, final Piece piece) {
    final int index = squareToIndex(square);
    canPieceBePlaced(index);
    board[index] = piece;
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
    for (final Piece piece : board) {
      if (!isSquareEmpty(piece)) {
        return false;
      }
    }
    return true;
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
    final Board newBoard = new Board(this.getRows(), this.getCols(), state.cloneState());

    for (int r = 0; r < newBoard.getRows(); r++) {
      for (int c = 0; c < newBoard.getCols(); c++) {
        newBoard.playPiece(new Square(r, c), this.getPiece(r, c));
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

  private boolean isSquareEmpty(final Piece piece) {
    return piece == Piece.Default;
  }
}
