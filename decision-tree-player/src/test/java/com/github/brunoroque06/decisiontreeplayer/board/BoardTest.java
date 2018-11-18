package com.github.brunoroque06.decisiontreeplayer.board;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class BoardTest {
  private Board board1x1;
  private Board board2x2;
  private Board board3x2;
  private Board board3x3;

  @BeforeEach
  void setUp() {
    final State stateMock = mock(State.class);
    when(stateMock.isOTurn()).thenReturn(true);

    board1x1 = new Board(1, 1, stateMock);
    board2x2 = new Board(2, 2, stateMock);
    board3x2 = new Board(3, 2, stateMock);
    board3x3 = new Board(3, 3, stateMock);
  }

  @Test
  void Given3x2Board_ThenPosition3() {
    final Square square = new Square(1, 1);
    final int arrayIndex = board3x2.squareToIndex(square);

    assertEquals(3, arrayIndex);
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
    final Piece piece = board3x2.getPiece(new Square(-1, 0));
    assertEquals(Piece.Default, piece);
  }

  @Test
  void GivenNegativeCol_ThenDefaultPiece() {
    final Piece piece = board3x2.getPiece(new Square(0, -1));
    assertEquals(Piece.Default, piece);
  }

  @Test
  void GivenNumberHigherThanBoardSize_ThenDefaultPiece() {
    final Piece piece = board3x2.getPiece(new Square(2, 2));
    assertEquals(Piece.Default, piece);
  }

  @Test
  void AfterAMoveTheCorrectSquareIsUpdated() {
    final Piece pieceToPlace = Piece.X;
    final Square squareToPlace = new Square(1, 1);

    board2x2.playPiece(squareToPlace, pieceToPlace);

    assertEquals(pieceToPlace, board2x2.getPiece(squareToPlace));
  }

  @Test
  void ExceptionIsThrownWhenWrongSquareIsProvided() {
    assertThrows(
        IndexOutOfBoundsException.class, () -> board3x2.playPiece(new Square(-2, -2), Piece.X));
  }

  @Test
  void FullBoard() {
    board2x2.playPiece(new Square(0, 0), Piece.X);
    board2x2.playPiece(new Square(0, 1), Piece.X);
    board2x2.playPiece(new Square(1, 0), Piece.X);
    board2x2.playPiece(new Square(1, 1), Piece.X);

    final boolean isBoardFull = board2x2.isBoardFull();

    assertTrue(isBoardFull);
  }

  @Test
  void GivenPlayPiece_WhenSquareIsOccupied_ThenException() {
    final Square square = new Square(0, 0);

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

    final Board newBoard = board2x2.cloneBoard();

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

    final List<Square> squares = board3x3.estimateEmptySquares();

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
    final State stateMock = mock(State.class);
    final Board board = new Board(1, 1, stateMock);

    final Board newBoard = board.cloneBoard();

    assertNotEquals(board.getStatus(), newBoard.getStatus());
  }
}
