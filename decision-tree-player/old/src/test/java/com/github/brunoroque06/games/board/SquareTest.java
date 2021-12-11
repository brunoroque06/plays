package com.github.brunoroque06.games.board;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class SquareTest {
  private final Coordinate coordinate = mock(Coordinate.class);
  private final PieceFactory<Piece> pieceFactory = mock(PieceFactory.class);
  private final Square square = new Square<>(coordinate, pieceFactory);

  @BeforeEach
  void setup() {
    when(pieceFactory.getWhite()).thenReturn(TestPiece.WHITE);
    when(pieceFactory.getBlack()).thenReturn(TestPiece.BLACK);
    when(pieceFactory.getEmpty()).thenReturn(TestPiece.EMPTY);
  }

  @Test
  void WhenPutWhite_ThenWhitePiece() {
    square.putWhite();

    assertThat(square.getPiece()).isEqualTo(TestPiece.WHITE);
    assertThat(square.getCoordinate()).isEqualTo(coordinate);
  }

  @Test
  void WhenPutBlack_ThenBlackPiece() {
    square.putBlack();

    assertThat(square.getPiece()).isEqualTo(TestPiece.BLACK);
  }

  @Test
  void WhenClear_ThenEmptyPiece() {
    square.clear();

    assertThat(square.getPiece()).isEqualTo(TestPiece.EMPTY);
    assertThat(square.isEmpty()).isTrue();
  }

  @Test
  void WhenCopy_ThenCoordinateIsReferencedAndPieceIsNot() {
    square.putBlack();
    final var newSquare = square.shallowClone();
    newSquare.putWhite();

    assertThat(square.getPiece()).isNotEqualTo(newSquare.getPiece());
    assertThat(square.getCoordinate()).isEqualTo(newSquare.getCoordinate());
  }
}
