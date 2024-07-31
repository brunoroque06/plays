let args = fsi.CommandLineArgs

let points =
    match (Array.length args) with
    | l when l > 1 -> args[1] |> int
    | _ -> 100_000_000

printfn $"Number of points: %d{points}"

let gen = System.Random()
let rnd = (fun () -> gen.NextDouble())

let inCircle (x, y) =
    let pit = x ** 2.0 + y ** 2.0
    pit <= 1.0

let calc (ins, tot) = 4.0 * (ins |> float) / (tot |> float)

let mutable ins, tot = (0, 0)

for i in 1..points do
    let x, y = rnd (), rnd ()
    let isIn = inCircle (x, y)
    if isIn then ins <- ins + 1
    tot <- tot + 1
    
let pi = calc (ins, tot)
printfn $"π: %f{pi}"
