package com.github.brunoroque06.games.players.tree;

import static org.assertj.core.api.Java6Assertions.assertThat;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.CoordinateFactory;
import com.github.brunoroque06.games.tictactoe.TicTacToeGame;
import com.github.brunoroque06.games.tictactoe.TicTacToePieceFactory;
import org.junit.jupiter.api.Test;

class TreeTest {

  @Test
  void Play2ConsecutiveMovesThatWin() {
    final var board = new Board<>(3, 3, new TicTacToePieceFactory());
    board.playMove(new Coordinate(2, 0));
    board.playMove(new Coordinate(1, 0));
    final var tree = new Tree<>(new LeafsFactory<>(), new TicTacToeGame(new CoordinateFactory()));

    final var move = tree.findBestMove(board, 5);

    assertThat(move).isEqualToComparingFieldByField(new Coordinate(2, 2));
    board.playMove(move);
    board.playMove(new Coordinate(2, 1));
    final var secondMove = tree.findBestMove(board, 3);
    assertThat(secondMove).isEqualToComparingFieldByField(new Coordinate(1, 1));
  }
}
