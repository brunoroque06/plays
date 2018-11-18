package com.github.brunoroque06.decisiontreeplayer.tree;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;

public class NodeFactory {
  Node instantiateRoot(final Board board) {
    return new Node(board);
  }

  Node instantiateNode(final Board board, final Square move, final Node parent) {
    return new Node(board, move, parent);
  }
}
