package com.github.brunoroque06.games.game;

import static org.assertj.core.api.Java6Assertions.assertThat;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.players.Player;
import org.junit.jupiter.api.Test;

class GameArbiterTest {

  @Test
  void GivenGameNeeds2TurnsToFinish_WhenPlayGame() {
    final var board = mock(Board.class);

    final var whitePlayer = mock(Player.class);
    final var whiteCoordinate = new Coordinate(0, 0);
    when(whitePlayer.chooseMove(board)).thenReturn(whiteCoordinate);

    final var blackPlayer = mock(Player.class);
    final var blackCoordinate = new Coordinate(1, 1);
    when(blackPlayer.chooseMove(board)).thenReturn(blackCoordinate);

    final var game = mock(Game.class);
    when(game.isOver(any())).thenReturn(false, false, false, true);
    when(game.getResult(any())).thenReturn(GameResult.WHITE_WON);

    final var gameHandler = new GameArbiter<>(board, whitePlayer, blackPlayer, game);

    assertThat(gameHandler.play()).isEqualTo(GameResult.WHITE_WON);
    verify(whitePlayer, times(2)).chooseMove(board);
    verify(board, times(2)).playMove(whiteCoordinate);
    verify(blackPlayer, times(1)).chooseMove(board);
    verify(board, times(1)).playMove(blackCoordinate);
  }
}
