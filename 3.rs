// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143 ?

// Simple solution

use std::num::sqrt;
use std::iter::range_step;

fn is_prime(n: int) -> bool {
    if n % 2 == 0 {
        return false;
    }
    
    let till = sqrt(n as float) as int + 1;
    for i in range_step(3, till, 2) {
        if n % i == 0 {
            return false;
        }
    }
    return true;
}

fn main() {

    let n = 600851475143;
    let mut factors: ~[int] = ~[];

    let till = sqrt(n as float) as int;

    for i in range_step(3, till, 2) {
        if is_prime(i) && (n % i == 0) {
            factors.push(i);
            if is_prime( n / i ) {
                factors.push( n / i );
            }
        }
    }

    for &x in factors.iter() {
        println!("{}", x);
    }
}

