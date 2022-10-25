module Board

type Piece =
    | X
    | O

let switchPiece piece =
    match piece with
    | Piece.X -> Piece.O
    | _ -> Piece.X

let createBoard: Piece option [] = [| 0..8 |] |> Array.map (fun _ -> None)

let printBoard board =
    let piece2Char piece =
        match piece with
        | Some p ->
            match p with
            | X -> 'X'
            | O -> 'O'
        | None -> ' '

    let printChar col piece =
        match col with
        | 2 -> printfn $" %c{piece}\n-----------"
        | _ -> printf $" %c{piece} |"

    board
    |> Array.map piece2Char
    |> Array.chunkBySize 3
    |> Array.iter (Array.iteri printChar)

let legalMoves board =
    Array.mapi (fun i s -> (i, s)) board
    |> Array.filter (fun (_, s) -> Option.isNone s)
    |> Array.map fst

let playMove piece board idx = Array.updateAt idx (Some piece) board

let getPiece board idx = Array.get board idx

let isBoardEmpty board =
    match Array.tryFind Option.isSome board with
    | Some _ -> false
    | None -> true

let isBoardFull board =
    match Array.tryFind Option.isNone board with
    | Some _ -> false
    | None -> true
