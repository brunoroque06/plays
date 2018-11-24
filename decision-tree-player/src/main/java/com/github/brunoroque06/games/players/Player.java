package com.github.brunoroque06.games.players;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.Square;

public interface Player {
  Square chooseMove(Board board);
}
