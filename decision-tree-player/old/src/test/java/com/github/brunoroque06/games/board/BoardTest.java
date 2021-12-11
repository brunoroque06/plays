package com.github.brunoroque06.games.board;

import static org.assertj.core.api.Java6Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class BoardTest {
  private final PieceFactory<Piece> pieceFactory = mock(PieceFactory.class);

  @BeforeEach
  void setup() {
    when(pieceFactory.getWhite()).thenReturn(TestPiece.WHITE);
    when(pieceFactory.getBlack()).thenReturn(TestPiece.BLACK);
    when(pieceFactory.getEmpty()).thenReturn(TestPiece.EMPTY);
  }

  @Test
  void WhenCreateBoard_ThenBoardIsEmpty() {
    final var board = new Board<>(2, 3, pieceFactory);

    assertThat(board.getPiece(new Coordinate(0, 0))).isEqualTo(TestPiece.EMPTY);
    assertThat(board.getPiece(new Coordinate(0, 1))).isEqualTo(TestPiece.EMPTY);
    assertThat(board.getPiece(new Coordinate(0, 2))).isEqualTo(TestPiece.EMPTY);
    assertThat(board.getPiece(new Coordinate(1, 0))).isEqualTo(TestPiece.EMPTY);
    assertThat(board.getPiece(new Coordinate(1, 1))).isEqualTo(TestPiece.EMPTY);
    assertThat(board.getPiece(new Coordinate(1, 2))).isEqualTo(TestPiece.EMPTY);
    assertThat(board.isEmpty()).isTrue();
    assertThat(board.isFull()).isFalse();
  }

  @Test
  void WhenCreateBoard_ThenWhiteToPlay() {
    final var board = new Board<>(0, 0, pieceFactory);
    assertThat(board.getToMove()).isEqualTo(TestPiece.WHITE);
  }

  @Test
  void GivenEmptyBoard_WhenPlayPieces_ThenBoardIsFull() {
    final var board = new Board<>(2, 2, pieceFactory);

    board.playMove(new Coordinate(0, 0));
    board.playMove(new Coordinate(1, 1));
    board.playMove(new Coordinate(0, 1));
    board.playMove(new Coordinate(1, 0));

    assertThat(board.getPiece(new Coordinate(0, 0))).isEqualTo(TestPiece.WHITE);
    assertThat(board.getPiece(new Coordinate(1, 1))).isEqualTo(TestPiece.BLACK);
    assertThat(board.getPiece(new Coordinate(0, 1))).isEqualTo(TestPiece.WHITE);
    assertThat(board.getPiece(new Coordinate(1, 0))).isEqualTo(TestPiece.BLACK);
    assertThat(board.isFull()).isTrue();
    assertThat(board.isEmpty()).isFalse();
    assertThat(board.getToMove()).isEqualTo(TestPiece.WHITE);
  }

  @Test
  void GivenBoardWithOnePiece_WhenGetEmptyCoordinates_ThenReturnEveryOther() {
    final var board = new Board<>(2, 2, pieceFactory);
    board.playMove(new Coordinate(1, 1));

    final var emptySquares = board.getEmptyCoordinates();

    assertThat(emptySquares.get(0)).isEqualToComparingFieldByField(new Coordinate(0, 0));
    assertThat(emptySquares.get(1)).isEqualToComparingFieldByField(new Coordinate(0, 1));
    assertThat(emptySquares.get(2)).isEqualToComparingFieldByField(new Coordinate(1, 0));
  }

  @Test
  void WhenShallowClone_ThenOnlySquaresAreHardCopied() {
    final var board = new Board<>(4, 2, pieceFactory);
    final var newBoard = board.shallowClone();
    assertThat(board).isEqualToComparingFieldByFieldRecursively(newBoard);

    final var coordinate = new Coordinate(3, 1);
    newBoard.playMove(coordinate);
    assertThat(board.getPiece(coordinate)).isNotEqualTo(newBoard.getPiece(coordinate));
    assertThat(board.getToMove()).isNotEqualTo(newBoard.getToMove());
  }

  @Test
  void WhenResetBoard_ThenBoardIsEmpty() {
    final var board = new Board<>(3, 3, pieceFactory);
    board.playMove(new Coordinate(0, 0));
    assertThat(board.isEmpty()).isFalse();

    board.resetBoard();

    assertThat(board.isEmpty()).isTrue();
  }
}
