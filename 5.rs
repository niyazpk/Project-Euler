// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

fn main () {
    let mut x = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19;  // all the prime numbers less than 20
    x = x * 2 * 2 * 2 * 3;  // 16 has 4 2s and 9 has 3 3s
    println!("{} {}", x, x == 232792560);
}

