use rand::prelude::ThreadRng;
use rand::Rng;

pub(crate) struct Rnd {
    seed: ThreadRng,
}

impl Rnd {
    pub(crate) fn new() -> Rnd {
        Rnd {
            seed: rand::thread_rng(),
        }
    }

    pub(crate) fn random(&mut self) -> f64 {
        self.seed.random()
    }
}
