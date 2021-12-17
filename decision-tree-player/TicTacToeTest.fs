module TicTacToeTest

open NUnit.Framework
open TicTacToe

[<Test>]
let testCreateBoard () =
    let l = createBoard |> Array.length
    Assert.AreEqual(9, l)
