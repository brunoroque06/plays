package com.github.brunoroque06.decisiontreeplayer.tree;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.State;
import org.junit.jupiter.api.Test;

class NodeTest {
  @Test
  void RootNodeConstructor() {
    final Board boardMock = mock(Board.class);

    final Node root = new Node(boardMock);

    assertNull(root.getMove());
    assertEquals(0, root.getMinimax());
    assertEquals(0, root.getDepth());
  }

  @Test
  void GivenXToPlay_WhenXHasWon_ThenMinimaxOf1() {
    final Board boardMock = mock(Board.class);
    final State stateMock = mock(State.class);
    when(stateMock.hasXWon()).thenReturn(true);
    when(stateMock.isXTurn()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(stateMock);
    final Node node = new Node(boardMock);

    node.estimateMinimax(stateMock);

    assertEquals(1, node.getMinimax());
  }

  @Test
  void GivenOToPlay_WhenOHasWon_ThenMinimaxOf1() {
    final Board boardMock = mock(Board.class);
    final State stateMock = mock(State.class);
    when(stateMock.hasOWon()).thenReturn(true);
    when(stateMock.isOTurn()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(stateMock);
    final Node node = new Node(boardMock);

    node.estimateMinimax(stateMock);

    assertEquals(1, node.getMinimax());
  }

  @Test
  void GivenXToPlay_WhenOHasWon_ThenMinimaxOfMinus1() {
    final Board boardMock = mock(Board.class);
    final State nodeStateMock = mock(State.class);
    when(nodeStateMock.hasOWon()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(nodeStateMock);
    final Node node = new Node(boardMock);

    final State rootStateMock = mock(State.class);
    when(rootStateMock.isXTurn()).thenReturn(true);

    node.estimateMinimax(rootStateMock);

    assertEquals(-1, node.getMinimax());
  }

  @Test
  void GivenOToPlay_WhenXHasWon_ThenMinimaxOfMinus1() {
    final Board boardMock = mock(Board.class);
    final State nodeStateMock = mock(State.class);
    when(nodeStateMock.hasXWon()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(nodeStateMock);
    final Node node = new Node(boardMock);

    final State rootStateMock = mock(State.class);
    when(rootStateMock.isOTurn()).thenReturn(true);

    node.estimateMinimax(rootStateMock);

    assertEquals(-1, node.getMinimax());
  }

  @Test
  void MinimaxOf0WhenTheGameIsDrawn() {
    final Board boardMock = mock(Board.class);
    final State stateMock = mock(State.class);
    when(stateMock.isGameDrawn()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(stateMock);
    final Node node = new Node(boardMock);

    node.estimateMinimax(stateMock);

    assertEquals(0, node.getMinimax());
  }

  @Test
  void WhenXToPlay_ThenMinimaxOf0() {
    final Board boardMock = mock(Board.class);
    final State stateMock = mock(State.class);
    when(stateMock.isXTurn()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(stateMock);
    final Node node = new Node(boardMock);

    node.estimateMinimax(stateMock);

    assertEquals(0, node.getMinimax());
  }

  @Test
  void WhenOToPlay_ThenMinimaxOf0() {
    final Board boardMock = mock(Board.class);
    final State stateMock = mock(State.class);
    when(stateMock.isOTurn()).thenReturn(true);
    when(boardMock.getStatus()).thenReturn(stateMock);
    final Node node = new Node(boardMock);

    node.estimateMinimax(stateMock);

    assertEquals(0, node.getMinimax());
  }
}
