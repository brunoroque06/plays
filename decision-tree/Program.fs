module Program

open Match
open Player
open System

let rnd len = Random.Shared.Next(0, len)

let players =
    [| ((dummyMoveStrategy rnd), (dummyMoveStrategy rnd))
       ((dummyMoveStrategy rnd), (decisionTreeStrategy 5))
       ((dummyMoveStrategy rnd), (decisionTreeStrategy 6))
       ((decisionTreeStrategy 6), (dummyMoveStrategy rnd)) |]

for pX, pO in players do
    playMatch 100 pX pO
    |> Array.countBy id
    |> Array.sortBy fst
    |> printfn "%A"
