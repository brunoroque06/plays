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
