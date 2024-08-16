use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::Arc;

pub(crate) struct Atomic {
    val: Arc<AtomicU64>,
    ordering: Ordering,
}

impl Atomic {
    pub(crate) fn new(val: u64, ordering: Ordering) -> Atomic {
        Atomic {
            val: Arc::new(AtomicU64::new(val)),
            ordering,
        }
    }

    pub(crate) fn clone(&self) -> Atomic {
        Atomic {
            val: Arc::clone(&self.val),
            ordering: self.ordering,
        }
    }

    pub(crate) fn add(&self, val: u64) {
        self.val.fetch_add(val, self.ordering);
    }

    pub(crate) fn load(&self) -> u64 {
        self.val.load(self.ordering)
    }
}
