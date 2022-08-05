let args = fsi.CommandLineArgs

let points =
    match (Array.length args) with
    | l when l > 1 -> args[1] |> int
    | _ -> 1_000_000

printfn $"Number of points: %d{points}"

let gen = System.Random()
let rnd = (fun () -> gen.NextDouble())

let inCircle (x, y) =
    let pit = x ** 2.0 + y ** 2.0
    pit <= 1.0

let count (ins, tot) isIn =
    let i = if isIn then ins + 1 else ins

    let t = tot + 1
    i, t

let calc (ins, tot) = 4.0 * (ins |> float) / (tot |> float)

Seq.init points (fun _ -> rnd (), rnd ())
|> Seq.map inCircle
|> Seq.fold count (0, 0)
|> calc
|> fun pi -> printfn $"π: %f{pi}"
