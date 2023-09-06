module PlayerFact

open Board
open Player
open Xunit

[<Fact>]
let ``Pick dummy move with empty board`` () =
    let board = createBoard
    let rand _ = 0
    let move = pickDummyMove rand Piece.O board
    Assert.Equal(0, move)

[<Fact>]
let ``Pick dummy move with non empty board`` () =
    let board = List.fold (playMove Piece.X) createBoard [ 0..3 ]
    let rand _ = 0
    let move = pickDummyMove rand Piece.O board
    Assert.Equal(4, move)

[<Fact>]
let ``Decision tree picks center move with empty board`` () =
    let board = createBoard
    let move = pickDecisionTreeMove 1 Piece.O board
    Assert.Equal(4, move)

[<Fact>]
let ``Decision tree picks winning moves`` () =
    let board =
        createBoard
        |> fun b -> playMove Piece.X b 2
        |> fun b -> playMove Piece.O b 1

    let move = pickDecisionTreeMove 5 Piece.X board
    Assert.Equal(4, move)

    let board' =
        playMove Piece.X board move
        |> fun b -> playMove Piece.O b 6

    let move = pickDecisionTreeMove 3 Piece.X board'
    Assert.Equal(5, move)

[<Fact>]
let ``Decision tree picks defensive move`` () =
    let board = createBoard |> fun b -> playMove Piece.X b 4

    let move = pickDecisionTreeMove 6 Piece.O board
    Assert.Equal(0, move)
