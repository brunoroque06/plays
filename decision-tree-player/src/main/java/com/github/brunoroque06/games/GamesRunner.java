package com.github.brunoroque06.games;

import com.github.brunoroque06.games.game.GameResult;
import java.util.ArrayList;
import java.util.List;

class GamesRunner {
  private final GameHandler gameHandler;
  private final int numberOfGames;
  private final List<GameResult> gameBoards;

  GamesRunner(final GameHandler gameHandler, final int numberOfGames) {
    this.gameHandler = gameHandler;
    this.numberOfGames = numberOfGames;
    gameBoards = new ArrayList<>();
  }

  void run() {
    for (var i = 0; i < numberOfGames; i++) {
      gameHandler.resetGame();
      gameBoards.add(gameHandler.playGame());
    }
    printStatistics();
  }

  private void printStatistics() {
    System.out.println("# Results Statistics:");
    System.out.println(
        "White Won: " + gameBoards.stream().filter(e -> e == GameResult.WHITE_WON).count());
    System.out.println(
        "Black Won: " + gameBoards.stream().filter(e -> e == GameResult.BLACK_WON).count());
    System.out.println("Drawn: " + gameBoards.stream().filter(e -> e == GameResult.DRAW).count());
  }
}
