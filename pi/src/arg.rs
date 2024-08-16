use std::env::args;
use std::str::FromStr;

pub(crate) fn get_num<T: FromStr>(n: usize) -> Option<T> {
    args().nth(n).and_then(|a| a.parse::<T>().ok())
}
