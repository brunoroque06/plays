package com.github.brunoroque06.games;

import com.github.brunoroque06.games.board.Board;
import com.github.brunoroque06.games.board.State;
import com.github.brunoroque06.games.players.DecisionTreePlayer;
import com.github.brunoroque06.games.players.DummyPlayer;
import com.github.brunoroque06.games.tree.DecisionTree;
import com.github.brunoroque06.games.tree.NodeFactory;
import java.util.Random;

class Main {
  public static void main(final String[] args) {
    final var numberOfGamesToPlay = 100;
    final var depth = 6;

    final var game =
        new Game(
            new Board(3, 3, new State()),
            new DummyPlayer(new Random()),
            new DecisionTreePlayer(new DecisionTree(new NodeFactory()), depth));

    new GamesRunner(game, numberOfGamesToPlay).run();
  }
}
