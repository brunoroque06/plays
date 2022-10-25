module PlayerTest

open Board
open NUnit.Framework
open Player

[<Test>]
let pickDummyMoveWithEmptyBoard () =
    let board = createBoard
    let rand _ = 0
    let move = pickDummyMove rand Piece.O board
    Assert.AreEqual(0, move)

[<Test>]
let pickDummyMoveWithNonEmptyBoard () =
    let board = List.fold (playMove Piece.X) createBoard [ 0..3 ]
    let rand _ = 0
    let move = pickDummyMove rand Piece.O board
    Assert.AreEqual(4, move)

[<Test>]
let decisionTreePicksCenterMoveWithEmptyBoard () =
    let board = createBoard
    let move = pickDecisionTreeMove 1 Piece.O board
    Assert.AreEqual(4, move)

[<Test>]
let decisionTreePicksWinningMoves () =
    let board =
        createBoard
        |> fun b -> playMove Piece.X b 2
        |> fun b -> playMove Piece.O b 1

    let move = pickDecisionTreeMove 5 Piece.X board
    Assert.AreEqual(4, move)

    let board' =
        playMove Piece.X board move
        |> fun b -> playMove Piece.O b 6

    let move = pickDecisionTreeMove 3 Piece.X board'
    Assert.AreEqual(5, move)

[<Test>]
let decisionTreePicksDefensiveMove () =
    let board = createBoard |> fun b -> playMove Piece.X b 4

    let move = pickDecisionTreeMove 6 Piece.O board
    Assert.AreEqual(0, move)
