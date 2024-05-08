module Match

open Board
open Game

let playGame playerX playerO =
    let rec resolveGame board playerPlaying theOther piece =
        let move = playerPlaying piece board
        let board' = playMove piece board move

        match (evaluatePosition board') with
        | Position.Playing -> resolveGame board' theOther playerPlaying (switchPiece piece)
        | pos -> pos

    resolveGame buildEmptyBoard playerX playerO Piece.X

let playMatch numberGames playerX playerO =
    [| 0 .. (numberGames - 1) |] |> Array.map (fun _ -> (playGame playerX playerO))
