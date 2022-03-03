module Program

open Match
open Player
open System

let rand len = Random.Shared.Next(0, len)

playMatch 100 (pickDummyMove rand) (pickDummyMove rand)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"

playMatch 100 (pickDecisionTreeMove 6) (pickDummyMove rand)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"

playMatch 100 (pickDummyMove rand) (pickDecisionTreeMove 6)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"

playMatch 100 (pickDummyMove rand) (pickDecisionTreeMove 5)
|> Array.countBy id
|> Array.sortBy fst
|> printfn "%A"
