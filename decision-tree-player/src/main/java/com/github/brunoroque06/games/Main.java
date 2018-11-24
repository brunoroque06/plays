package com.github.brunoroque06.games;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.players.DummyPlayer;
import com.github.brunoroque06.games.players.tree.DecisionTreePlayer;
import com.github.brunoroque06.games.players.tree.LeafsFactory;
import com.github.brunoroque06.games.players.tree.Tree;
import com.github.brunoroque06.games.tictactoe.TicTacToeGame;
import com.github.brunoroque06.games.tictactoe.TicTacToePieceFactory;
import java.util.Random;

class Main {
  public static void main(final String[] args) {
    final var numberOfGamesToPlay = 100;
    final var depth = 6;

    final var board = new Board<>(3, 3, new TicTacToePieceFactory());
    final var gameHandler =
        new GameHandler<>(
            board,
            new DummyPlayer<>(new Random()),
            new DecisionTreePlayer<>(new Tree<>(new LeafsFactory<>(), new TicTacToeGame()), depth),
            new TicTacToeGame());

    System.out.println(gameHandler.playGame());
    new GamesRunner(gameHandler, numberOfGamesToPlay).run();
  }
}
