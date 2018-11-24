package com.github.brunoroque06.games.players;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Square;
import com.github.brunoroque06.games.tree.DecisionTree;
import org.junit.jupiter.api.Test;

class DecisionTreePlayerTest {
  @Test
  void CorrectMoveReturned() {
    final var decisionTree = mock(DecisionTree.class);
    final var board = mock(Board.class);
    final var depthToCalculate = 2;
    when(decisionTree.estimateBestMove(board, depthToCalculate)).thenReturn(new Square(1, 1));

    final var square = new DecisionTreePlayer(decisionTree, depthToCalculate).chooseMove(board);

    assertEquals(1, square.getRow());
    assertEquals(1, square.getCol());
  }
}
