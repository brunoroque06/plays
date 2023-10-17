module PlayerTest

open Board
open Player
open Xunit

[<Fact>]
let ``Pick dummy move with empty board`` () =
    let board = buildEmptyBoard
    let rand _ = 0
    let move = dummyMoveStrategy rand Piece.O board
    Assert.Equal(0, move)

[<Fact>]
let ``Pick dummy move with non empty board`` () =
    let board = List.fold (playMove Piece.X) buildEmptyBoard [ 0..3 ]
    let rand _ = 0
    let move = dummyMoveStrategy rand Piece.O board
    Assert.Equal(4, move)

[<Fact>]
let ``Decision tree picks center move with empty board`` () =
    let board = buildEmptyBoard
    let move = decisionTreeStrategy 1 Piece.O board
    Assert.Equal(4, move)

[<Fact>]
let ``Decision tree picks winning moves`` () =
    let board =
        buildEmptyBoard
        |> fun b -> playMove Piece.X b 2
        |> fun b -> playMove Piece.O b 1

    let move = decisionTreeStrategy 5 Piece.X board
    Assert.Equal(4, move)

    let board' =
        playMove Piece.X board move
        |> fun b -> playMove Piece.O b 6

    let move = decisionTreeStrategy 3 Piece.X board'
    Assert.Equal(5, move)

[<Fact>]
let ``Decision tree picks defensive move`` () =
    let board = buildEmptyBoard |> fun b -> playMove Piece.X b 4

    let move = decisionTreeStrategy 6 Piece.O board
    Assert.Equal(0, move)
