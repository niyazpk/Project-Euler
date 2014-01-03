// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

// Find the largest palindrome made from the product of two 3-digit numbers.


// Brute force solution

fn main() {
    let mut s = 0;
    for i in range(100, 1000) {
        for j in range(100, 1000) {
            let x = i * j;
            if x == reverse(x) && x > s {
                s = x;
            }

        }
    }
    println! ("{}", s);
}

fn reverse (n: int) -> int {
    let mut x: int = n;
    let mut y: int = 0;
    while x != 0 {
        y *= 10;
        y += x % 10;
        x /= 10;
    }
    return (y).to_int();
}

// faster solution?

