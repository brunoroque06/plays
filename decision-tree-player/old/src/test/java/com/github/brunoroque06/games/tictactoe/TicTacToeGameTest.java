package com.github.brunoroque06.games.tictactoe;

import static org.assertj.core.api.Java6Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.CoordinateFactory;
import com.github.brunoroque06.games.game.GameResult;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class TicTacToeGameTest {

  private final Coordinate zero_zero = new Coordinate(0, 0);
  private final Coordinate zero_one = new Coordinate(0, 1);
  private final Coordinate zero_two = new Coordinate(0, 2);
  private final Coordinate one_zero = new Coordinate(1, 0);
  private final Coordinate one_one = new Coordinate(1, 1);
  private final Coordinate one_two = new Coordinate(1, 2);
  private final Coordinate two_zero = new Coordinate(2, 0);
  private final Coordinate two_one = new Coordinate(2, 1);
  private final Coordinate two_two = new Coordinate(2, 2);
  private TicTacToeGame ticTacToeGame;

  @BeforeEach
  void setup() {
    final var coordinateFactory = mock(CoordinateFactory.class);
    when(coordinateFactory.create(0, 0)).thenReturn(zero_zero);
    when(coordinateFactory.create(0, 1)).thenReturn(zero_one);
    when(coordinateFactory.create(0, 2)).thenReturn(zero_two);
    when(coordinateFactory.create(1, 0)).thenReturn(one_zero);
    when(coordinateFactory.create(1, 1)).thenReturn(one_one);
    when(coordinateFactory.create(1, 2)).thenReturn(one_two);
    when(coordinateFactory.create(2, 0)).thenReturn(two_zero);
    when(coordinateFactory.create(2, 1)).thenReturn(two_one);
    when(coordinateFactory.create(2, 2)).thenReturn(two_two);
    ticTacToeGame = new TicTacToeGame(coordinateFactory);
  }

  @Test
  void GivenBoardIsFullAndNoPlayerWon_ThenGameIsDrawn() {
    final var board = mock(Board.class);
    when(board.getPiece(zero_zero)).thenReturn(TicTacToePiece.BLACK);
    when(board.getPiece(zero_one)).thenReturn(TicTacToePiece.BLACK);
    when(board.getPiece(zero_two)).thenReturn(TicTacToePiece.WHITE);
    when(board.getPiece(one_zero)).thenReturn(TicTacToePiece.WHITE);
    when(board.getPiece(one_one)).thenReturn(TicTacToePiece.WHITE);
    when(board.getPiece(one_two)).thenReturn(TicTacToePiece.BLACK);
    when(board.getPiece(two_zero)).thenReturn(TicTacToePiece.BLACK);
    when(board.getPiece(two_one)).thenReturn(TicTacToePiece.BLACK);
    when(board.getPiece(two_two)).thenReturn(TicTacToePiece.WHITE);
    when(board.isFull()).thenReturn(true);

    assertTrue(ticTacToeGame.isOver(board));
    assertThat(ticTacToeGame.evaluatePosition(board)).isEqualTo(0);
    assertThat(ticTacToeGame.getResult(board)).isEqualTo(GameResult.DRAW);
  }

  @Test
  void GivenWhiteHasWon_ThenGameIsOver() {
    final var board = mock(Board.class);
    when(board.getPiece(zero_zero)).thenReturn(TicTacToePiece.WHITE);
    when(board.getPiece(zero_one)).thenReturn(TicTacToePiece.WHITE);
    when(board.getPiece(zero_two)).thenReturn(TicTacToePiece.WHITE);
    when(board.isFull()).thenReturn(false);

    assertTrue(ticTacToeGame.isOver(board));
    assertThat(ticTacToeGame.evaluatePosition(board)).isEqualTo(Float.POSITIVE_INFINITY);
    assertThat(ticTacToeGame.getResult(board)).isEqualTo(GameResult.WHITE_WON);
  }

  @Test
  void GivenBlackHasWon_ThenGameIsOver() {
    final var board = mock(Board.class);
    when(board.getPiece(zero_zero)).thenReturn(TicTacToePiece.BLACK);
    when(board.getPiece(one_one)).thenReturn(TicTacToePiece.BLACK);
    when(board.getPiece(two_two)).thenReturn(TicTacToePiece.BLACK);
    when(board.isFull()).thenReturn(false);

    assertTrue(ticTacToeGame.isOver(board));
    assertThat(ticTacToeGame.evaluatePosition(board)).isEqualTo(Float.NEGATIVE_INFINITY);
    assertThat(ticTacToeGame.getResult(board)).isEqualTo(GameResult.BLACK_WON);
  }
}
