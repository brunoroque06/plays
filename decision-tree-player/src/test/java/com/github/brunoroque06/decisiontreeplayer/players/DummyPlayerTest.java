package com.github.brunoroque06.decisiontreeplayer.players;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;

class DummyPlayerTest {
  @Test
  void EmptySquareIsReturned() {
    final Board board = mock(Board.class);
    when(board.estimateEmptySquares())
        .thenReturn(
            new ArrayList<Square>() {
              {
                add(new Square(0, 1));
                add(new Square(1, 0));
              }
            });

    final Player dummyPlayer = new DummyPlayer();

    final Square square = dummyPlayer.chooseMove(board);

    assertTrue(
        square.getRow() == 0 && square.getCol() == 1
            || square.getRow() == 1 && square.getCol() == 0);
  }
}
