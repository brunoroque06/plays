package com.github.brunoroque06.games.players;

import static org.assertj.core.api.Java6Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import java.util.Arrays;
import java.util.Random;
import org.junit.jupiter.api.Test;

class DummyPlayerTest {
  @Test
  void Given2EmptySquaresAndRandomReturns1_WhenEstimateMove_ThenSecondEmptySquare() {
    final var board = mock(Board.class);
    final var emptyCoordinates = Arrays.asList(new Coordinate(0, 1), new Coordinate(1, 0));
    when(board.getEmptyCoordinates()).thenReturn(emptyCoordinates);
    final var random = mock(Random.class);
    when(random.nextInt(2)).thenReturn(1);

    final var dummyPlayer = new DummyPlayer<>(random);

    final var coordinate = dummyPlayer.chooseMove(board);

    assertThat(coordinate.getRow()).isEqualTo(1);
    assertThat(coordinate.getCol()).isEqualTo(0);
  }
}
