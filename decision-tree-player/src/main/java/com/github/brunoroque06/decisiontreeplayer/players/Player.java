package com.github.brunoroque06.decisiontreeplayer.players;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.Square;

public interface Player {
  Square chooseMove(Board board);
}
