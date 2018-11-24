package com.github.brunoroque06.games;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.State;
import org.junit.jupiter.api.Test;

class GamesRunnerTest {
  @Test
  void GamesAndScoresAreCorrect() {
    final var state = mock(State.class);
    when(state.isGameDrawn()).thenReturn(true);
    final var board = mock(Board.class);
    when(board.getStatus()).thenReturn(state);
    final var game = mock(Game.class);
    when(game.process()).thenReturn(board);
    final var numberOfGames = 3;

    final var gamesRunner = new GamesRunner(game, numberOfGames);

    gamesRunner.run();
    final var gameResults = gamesRunner.getGameResults();

    assertEquals(numberOfGames, gameResults.size());
    assertTrue(gameResults.get(0).getStatus().isGameDrawn());
    assertTrue(gameResults.get(1).getStatus().isGameDrawn());
    assertTrue(gameResults.get(2).getStatus().isGameDrawn());
  }
}
