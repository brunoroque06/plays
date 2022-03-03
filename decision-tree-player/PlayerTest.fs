module PlayerTest

open Board
open NUnit.Framework
open Player

[<Test>]
let pickDummyMoveWithEmptyBoard () =
    let board = createBoard
    let rand _ = 0
    let move = pickDummyMove rand Piece.Nought board
    Assert.AreEqual(0, move)

[<Test>]
let pickDummyMoveWithNonEmptyBoard () =
    let board = List.fold (playMove Piece.Cross) createBoard [ 0..3 ]
    let rand _ = 0
    let move = pickDummyMove rand Piece.Nought board
    Assert.AreEqual(4, move)

[<Test>]
let decisionTreePicksCenterMoveWithEmptyBoard () =
    let board = createBoard
    let move = pickDecisionTreeMove 1 Piece.Nought board
    Assert.AreEqual(4, move)

[<Test>]
let decisionTreePicksWinningMoves () =
    let board =
        createBoard
        |> fun b -> playMove Piece.Cross b 2
        |> fun b -> playMove Piece.Nought b 1

    let move = pickDecisionTreeMove 5 Piece.Nought board
    Assert.AreEqual(8, move)

    let board' =
        playMove Piece.Cross board 8
        |> fun b -> playMove Piece.Nought b 5

    let move = pickDecisionTreeMove 3 Piece.Nought board'
    Assert.AreEqual(4, move)

[<Test>]
let decisionTreePicksDefensiveMove () =
    let board = createBoard |> fun b -> playMove Piece.Cross b 4

    let move = pickDecisionTreeMove 6 Piece.Nought board
    Assert.AreEqual(0, move)
