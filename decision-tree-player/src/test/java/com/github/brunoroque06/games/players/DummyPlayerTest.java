package com.github.brunoroque06.games.players;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Square;
import java.util.Arrays;
import java.util.Random;
import org.junit.jupiter.api.Test;

class DummyPlayerTest {
  @Test
  void Given2EmptySquaresAndRandomReturns1_WhenEstimateMove_ThenSecondEmptySquare() {
    final var board = mock(Board.class);
    final var emptySquares = Arrays.asList(new Square(0, 1), new Square(1, 0));
    when(board.estimateEmptySquares()).thenReturn(emptySquares);
    final var random = mock(Random.class);
    when(random.nextInt(2)).thenReturn(1);

    final var dummyPlayer = new DummyPlayer(random);

    final var square = dummyPlayer.chooseMove(board);

    assertThat(square.getRow()).isEqualTo(1);
    assertThat(square.getCol()).isEqualTo(0);
  }
}
