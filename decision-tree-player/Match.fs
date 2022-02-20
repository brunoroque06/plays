module Match

open Board
open Game

let playGame playerO playerX =
    let switchPiece piece =
        match piece with
        | Piece.Cross -> Piece.Nought
        | _ -> Piece.Cross

    let rec resolveGame board playerPlaying theOther piece =
        let move = playerPlaying piece board
        let board' = playMove piece board move

        match (evaluatePosition board') with
        | Position.Playing -> resolveGame board' theOther playerPlaying (switchPiece piece)
        | pos -> pos

    resolveGame (createBoard) playerO playerX Piece.Nought
