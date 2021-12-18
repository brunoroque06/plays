module Player

open Board

type Side =
    | Cross
    | Nought

let pickDummyMove rand board =
    let idx =
        Array.mapi (fun i s -> (i, s)) board
        |> Array.filter (fun (_, s) -> s = Piece.Empty)
        |> Array.map fst

    Array.length idx |> rand |> Array.get idx
