package com.github.brunoroque06.decisiontreeplayer.tree;

import static org.junit.jupiter.api.Assertions.assertEquals;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Piece;
import com.github.brunoroque06.decisiontreeplayer.board.Square;
import com.github.brunoroque06.decisiontreeplayer.board.State;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class DecisionTreeTest {
  private Board board3x3;
  private NodeFactory nodeFactory;

  @BeforeEach
  void setUp() {
    board3x3 = new Board(3, 3, new State());
    nodeFactory = new NodeFactory();
  }

  @Test
  void WinningMoveIsReturned() {
    board3x3.playPiece(new Square(0, 0), Piece.X);
    board3x3.playPiece(new Square(0, 1), Piece.O);
    board3x3.playPiece(new Square(0, 2), Piece.X);
    board3x3.playPiece(new Square(1, 0), Piece.O);
    board3x3.playPiece(new Square(1, 1), Piece.Default);
    board3x3.playPiece(new Square(1, 2), Piece.O);
    board3x3.playPiece(new Square(2, 0), Piece.X);
    board3x3.playPiece(new Square(2, 1), Piece.O);
    board3x3.playPiece(new Square(2, 2), Piece.Default);

    final var square = new DecisionTree(nodeFactory).estimateBestMove(board3x3, 2);

    assertEquals(1, square.getRow());
    assertEquals(1, square.getCol());
  }

  @Test
  void MoveThatStopsOpponentFromWinningIsReturned() {
    board3x3.playPiece(new Square(0, 0), Piece.O);
    board3x3.playPiece(new Square(0, 1), Piece.Default);
    board3x3.playPiece(new Square(0, 2), Piece.Default);
    board3x3.playPiece(new Square(1, 0), Piece.Default);
    board3x3.playPiece(new Square(1, 1), Piece.Default);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.X);
    board3x3.playPiece(new Square(2, 1), Piece.X);
    board3x3.playPiece(new Square(2, 2), Piece.O);

    final var square = new DecisionTree(nodeFactory).estimateBestMove(board3x3, 3);

    assertEquals(1, square.getRow());
    assertEquals(1, square.getCol());
  }

  @Test
  void WinningMoveThatRequiresADepthOf5MovesIsReturned() {
    board3x3.playPiece(new Square(0, 0), Piece.Default);
    board3x3.playPiece(new Square(0, 1), Piece.Default);
    board3x3.playPiece(new Square(0, 2), Piece.Default);
    board3x3.playPiece(new Square(1, 0), Piece.O);
    board3x3.playPiece(new Square(1, 1), Piece.Default);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.X);
    board3x3.playPiece(new Square(2, 1), Piece.Default);
    board3x3.playPiece(new Square(2, 2), Piece.Default);

    final var square = new DecisionTree(nodeFactory).estimateBestMove(board3x3, 5);

    assertEquals(1, square.getRow());
    assertEquals(1, square.getCol());
  }

  @Test
  void FirstMoveShouldBeInTheCenterOfTheBoard() {
    board3x3.playPiece(new Square(0, 0), Piece.Default);
    board3x3.playPiece(new Square(0, 1), Piece.Default);
    board3x3.playPiece(new Square(0, 2), Piece.Default);
    board3x3.playPiece(new Square(1, 0), Piece.Default);
    board3x3.playPiece(new Square(1, 1), Piece.Default);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.Default);
    board3x3.playPiece(new Square(2, 1), Piece.Default);
    board3x3.playPiece(new Square(2, 2), Piece.Default);

    final var square = new DecisionTree(nodeFactory).estimateBestMove(board3x3, 5);

    assertEquals(1, square.getRow());
    assertEquals(1, square.getCol());
  }

  @Test
  void DrawADrawnPosition() {
    board3x3.playPiece(new Square(0, 0), Piece.Default);
    board3x3.playPiece(new Square(0, 1), Piece.Default);
    board3x3.playPiece(new Square(0, 2), Piece.X);
    board3x3.playPiece(new Square(1, 0), Piece.X);
    board3x3.playPiece(new Square(1, 1), Piece.O);
    board3x3.playPiece(new Square(1, 2), Piece.O);
    board3x3.playPiece(new Square(2, 0), Piece.Default);
    board3x3.playPiece(new Square(2, 1), Piece.O);
    board3x3.playPiece(new Square(2, 2), Piece.X);

    final var square = new DecisionTree(nodeFactory).estimateBestMove(board3x3, 3);

    assertEquals(0, square.getRow());
    assertEquals(1, square.getCol());
  }

  @Test
  void Play2ConsecutiveMovesThatWin() {
    board3x3.playPiece(new Square(0, 0), Piece.O);
    board3x3.playPiece(new Square(0, 1), Piece.O);
    board3x3.playPiece(new Square(0, 2), Piece.Default);
    board3x3.playPiece(new Square(1, 0), Piece.X);
    board3x3.playPiece(new Square(1, 1), Piece.O);
    board3x3.playPiece(new Square(1, 2), Piece.Default);
    board3x3.playPiece(new Square(2, 0), Piece.Default);
    board3x3.playPiece(new Square(2, 1), Piece.Default);
    board3x3.playPiece(new Square(2, 2), Piece.X);

    final var firstMove = new DecisionTree(nodeFactory).estimateBestMove(board3x3, 3);
    board3x3.playPieceAndUpdateState(firstMove);

    assertEquals(0, firstMove.getRow());
    assertEquals(2, firstMove.getCol());

    final var secondMove = new DecisionTree(nodeFactory).estimateBestMove(board3x3, 3);

    assertEquals(2, secondMove.getRow());
    assertEquals(1, secondMove.getCol());
  }
}
