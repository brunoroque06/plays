module BoardTest

open Board
open NUnit.Framework

[<Test>]
let testCreateBoard () =
    let l = createBoard |> Array.length
    Assert.AreEqual(9, l)

[<Test>]
let testBoardFull () =
    let isFull =
        createBoard
        |> fun b -> List.fold (playMove Cross) b [ 0..8 ]
        |> isBoardFull

    Assert.IsTrue(isFull)
