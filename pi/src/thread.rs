use std::thread;
use std::thread::JoinHandle;

pub(crate) struct ThreadPool {
    handles: Vec<JoinHandle<()>>,
}

impl ThreadPool {
    pub(crate) fn new(cap: usize) -> ThreadPool {
        ThreadPool {
            handles: Vec::with_capacity(cap),
        }
    }

    pub(crate) fn exec<F>(&mut self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let handle = thread::spawn(f);
        self.handles.push(handle);
    }

    pub(crate) fn join(&mut self) {
        for handle in self.handles.drain(..) {
            handle.join().unwrap();
        }
    }
}
