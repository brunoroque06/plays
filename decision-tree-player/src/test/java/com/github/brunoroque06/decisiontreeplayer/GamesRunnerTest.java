package com.github.brunoroque06.decisiontreeplayer;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.State;
import java.util.List;
import org.junit.jupiter.api.Test;

class GamesRunnerTest {
  @Test
  void GamesAndScoresAreCorrect() {
    final State stateMock = mock(State.class);
    when(stateMock.isGameDrawn()).thenReturn(true);
    final Board boardMock = mock(Board.class);
    when(boardMock.getStatus()).thenReturn(stateMock);
    final Game gameMock = mock(Game.class);
    when(gameMock.process()).thenReturn(boardMock);
    final int numberOfGames = 3;

    final GamesRunner gamesRunner = new GamesRunner(gameMock, numberOfGames);

    gamesRunner.runGames();
    final List<Board> gameResults = gamesRunner.getGameResults();

    assertEquals(numberOfGames, gameResults.size());
    assertTrue(gameResults.get(0).getStatus().isGameDrawn());
    assertTrue(gameResults.get(1).getStatus().isGameDrawn());
    assertTrue(gameResults.get(2).getStatus().isGameDrawn());
  }
}
