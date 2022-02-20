module Player

type Side =
    | Cross
    | Nought

let pickDummyMove rand _ board =
    let idx =
        Array.mapi (fun i s -> (i, s)) board
        |> Array.filter (fun (_, s) -> Option.isNone s)
        |> Array.map fst

    Array.length idx |> rand |> Array.get idx
