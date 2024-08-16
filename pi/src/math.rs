pub(crate) fn split_evenly(num: u64, dem: u64) -> Vec<u64> {
    let floor = num / dem;
    let mut div = vec![floor; dem as usize];
    let missing = num - dem * floor;
    div[0] += missing;
    div
}

pub(crate) fn in_circle(x: f64, y: f64) -> bool {
    x * x + y * y <= 1.0
}

pub(crate) fn calc_pi(in_circle: u64, total: u64) -> f64 {
    4.0 * (in_circle as f64) / (total as f64)
}
