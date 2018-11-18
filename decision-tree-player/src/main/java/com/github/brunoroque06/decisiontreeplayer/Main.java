package com.github.brunoroque06.decisiontreeplayer;

import com.github.brunoroque06.decisiontreeplayer.board.Board;
import com.github.brunoroque06.decisiontreeplayer.board.State;
import com.github.brunoroque06.decisiontreeplayer.players.DecisionTreePlayer;
import com.github.brunoroque06.decisiontreeplayer.players.DummyPlayer;
import com.github.brunoroque06.decisiontreeplayer.tree.DecisionTree;
import com.github.brunoroque06.decisiontreeplayer.tree.NodeFactory;

class Main {
  public static void main(final String[] args) {
    final int numberOfGamesToPlay = 100;
    final int howManyMovesToCalculate = 6;

    final Game game =
        new Game(
            new Board(3, 3, new State()),
            new DummyPlayer(),
            new DecisionTreePlayer(new DecisionTree(new NodeFactory()), howManyMovesToCalculate));

    new GamesRunner(game, numberOfGamesToPlay).runGames();
  }
}
