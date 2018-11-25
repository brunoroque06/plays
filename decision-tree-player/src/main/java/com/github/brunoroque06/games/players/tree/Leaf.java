package com.github.brunoroque06.games.players.tree;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.Piece;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Leaf<T extends Piece> {

  private final Board<T> board;
  private final List<Leaf<T>> leafs;
  private final Coordinate move;
  private float evaluation;

  Leaf(final Board<T> board) {
    this(board, null);
  }

  Leaf(final Board<T> board, final Coordinate move) {
    this.board = board;
    leafs = new ArrayList<>();
    this.move = move;
  }

  void addLeaf(final Leaf<T> leaf) {
    leafs.add(leaf);
  }

  Board<T> getBoard() {
    return board;
  }

  void updateEvaluation() {
    if (board.getToMove().isWhite()) {
      evaluation =
          leafs
              .stream()
              .map(Leaf::getEvaluation)
              .max(Comparator.comparing(Float::valueOf))
              .orElse(0F);
    } else {
      evaluation =
          leafs
              .stream()
              .map(Leaf::getEvaluation)
              .min(Comparator.comparing(Float::valueOf))
              .orElse(0F);
    }
  }

  float getEvaluation() {
    return evaluation;
  }

  void setEvaluation(final float evaluation) {
    this.evaluation = evaluation;
  }

  Coordinate findBestLeaf() {
    if (board.getToMove().isWhite()) {
      return leafs.stream().reduce((p, c) -> p.evaluation > c.evaluation ? p : c).get().move;
    }
    return leafs.stream().reduce((p, c) -> p.evaluation > c.evaluation ? c : p).get().move;
  }
}
