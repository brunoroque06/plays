module BoardTest

open NUnit.Framework

open Board

[<Test>]
let testCreateBoard () =
    let l = createBoard |> Array.length
    Assert.AreEqual(9, l)

[<Test>]
let testBoardFull () =
    let isFull =
        createBoard
        |> fun b -> List.fold (fun b i -> playMove Cross i b) b [ 0..8 ]
        |> isBoardFull

    Assert.IsTrue(isFull)
