extern crate actix;

use actix::{Actor, Context, System};

struct MyActor;

impl Actor for MyActor {
    type Context = Context<Self>;

    fn started(&mut self, _ctx: &mut Self::Context) {
        println!("I am alive!");
        System::current().stop(); // <- stop system
    }
}

fn main() {
    let system = System::new("test");

    MyActor.start();

    system.run().expect("Something went wrong");
}
