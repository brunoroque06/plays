package com.github.brunoroque06.games.players;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Square;
import java.util.Random;

public class DummyPlayer implements Player {

  private final Random random;

  public DummyPlayer(final Random random) {
    this.random = random;
  }

  @Override
  public Square chooseMove(final Board board) {
    final var squares = board.estimateEmptySquares();
    final var randomIndex = random.nextInt(squares.size());
    return squares.get(randomIndex);
  }
}
