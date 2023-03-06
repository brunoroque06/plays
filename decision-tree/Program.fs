module Program

open Match
open Player
open System

let rnd len = Random.Shared.Next(0, len)

let players =
    [| ((pickDummyMove rnd), (pickDummyMove rnd))
       ((pickDecisionTreeMove 6), (pickDummyMove rnd))
       ((pickDummyMove rnd), (pickDecisionTreeMove 6))
       ((pickDummyMove rnd), (pickDecisionTreeMove 5)) |]

for pX, pO in players do
    playMatch 100 pX pO
    |> Array.countBy id
    |> Array.sortBy fst
    |> printfn "%A"
