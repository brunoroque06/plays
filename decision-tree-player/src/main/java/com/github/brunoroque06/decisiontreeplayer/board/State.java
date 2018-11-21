package com.github.brunoroque06.decisiontreeplayer.board;

public class State {
  private PossibleState state;
  private Board board;

  public State() {
    this(PossibleState.XToPlay);
  }

  private State(final PossibleState state) {
    this.state = state;
  }

  public boolean isXTurn() {
    return state == PossibleState.XToPlay;
  }

  public boolean isOTurn() {
    return state == PossibleState.OToPlay;
  }

  void restart() {
    state = PossibleState.XToPlay;
  }

  Piece whichPieceToPlay() {
    return state == PossibleState.XToPlay ? Piece.X : Piece.O;
  }

  public boolean hasXWon() {
    return state == PossibleState.XWon;
  }

  public boolean hasOWon() {
    return state == PossibleState.OWon;
  }

  public boolean isGameDrawn() {
    return state == PossibleState.Drawn;
  }

  void update(final Board board) {
    this.board = board;

    checkIfGameIsWon();
    if (!isGameWonOrDrawn()) {
      state = this.board.isBoardFull() ? PossibleState.Drawn : state;
    }
    if (!isGameWonOrDrawn()) {
      nextState();
    }
  }

  void nextState() {
    state = state == PossibleState.XToPlay ? PossibleState.OToPlay : PossibleState.XToPlay;
  }

  public boolean isGameWonOrDrawn() {
    return state == PossibleState.OWon
        || state == PossibleState.XWon
        || state == PossibleState.Drawn;
  }

  private void checkIfGameIsWon() {
    for (int r = 0; r < board.getRows(); r++) {
      for (int c = 0; c < board.getCols(); c++) {
        final Square square = new Square(r, c);
        state = checkTheFourPossibleLines(square) ? checkWhoWon(square) : state;
      }
    }
  }

  private boolean checkTheFourPossibleLines(final Square square) {

    final Square topLeft = new Square(square.getRow() - 1, square.getCol() - 1);
    final Square top = new Square(square.getRow() - 1, square.getCol());
    final Square topRight = new Square(square.getRow() - 1, square.getCol() + 1);
    final Square left = new Square(square.getRow(), square.getCol() - 1);
    final Square right = new Square(square.getRow(), square.getCol() + 1);
    final Square botLeft = new Square(square.getRow() + 1, square.getCol() - 1);
    final Square bot = new Square(square.getRow() + 1, square.getCol());
    final Square botRight = new Square(square.getRow() + 1, square.getCol() + 1);

    return arePiecesEqual(left, square, right)
        || arePiecesEqual(top, square, bot)
        || arePiecesEqual(topLeft, square, botRight)
        || arePiecesEqual(botLeft, square, topRight);
  }

  private boolean arePiecesEqual(final Square square1, final Square square2, final Square square3) {

    final Piece piece1 = board.getPiece(square1.getRow(), square1.getCol());
    final Piece piece2 = board.getPiece(square2.getRow(), square2.getCol());
    final Piece piece3 = board.getPiece(square3.getRow(), square3.getCol());

    return piece1 == piece2 && piece1 == piece3 && !piece1.isDefault();
  }

  private PossibleState checkWhoWon(final Square square) {
    return board.getPiece(square) == Piece.O ? PossibleState.OWon : PossibleState.XWon;
  }

  State cloneState() {
    return new State(state);
  }

  private enum PossibleState {
    OToPlay,
    XToPlay,
    OWon,
    XWon,
    Drawn
  }
}
