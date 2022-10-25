module Program

open Match
open Player
open System

let rnd len = Random.Shared.Next(0, len)

playMatch 100 (pickDummyMove rnd) (pickDummyMove rnd)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"

playMatch 100 (pickDecisionTreeMove 6) (pickDummyMove rnd)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"

playMatch 100 (pickDummyMove rnd) (pickDecisionTreeMove 6)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"

playMatch 100 (pickDummyMove rnd) (pickDecisionTreeMove 5)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"
