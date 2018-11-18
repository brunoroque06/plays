package com.github.brunoroque06.decisiontreeplayer.players;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;
import com.github.brunoroque06.decisiontreeplayer.tree.DecisionTree;
import org.junit.jupiter.api.Test;

class DecisionTreePlayerTest {
  @Test
  void CorrectMoveReturned() {
    final DecisionTree decisionTree = mock(DecisionTree.class);
    final Board board = mock(Board.class);
    final int depthToCalculate = 2;
    when(decisionTree.estimateBestMove(board, depthToCalculate)).thenReturn(new Square(1, 1));

    final Square square = new DecisionTreePlayer(decisionTree, depthToCalculate).chooseMove(board);

    assertEquals(1, square.getRow());
    assertEquals(1, square.getCol());
  }
}
