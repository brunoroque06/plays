package com.github.brunoroque06.decisiontreeplayer;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.State;
import com.github.brunoroque06.decisiontreeplayer.players.DecisionTreePlayer;
import com.github.brunoroque06.decisiontreeplayer.players.DummyPlayer;
import com.github.brunoroque06.decisiontreeplayer.tree.DecisionTree;
import com.github.brunoroque06.decisiontreeplayer.tree.NodeFactory;
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
