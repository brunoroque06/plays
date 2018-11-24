package com.github.brunoroque06.games;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Piece;
import com.github.brunoroque06.games.board.State;
import com.github.brunoroque06.games.players.Player;
import org.junit.jupiter.api.Test;

class GameTest {
  @Test
  void GivenDrawOrWin_ThenGameFinished() {
    final var state = mock(State.class);
    when(state.isGameWonOrDrawn()).thenReturn(true);
    when(state.isGameDrawn()).thenReturn(true);
    final var board = mock(Board.class);
    when(board.getStatus()).thenReturn(state);
    when(board.cloneBoard()).thenReturn(board);

    final var game = new Game(board, mock(Player.class), mock(Player.class));

    assertTrue(game.process().getStatus().isGameDrawn());
  }

  @Test
  void CorrectBoardReset() {
    final var game = new Game(new Board(3, 3, new State()), mock(Player.class), mock(Player.class));

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
