module Referee

type Position =
    | Playing
    | CrossWon
    | NoughtWon
    | Draw

let private sup = 1

let evaluatePosition board =
    let combs =
        [| [| 0 .. 2 |]; [| 1; 4; 7 |] |]
        |> Array.collect (fun c -> Array.map (fun i -> Array.map ((+) i) c) [| 0; 3; 6 |])
        |> Array.append [| [| 0; 4; 8 |]
                           [| 2; 4; 6 |] |]

    Position.Draw
