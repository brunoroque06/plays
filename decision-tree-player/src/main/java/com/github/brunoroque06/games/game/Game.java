package com.github.brunoroque06.games.game;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Piece;

public interface Game<T extends Piece> {

  float evaluatePosition(Board<T> boar);

  boolean isOver(Board<T> board);

  GameResult getResult(Board<T> board);
}
