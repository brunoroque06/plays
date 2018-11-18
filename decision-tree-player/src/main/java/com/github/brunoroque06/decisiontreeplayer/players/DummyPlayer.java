package com.github.brunoroque06.decisiontreeplayer.players;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;
import java.util.List;
import java.util.Random;

public class DummyPlayer implements Player {
  @Override
  public Square chooseMove(final Board board) {
    final List<Square> squares = board.estimateEmptySquares();
    final int randomIndex = generateRandomIndex(squares.size());

    return squares.get(randomIndex);
  }

  private int generateRandomIndex(final int maxIndex) {
    final Random random = new Random();
    return Math.round(random.nextInt(maxIndex));
  }
}
