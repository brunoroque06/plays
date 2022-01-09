module RefereeTest

open NUnit.Framework

open Board
open Referee

[<Test>]
let evaluateOnGoingGame () =
    let p = createBoard |> evaluatePosition
    Assert.AreEqual(Position.Playing, p)

[<Test>]
let evaluateCrossWin () =
    let p =
        createBoard
        |> fun board -> List.fold (fun b i -> playMove Cross i b) board [ 0; 1; 2 ]
        |> evaluatePosition

    Assert.AreEqual(Position.CrossWon, p)
