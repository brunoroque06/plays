// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System

// Define a function to construct a message to print
let from whom = $"from %s{whom}\n"

let m = from "Bruno"
printf $"%s{m}"

let sampleFunction1 x = x * x + 3
let tuple1 = (1, 2, 3)

[<EntryPoint>]
let main argv =
    let message = from "F#" // Call the function
    printfn $"Hello world %s{message}"
    0 // return an integer exit code
