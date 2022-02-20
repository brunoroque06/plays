module Program

open Match
open Player
open System

let rand _ = 0

playGame (pickDummyMove rand) (pickDummyMove rand)
|> Console.WriteLine
