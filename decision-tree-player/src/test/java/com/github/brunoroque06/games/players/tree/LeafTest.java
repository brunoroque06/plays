package com.github.brunoroque06.games.players.tree;

import static org.assertj.core.api.Java6Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.Piece;
import com.github.brunoroque06.games.board.TestPiece;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class LeafTest {

  private Leaf<Piece> root;
  private Board<Piece> board;

  @BeforeEach
  void setup() {
    board = mock(Board.class);
    final var leaf1 = new Leaf<>(board, new Coordinate(0, 0));
    leaf1.setEvaluation(10);
    final var leaf2 = new Leaf<>(board, new Coordinate(1, 1));
    leaf2.setEvaluation(0);
    final var leaf3 = new Leaf<>(board, new Coordinate(2, 2));
    leaf3.setEvaluation(-10);

    root = new Leaf<>(board, new Coordinate(0, 0));
    root.addLeaf(leaf1);
    root.addLeaf(leaf2);
    root.addLeaf(leaf3);
  }

  @Test
  void GivenWhiteToMove_WhenUpdateEvaluation_ThenHighestValueIsPicked() {
    when(board.getToMove()).thenReturn(TestPiece.WHITE);

    root.updateEvaluation();

    assertThat(root.getEvaluation()).isEqualTo(10);
    assertThat(root.findBestLeaf()).isEqualToComparingFieldByField(new Coordinate(0, 0));
  }

  @Test
  void GivenBlackToMove_WhenUpdateEvaluation_ThenLowestValueIsPicked() {
    when(board.getToMove()).thenReturn(TestPiece.BLACK);

    root.updateEvaluation();

    assertThat(root.getEvaluation()).isEqualTo(-10);
    assertThat(root.findBestLeaf()).isEqualToComparingFieldByField(new Coordinate(2, 2));
  }
}
