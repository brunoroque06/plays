module Program

open Match
open Player
open System

let rand len = Random.Shared.Next(0, len)

playMatch 100 (pickDummyMove rand) (pickDummyMove rand)
|> List.countBy id
|> List.sortBy fst
|> Console.WriteLine
