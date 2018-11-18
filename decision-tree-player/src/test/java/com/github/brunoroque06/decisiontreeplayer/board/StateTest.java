package com.github.brunoroque06.decisiontreeplayer.board;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class StateTest {
  private State state;
  private Board board3x3;

  @BeforeEach
  void setUp() {
    state = new State();
    board3x3 = new Board(3, 3, state);
  }

  @Test
  void PlayOrder() {
    assertTrue(state.isXTurn());
    state.nextState();
    assertTrue(state.isOTurn());
    state.nextState();
    assertTrue(state.isXTurn());
  }

  @Test
  void PieceOrder() {
    assertTrue(state.isXTurn());
    state.nextState();
    assertTrue(state.isOTurn());
    state.restart();
    assertTrue(state.isXTurn());
  }

  @Test
  void XWon159() {
    board3x3.playPiece(new Square(0, 0), Piece.X);
    board3x3.playPiece(new Square(0, 1), Piece.O);
    board3x3.playPiece(new Square(0, 2), Piece.O);
    board3x3.playPiece(new Square(1, 0), Piece.O);
    board3x3.playPiece(new Square(1, 1), Piece.X);
    board3x3.playPiece(new Square(1, 2), Piece.O);
    board3x3.playPiece(new Square(2, 0), Piece.O);
    board3x3.playPiece(new Square(2, 1), Piece.Default);
    board3x3.playPiece(new Square(2, 2), Piece.X);

    state.update(board3x3);

    assertTrue(state.hasXWon());
  }

  @Test
  void OWon123() {
    board3x3.playPiece(new Square(0, 0), Piece.O);
    board3x3.playPiece(new Square(0, 1), Piece.O);
    board3x3.playPiece(new Square(0, 2), Piece.O);
    board3x3.playPiece(new Square(1, 0), Piece.X);
    board3x3.playPiece(new Square(1, 1), Piece.X);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.O);
    board3x3.playPiece(new Square(2, 1), Piece.X);
    board3x3.playPiece(new Square(2, 2), Piece.X);

    state.update(board3x3);

    assertTrue(state.hasOWon());
  }

  @Test
  void XWon147() {
    board3x3.playPiece(new Square(0, 0), Piece.X);
    board3x3.playPiece(new Square(0, 1), Piece.O);
    board3x3.playPiece(new Square(0, 2), Piece.O);
    board3x3.playPiece(new Square(1, 0), Piece.X);
    board3x3.playPiece(new Square(1, 1), Piece.X);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.X);
    board3x3.playPiece(new Square(2, 1), Piece.Default);
    board3x3.playPiece(new Square(2, 2), Piece.O);

    state.update(board3x3);

    assertTrue(state.hasXWon());
  }

  @Test
  void OWon258() {
    board3x3.playPiece(new Square(0, 0), Piece.X);
    board3x3.playPiece(new Square(0, 1), Piece.O);
    board3x3.playPiece(new Square(0, 2), Piece.X);
    board3x3.playPiece(new Square(1, 0), Piece.Default);
    board3x3.playPiece(new Square(1, 1), Piece.O);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.X);
    board3x3.playPiece(new Square(2, 1), Piece.O);
    board3x3.playPiece(new Square(2, 2), Piece.O);

    state.update(board3x3);

    assertTrue(state.hasOWon());
  }

  @Test
  void XWon369() {
    board3x3.playPiece(new Square(0, 0), Piece.Default);
    board3x3.playPiece(new Square(0, 1), Piece.Default);
    board3x3.playPiece(new Square(0, 2), Piece.X);
    board3x3.playPiece(new Square(1, 0), Piece.Default);
    board3x3.playPiece(new Square(1, 1), Piece.Default);
    board3x3.playPiece(new Square(1, 2), Piece.X);
    board3x3.playPiece(new Square(2, 0), Piece.Default);
    board3x3.playPiece(new Square(2, 1), Piece.Default);
    board3x3.playPiece(new Square(2, 2), Piece.X);

    state.update(board3x3);

    assertTrue(state.hasXWon());
  }

  @Test
  void DrawnFullBoard() {
    board3x3.playPiece(new Square(0, 0), Piece.X);
    board3x3.playPiece(new Square(0, 1), Piece.O);
    board3x3.playPiece(new Square(0, 2), Piece.X);
    board3x3.playPiece(new Square(1, 0), Piece.O);
    board3x3.playPiece(new Square(1, 1), Piece.X);
    board3x3.playPiece(new Square(1, 2), Piece.O);
    board3x3.playPiece(new Square(2, 0), Piece.O);
    board3x3.playPiece(new Square(2, 1), Piece.X);
    board3x3.playPiece(new Square(2, 2), Piece.O);

    state.update(board3x3);

    assertTrue(state.isGameDrawn());
  }

  @Test
  void CorrectState() {
    board3x3.playPiece(new Square(0, 0), Piece.O);
    board3x3.playPiece(new Square(0, 1), Piece.X);
    board3x3.playPiece(new Square(0, 2), Piece.O);
    board3x3.playPiece(new Square(1, 0), Piece.O);
    board3x3.playPiece(new Square(1, 1), Piece.X);
    board3x3.playPiece(new Square(1, 2), Piece.X);
    board3x3.playPiece(new Square(2, 0), Piece.X);
    board3x3.playPiece(new Square(2, 1), Piece.O);
    board3x3.playPiece(new Square(2, 2), Piece.Default);

    state.update(board3x3);

    assertTrue(state.isOTurn());
  }

  @Test
  void OTurn() {
    board3x3.playPiece(new Square(0, 0), Piece.Default);
    board3x3.playPiece(new Square(0, 1), Piece.Default);
    board3x3.playPiece(new Square(0, 2), Piece.Default);
    board3x3.playPiece(new Square(1, 0), Piece.Default);
    board3x3.playPiece(new Square(1, 1), Piece.Default);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.Default);
    board3x3.playPiece(new Square(2, 1), Piece.X);
    board3x3.playPiece(new Square(2, 2), Piece.Default);

    state.update(board3x3);

    assertTrue(state.isOTurn());
  }

  @Test
  void Clone() {
    final State state = new State();
    final State newState = state.cloneState();

    assertNotEquals(state, newState);
    assertEquals(state.isXTurn(), newState.isXTurn());
  }
}
