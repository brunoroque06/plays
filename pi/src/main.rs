use std::sync::atomic::Ordering;

mod arg;
mod math;
mod rnd;
mod sync;
mod thread;

fn main() {
    let num_points: u64 = arg::get_num(1).unwrap_or(1e10) as u64;
    let num_threads: u8 = arg::get_num(2).unwrap_or(8);
    let num_points_per_thread = math::split_evenly(num_points, num_threads as u64);

    println!("Points: {:e}", num_points);
    println!("Threads: {}", num_threads);
    println!(
        "Points/Thread: ~{:e}",
        num_points_per_thread.first().unwrap()
    );

    let mut thread_pool = thread::ThreadPool::new(num_threads as usize);
    let in_circle = sync::Atomic::new(0, Ordering::Relaxed);

    for points in num_points_per_thread {
        let in_circle_clone = in_circle.clone();

        thread_pool.exec(move || {
            let mut rnd = rnd::Rnd::new();

            let mut ins: u64 = 0;
            for _ in 0..points {
                let x = rnd.random();
                let y = rnd.random();

                if math::in_circle(x, y) {
                    ins += 1;
                }
            }

            in_circle_clone.add(ins);
        });
    }

    thread_pool.join();

    let pi = math::calc_pi(in_circle.load(), num_points);

    println!("π: {:.6}", pi);
    println!("Δe: {:.3e}", (pi - std::f64::consts::PI).abs());
}
