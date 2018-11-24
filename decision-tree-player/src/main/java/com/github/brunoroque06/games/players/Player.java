package com.github.brunoroque06.games.players;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Coordinate;
import com.github.brunoroque06.games.board.Piece;

public interface Player<T extends Piece> {
  Coordinate chooseMove(Board<T> board);
}
