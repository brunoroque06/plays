module Player

open Board
open Game

let pickDummyMove rand _ board =
    let moves = legalMoves board
    Array.length moves |> rand |> Array.get moves

[<Struct>]
type Leaf =
    { Piece: Piece
      Move: int
      Position: Position }

let bestLeaf leaves =
    let findWin position =
        Array.sortBy
            (fun l ->
                let res =
                    match l.Position with
                    | p when p = position -> 0
                    | Draw -> 1
                    | Playing -> 2
                    | _ -> 3

                res * 10 + l.Move)
            leaves
        |> Array.head

    match leaves[0].Piece with
    | Cross -> findWin CrossWon
    | _ -> findWin NoughtWon

let pickDecisionTreeMove depth piece board =
    let rec revolveLeaf depth piece board move =
        let board' = playMove piece board move
        let position = evaluatePosition board'

        if (depth > 0 && position = Playing) then
            legalMoves board'
            |> Array.map (revolveLeaf (depth - 1) (switchPiece piece) board')
            |> bestLeaf
            |> fun l ->
                { Piece = piece
                  Move = move
                  Position = l.Position }
        else
            { Piece = piece
              Move = move
              Position = position }

    match isBoardEmpty board with
    | true -> 4
    | _ ->
        legalMoves board
        |> Array.map (revolveLeaf (depth - 1) piece board)
        |> bestLeaf
        |> fun l -> l.Move
