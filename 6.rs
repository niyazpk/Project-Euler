
// The sum of the squares of the first ten natural numbers is,

// 12 + 22 + ... + 102 = 385
// The square of the sum of the first ten natural numbers is,

// (1 + 2 + ... + 10)2 = 552 = 3025
// Hence the difference between the sum of the squares of the first ten
// natural numbers and the square of the sum is 3025  385 = 2640.

// Find the difference between the sum of the squares of the first
// one hundred natural numbers and the square of the sum.

use std::iter::AdditiveIterator;

fn sum_of_squares (n: int) -> int {
    range(1, n + 1).map(|x| x * x).sum()
}

fn square_of_sum (n: int) -> int {
    let x = range(1, n + 1).sum();
    x * x
}

fn main(){
    let x = square_of_sum(100) - sum_of_squares(100);
    println!("{} {}", x, x == 25164150);
}

