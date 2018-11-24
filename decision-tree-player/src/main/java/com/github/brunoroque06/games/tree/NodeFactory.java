package com.github.brunoroque06.games.tree;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Square;

public class NodeFactory {
  Node instantiateRoot(final Board board) {
    return new Node(board);
  }

  Node instantiateNode(final Board board, final Square move, final Node parent) {
    return new Node(board, move, parent);
  }
}
