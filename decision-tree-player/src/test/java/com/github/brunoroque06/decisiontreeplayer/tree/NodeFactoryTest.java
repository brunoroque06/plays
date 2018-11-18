package com.github.brunoroque06.decisiontreeplayer.tree;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class NodeFactoryTest {
  private NodeFactory nodeFactory;

  @BeforeEach
  void setUp() {
    nodeFactory = new NodeFactory();
  }

  @Test
  void RootNodeInstantiation() {
    final Board boardMock = mock(Board.class);
    when(boardMock.isBoardEmpty()).thenReturn(false);
    final Node root = nodeFactory.instantiateRoot(boardMock);

    assertFalse(root.isBoardEmpty());
    assertEquals(0, root.getMinimax());
    assertEquals(0, root.getDepth());
    assertNull(root.getMove());
  }

  @Test
  void NoteInstantiation() {
    final Board boardMock = mock(Board.class);
    when(boardMock.isBoardEmpty()).thenReturn(false);
    final Square move = new Square(0, 0);
    final Node root = nodeFactory.instantiateRoot(boardMock);

    final Node node = nodeFactory.instantiateNode(boardMock, move, root);

    assertFalse(node.isBoardEmpty());
    assertEquals(0, node.getMinimax());
    assertEquals(1, node.getDepth());
    assertEquals(move, node.getMove());
  }
}
