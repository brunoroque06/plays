module GameTest

open Board
open Game
open NUnit.Framework

[<Test>]
let evaluateOnGoingGame () =
    let p = createBoard |> evaluatePosition
    Assert.AreEqual(Position.Playing, p)

[<Test>]
let evaluateCrossWin () =
    let p =
        createBoard
        |> fun board -> List.fold (playMove Cross) board [ 0; 1; 2 ]
        |> evaluatePosition

    Assert.AreEqual(Position.CrossWon, p)

[<Test>]
let evaluateDraw () =
    let p =
        createBoard
        |> fun board -> List.fold (playMove Cross) board [ 0; 2; 3; 7; 8 ]
        |> fun board -> List.fold (playMove Nought) board [ 1; 4; 5; 6 ]
        |> evaluatePosition

    Assert.AreEqual(Position.Draw, p)
