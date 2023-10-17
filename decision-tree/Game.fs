module Game

open Board

type Position =
    | Playing
    | XWon
    | Draw
    | OWon

let files = Array.map (fun s -> Array.map ((+) s) [| 0..2 |]) [| 0; 3; 6 |]
let ranks = Array.map (fun s -> Array.map ((+) s) [| 0; 3; 6 |]) [| 0; 1; 2 |]
let diags = [| [| 0; 4; 8 |]; [| 2; 4; 6 |] |]
let combs = Array.concat [| files; ranks; diags |]

let private samePiece board =
    Array.map (Array.map (getPiece board)) combs
    |> Array.filter (fun f ->
        Option.isSome f[0]
        && Option.isSome f[1]
        && Option.isSome f[2])
    |> Array.tryFind (fun f ->
        Array.pairwise f
        |> Array.forall (fun (a, b) -> a.Value = b.Value))
    |> Option.map Array.head

let evaluatePosition board =
    let piece = samePiece board

    match piece with
    | Some p ->
        match p with
        | Some X -> XWon
        | _ -> OWon
    | _ ->
        if (isBoardFull board) then
            Draw
        else
            Playing
