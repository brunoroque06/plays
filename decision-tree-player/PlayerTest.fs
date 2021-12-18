module PlayerTest

open NUnit.Framework

open Board
open Player

[<Test>]
let pickDummyMoveWithEmptyBoard () =
    let board = createBoard
    let rand _ = 0
    let move = pickDummyMove rand board
    Assert.AreEqual(0, move)

[<Test>]
let pickDummyMoveWithNonEmptyBoard () =
    let playCross = playMove Piece.Cross

    let board =
        List.fold (fun b i -> playCross i b) createBoard [ 0 .. 3 ]

    let rand _ = 0
    let move = pickDummyMove rand board
    Assert.AreEqual(4, move)
