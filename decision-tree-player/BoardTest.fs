module BoardTest

open NUnit.Framework

open Board

[<Test>]
let testCreateBoard () =
    let l = createBoard |> Array.length
    Assert.AreEqual(9, l)
