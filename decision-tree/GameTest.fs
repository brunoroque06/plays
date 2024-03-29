module GameTest

open Board
open Game
open Xunit

[<Fact>]
let ``Evaluate ongoing game`` () =
    let p = buildEmptyBoard |> evaluatePosition
    Assert.Equal(Position.Playing, p)

[<Fact>]
let ``Evaluate X win`` () =
    let p =
        buildEmptyBoard
        |> fun board -> List.fold (playMove X) board [ 0; 1; 2 ]
        |> evaluatePosition

    Assert.Equal(Position.XWon, p)

[<Fact>]
let ``Evaluate draw`` () =
    let p =
        buildEmptyBoard
        |> fun board -> List.fold (playMove X) board [ 0; 2; 3; 7; 8 ]
        |> fun board -> List.fold (playMove O) board [ 1; 4; 5; 6 ]
        |> evaluatePosition

    Assert.Equal(Position.Draw, p)
