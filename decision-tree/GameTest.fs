module GameTest

open Board
open Game
open Xunit

[<Fact>]
let evaluateOnGoingGame () =
    let p = createBoard |> evaluatePosition
    Assert.Equal(Position.Playing, p)

[<Fact>]
let evaluateXWin () =
    let p =
        createBoard
        |> fun board -> List.fold (playMove X) board [ 0; 1; 2 ]
        |> evaluatePosition

    Assert.Equal(Position.XWon, p)

[<Fact>]
let evaluateDraw () =
    let p =
        createBoard
        |> fun board -> List.fold (playMove X) board [ 0; 2; 3; 7; 8 ]
        |> fun board -> List.fold (playMove O) board [ 1; 4; 5; 6 ]
        |> evaluatePosition

    Assert.Equal(Position.Draw, p)
