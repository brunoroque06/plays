package com.github.brunoroque06.games.tree;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.State;
import org.junit.jupiter.api.Test;

class NodeTest {
  @Test
  void RootNodeConstructor() {
    final var board = mock(Board.class);

    final var root = new Node(board);

    assertNull(root.getMove());
    assertEquals(0, root.getMinimax());
    assertEquals(0, root.getDepth());
  }

  @Test
  void GivenXToPlay_WhenXHasWon_ThenMinimaxOf1() {
    final var board = mock(Board.class);
    final var state = mock(State.class);
    when(state.hasXWon()).thenReturn(true);
    when(state.isXTurn()).thenReturn(true);
    when(board.getStatus()).thenReturn(state);
    final var node = new Node(board);

    node.estimateMinimax(state);

    assertEquals(1, node.getMinimax());
  }

  @Test
  void GivenOToPlay_WhenOHasWon_ThenMinimaxOf1() {
    final var board = mock(Board.class);
    final var state = mock(State.class);
    when(state.hasOWon()).thenReturn(true);
    when(state.isOTurn()).thenReturn(true);
    when(board.getStatus()).thenReturn(state);
    final var node = new Node(board);

    node.estimateMinimax(state);

    assertEquals(1, node.getMinimax());
  }

  @Test
  void GivenXToPlay_WhenOHasWon_ThenMinimaxOfMinus1() {
    final var board = mock(Board.class);
    final var state = mock(State.class);
    when(state.hasOWon()).thenReturn(true);
    when(board.getStatus()).thenReturn(state);
    final var node = new Node(board);

    final var rootStateMock = mock(State.class);
    when(rootStateMock.isXTurn()).thenReturn(true);

    node.estimateMinimax(rootStateMock);

    assertEquals(-1, node.getMinimax());
  }

  @Test
  void GivenOToPlay_WhenXHasWon_ThenMinimaxOfMinus1() {
    final var board = mock(Board.class);
    final var state = mock(State.class);
    when(state.hasXWon()).thenReturn(true);
    when(board.getStatus()).thenReturn(state);
    final var node = new Node(board);

    final var rootStateMock = mock(State.class);
    when(rootStateMock.isOTurn()).thenReturn(true);

    node.estimateMinimax(rootStateMock);

    assertEquals(-1, node.getMinimax());
  }

  @Test
  void MinimaxOf0WhenTheGameIsDrawn() {
    final var board = mock(Board.class);
    final var state = mock(State.class);
    when(state.isGameDrawn()).thenReturn(true);
    when(board.getStatus()).thenReturn(state);
    final var node = new Node(board);

    node.estimateMinimax(state);

    assertEquals(0, node.getMinimax());
  }

  @Test
  void WhenXToPlay_ThenMinimaxOf0() {
    final var board = mock(Board.class);
    final var state = mock(State.class);
    when(state.isXTurn()).thenReturn(true);
    when(board.getStatus()).thenReturn(state);
    final var node = new Node(board);

    node.estimateMinimax(state);

    assertEquals(0, node.getMinimax());
  }

  @Test
  void WhenOToPlay_ThenMinimaxOf0() {
    final var board = mock(Board.class);
    final var state = mock(State.class);
    when(state.isOTurn()).thenReturn(true);
    when(board.getStatus()).thenReturn(state);
    final var node = new Node(board);

    node.estimateMinimax(state);

    assertEquals(0, node.getMinimax());
  }
}
