package com.github.brunoroque06.games.players;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.Piece;
import java.util.Random;

public class DummyPlayer<T extends Piece> implements Player<T> {

  private final Random random;

  public DummyPlayer(final Random random) {
    this.random = random;
  }

  @Override
  public Coordinate chooseMove(final Board<T> board) {
    final var squares = board.getEmptyCoordinates();
    final var randomIndex = random.nextInt(squares.size());
    return squares.get(randomIndex);
  }
}
