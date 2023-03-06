module BoardTest

open Board
open Xunit

[<Fact>]
let testCreateBoard () =
    let l = createBoard |> Array.length
    Assert.Equal(9, l)

[<Fact>]
let testBoardFull () =
    let isFull =
        createBoard
        |> fun b -> List.fold (playMove X) b [ 0..8 ]
        |> isBoardFull

    Assert.True(isFull)
