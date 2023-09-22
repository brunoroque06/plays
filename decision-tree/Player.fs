module Player

open Board
open Game

let dummyMoveStrategy rnd _ board =
    let moves = legalMoves board
    Array.length moves |> rnd |> Array.get moves

[<Struct>]
type Leaf =
    { Piece: Piece
      Move: int
      Position: Position }

let bestLeaf leaves =
    let findWin pos =
        Array.sortBy
            (fun l ->
                let res =
                    match l.Position with
                    | p when p = pos -> 0
                    | Draw -> 1
                    | Playing -> 2
                    | _ -> 3

                res * 10 + l.Move)
            leaves
        |> Array.head

    match leaves[0].Piece with
    | X -> findWin XWon
    | _ -> findWin OWon

let decisionTreeStrategy depth piece board =
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
