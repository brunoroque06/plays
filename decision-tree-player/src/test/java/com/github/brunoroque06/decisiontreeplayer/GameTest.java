package com.github.brunoroque06.decisiontreeplayer;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Piece;
import com.github.brunoroque06.decisiontreeplayer.board.State;
import com.github.brunoroque06.decisiontreeplayer.players.Player;
import org.junit.jupiter.api.Test;

class GameTest {
  @Test
  void GivenDrawOrWin_ThenGameFinished() {
    final Board boardMock = mock(Board.class);
    final State stateMock = mock(State.class);
    when(stateMock.isGameDrawn()).thenReturn(true);
    when(stateMock.isGameWonOrDrawn()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(stateMock);
    when(boardMock.cloneBoard()).thenReturn(boardMock);

    final Game game = new Game(boardMock, mock(Player.class), mock(Player.class));

    assertTrue(game.process().getStatus().isGameDrawn());
  }

  @Test
  void CorrectBoardReset() {
    final Game game =
        new Game(new Board(3, 3, new State()), mock(Player.class), mock(Player.class));

    game.resetGame();

    assertTrue(game.getBoard().getStatus().isXTurn());
    assertEquals(Piece.Default, game.getBoard().getPiece(0, 0));
    assertEquals(Piece.Default, game.getBoard().getPiece(0, 1));
    assertEquals(Piece.Default, game.getBoard().getPiece(0, 2));
    assertEquals(Piece.Default, game.getBoard().getPiece(1, 0));
    assertEquals(Piece.Default, game.getBoard().getPiece(1, 1));
    assertEquals(Piece.Default, game.getBoard().getPiece(1, 2));
    assertEquals(Piece.Default, game.getBoard().getPiece(2, 0));
    assertEquals(Piece.Default, game.getBoard().getPiece(2, 1));
    assertEquals(Piece.Default, game.getBoard().getPiece(2, 2));
  }
}
