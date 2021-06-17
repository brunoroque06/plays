// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp
module BrunoRoque06.Blockchain.Program

open System

// Define a function to construct a message to print
let from whom = $"from %s{whom}\n"

let m = from "Bruno"
printf $"%s{m}"

let sampleFunction1 x = x * x + 3
let tuple1 = (1, 2, 3)

type Message = string * AsyncReplyChannel<string>

type MessageAnother =
    | HashReport
    | Message

type HashReport =
    { Name: string
      Phone: string
      Verified: bool }

type MineMessage = { Value: string }

[<EntryPoint>]
let main argv =
    let message = from "F#" // Call the function
    printfn $"Hello world %s{message}"

    let printerAgent =
        MailboxProcessor.Start
            (fun inbox ->
                let rec messageLoop () =
                    async {
                        let! msg = inbox.Receive()
                        printfn "message is: %s" msg
                        return! messageLoop ()
                    }

                messageLoop ())

    let replyAgent =
        MailboxProcessor<Message>.Start
            (fun inbox ->
                let rec loop () =
                    async {
                        let! (message, replyChannel) = inbox.Receive()
                        replyChannel.Reply(String.Format("Received message: {0}", message))
                        do! loop ()
                    }

                loop ())

    printerAgent.Post "hello"
    printerAgent.Post "hello again"
    printerAgent.Post "hello a third time"

    let reply =
        replyAgent.PostAndReply(fun rc -> "Hello", rc)

    let miner =
        MailboxProcessor<MessageAnother>.Start
            (fun inbox ->
                let rec loop () =
                    async {
                        let! message = inbox.Receive()

//                        let! miners =
//                            [ 1 .. 100 ] 

                        return! loop ()
                    }

                loop ())


    printfn "%s" reply

    0 // return an integer exit code
