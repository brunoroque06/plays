module TicTacToe

type Piece =
    | Empty
    | Cross
    | Nought

let piece2Char piece =
    match piece with
    | Empty -> ' '
    | Cross -> 'X'
    | Nought -> 'O'

let createBoard =
    [| 0 .. 8 |] |> Array.map (fun _ -> Piece.Empty)

let printChar col piece =
    match col with
    | 2 -> printfn $" %c{piece}\n-----------"
    | _ -> printf $" %c{piece} |"

let printBoard board =
    board
    |> Array.map piece2Char
    |> Array.chunkBySize 3
    |> Array.iter (Array.iteri printChar)
