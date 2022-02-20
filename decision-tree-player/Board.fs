module Board

type Piece =
    | Cross
    | Nought

let createBoard: Piece option [] = [| 0..8 |] |> Array.map (fun _ -> None)

let private piece2Char piece =
    match piece with
    | Some p ->
        match p with
        | Cross -> 'X'
        | Nought -> 'O'
    | None -> ' '

let private printChar col piece =
    match col with
    | 2 -> printfn $" %c{piece}\n-----------"
    | _ -> printf $" %c{piece} |"

let printBoard board =
    board
    |> Array.map piece2Char
    |> Array.chunkBySize 3
    |> Array.iter (Array.iteri printChar)

let playMove piece board idx = Array.updateAt idx (Some piece) board

let getPiece board idx = Array.get board idx

let isBoardFull board =
    match Array.tryFind Option.isNone board with
    | Some _ -> false
    | None -> true
