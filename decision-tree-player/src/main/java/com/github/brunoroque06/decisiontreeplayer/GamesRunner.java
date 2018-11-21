package com.github.brunoroque06.decisiontreeplayer;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import java.util.ArrayList;
import java.util.List;

class GamesRunner {
  private final Game game;
  private final int numberOfGames;
  private final List<Board> gameBoards;

  GamesRunner(final Game game, final int numberOfGames) {
    this.game = game;
    this.numberOfGames = numberOfGames;
    gameBoards = new ArrayList<>();
  }

  List<Board> getGameResults() {
    return gameBoards;
  }

  void run() {
    for (var i = 0; i < numberOfGames; i++) {
      game.resetGame();
      gameBoards.add(game.process());
    }
    printStatistics();
  }

  private void printStatistics() {
    System.out.println("# Results Statistics:");
    System.out.println(
        "X Won: " + gameBoards.stream().filter(e -> e.getStatus().hasXWon()).count());
    System.out.println(
        "O Won: " + gameBoards.stream().filter(e -> e.getStatus().hasOWon()).count());
    System.out.println(
        "Drawn: " + gameBoards.stream().filter(e -> e.getStatus().isGameDrawn()).count());
  }
}
