module Match

open Board
open Game

let playGame playerX playerO =
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

    resolveGame createBoard playerX playerO Piece.Cross

let playMatch numberGames playerX playerO =
    [ 0 .. (numberGames - 1) ]
    |> List.map (fun _ -> (playGame playerX playerO))
