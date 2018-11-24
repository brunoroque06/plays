package com.github.brunoroque06.games.board;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class BoardTest {
  private Board board1x1;
  private Board board2x2;
  private Board board3x2;
  private Board board3x3;

  @BeforeEach
  void setUp() {
    final var state = mock(State.class);
    when(state.isOTurn()).thenReturn(true);

    board1x1 = new Board(1, 1, state);
    board2x2 = new Board(2, 2, state);
    board3x2 = new Board(3, 2, state);
    board3x3 = new Board(3, 3, state);
  }

  @Test
  void Given3x2Board_ThenPosition3() {
    final var square = new Square(1, 1);
    final var arrayIndex = board3x2.squareToIndex(square);

    Assertions.assertEquals(3, arrayIndex);
  }

  @Test
  void ANewBoardHasDefaultPieces() {
    assertEquals(Piece.Default, board2x2.getPiece(new Square(0, 0)));
    assertEquals(Piece.Default, board2x2.getPiece(new Square(0, 1)));
    assertEquals(Piece.Default, board2x2.getPiece(new Square(1, 0)));
    assertEquals(Piece.Default, board2x2.getPiece(new Square(1, 1)));
  }

  @Test
  void GivenNegativeRow_ThenDefaultPiece() {
    final var piece = board3x2.getPiece(new Square(-1, 0));
    assertEquals(Piece.Default, piece);
  }

  @Test
  void GivenNegativeCol_ThenDefaultPiece() {
    final var piece = board3x2.getPiece(new Square(0, -1));
    assertEquals(Piece.Default, piece);
  }

  @Test
  void GivenNumberHigherThanBoardSize_ThenDefaultPiece() {
    final var piece = board3x2.getPiece(new Square(2, 2));
    assertEquals(Piece.Default, piece);
  }

  @Test
  void AfterAMoveTheCorrectSquareIsUpdated() {
    final var pieceToPlace = Piece.X;
    final var squareToPlace = new Square(1, 1);

    board2x2.playPiece(squareToPlace, pieceToPlace);

    assertEquals(pieceToPlace, board2x2.getPiece(squareToPlace));
  }

  @Test
  void ExceptionIsThrownWhenWrongSquareIsProvided() {
    assertThrows(
        IndexOutOfBoundsException.class, () -> board3x2.playPiece(new Square(-2, -2), Piece.X));
  }

  @Test
  void GivenBoard2x2WithXPieces_WhenIsBoardFull_ThenTrue() {
    board2x2.playPiece(new Square(0, 0), Piece.X);
    board2x2.playPiece(new Square(0, 1), Piece.X);
    board2x2.playPiece(new Square(1, 0), Piece.X);
    board2x2.playPiece(new Square(1, 1), Piece.X);

    final var isBoardFull = board2x2.isBoardFull();

    Assertions.assertTrue(isBoardFull);
  }

  @Test
  void GivenPlayPiece_WhenSquareIsOccupied_ThenException() {
    final var square = new Square(0, 0);

    board1x1.playPiece(square, Piece.X);

    assertThrows(Exception.class, () -> board1x1.playPiece(square, Piece.O));
  }

  @Test
  void CloneToBeEqual() {
    board2x2.updateStatus();
    board2x2.playPiece(new Square(0, 0), Piece.X);
    board2x2.playPiece(new Square(0, 1), Piece.O);
    board2x2.playPiece(new Square(1, 0), Piece.Default);
    board2x2.playPiece(new Square(1, 1), Piece.X);

    final var newBoard = board2x2.cloneBoard();

    assertEquals(2, newBoard.getCols());
    assertEquals(2, newBoard.getRows());
    assertEquals(Piece.X, newBoard.getPiece(0, 0));
    assertEquals(Piece.O, newBoard.getPiece(0, 1));
    assertEquals(Piece.Default, newBoard.getPiece(1, 0));
    assertEquals(Piece.X, newBoard.getPiece(1, 1));
  }

  @Test
  void EmptySquaresAreCorrectlyEstimated() {
    board3x3.playPiece(new Square(0, 0), Piece.X);
    board3x3.playPiece(new Square(0, 1), Piece.X);
    board3x3.playPiece(new Square(0, 2), Piece.O);
    board3x3.playPiece(new Square(1, 2), Piece.O);
    board3x3.playPiece(new Square(2, 2), Piece.O);

    final var squares = board3x3.estimateEmptySquares();

    assertEquals(4, squares.size());
    assertEquals(1, squares.get(0).getRow());
    assertEquals(0, squares.get(0).getCol());
    assertEquals(1, squares.get(1).getRow());
    assertEquals(1, squares.get(1).getCol());
    assertEquals(2, squares.get(2).getRow());
    assertEquals(0, squares.get(2).getCol());
    assertEquals(2, squares.get(3).getRow());
    assertEquals(1, squares.get(3).getCol());
  }

  @Test
  void StateClone() {
    final var state = mock(State.class);
    final var board = new Board(1, 1, state);

    final var newBoard = board.cloneBoard();

    assertNotEquals(board.getStatus(), newBoard.getStatus());
  }
}
