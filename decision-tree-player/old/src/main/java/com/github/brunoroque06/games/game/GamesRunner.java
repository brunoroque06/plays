package com.github.brunoroque06.games.game;

import java.util.ArrayList;
import java.util.List;

public class GamesRunner {
  private final GameArbiter gameArbiter;
  private final int numberOfGames;
  private final List<GameResult> gameBoards;

  public GamesRunner(final GameArbiter gameArbiter, final int numberOfGames) {
    this.gameArbiter = gameArbiter;
    this.numberOfGames = numberOfGames;
    gameBoards = new ArrayList<>();
  }

  public void run() {
    for (var i = 0; i < numberOfGames; i++) {
      gameArbiter.resetGame();
      gameBoards.add(gameArbiter.play());
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
