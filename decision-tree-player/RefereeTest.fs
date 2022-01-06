module RefereeTest

open NUnit.Framework

open Board
open Referee

[<Test>]
let evaluateOnGoingGame () =
    let p = createBoard |> evaluatePosition
    Assert.AreEqual(Position.Playing, p)
