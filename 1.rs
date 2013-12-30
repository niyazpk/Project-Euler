// If we list all the natural numbers below 10 that are multiples of 3 or 5,
// we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.
// -------------------------------------------


// Simple solution
fn simple(n: int) -> int {
   
    let mut sum = 0;

    for i in range(0, n) {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
    }

   sum
}


// Solution using arithmetic progression equations

fn sum(n: int) -> int{
   n * (n + 1) / 2
}

fn arithmetic_progression(mut n:int ) -> int {
    
    n = n - 1;

    let c3  = n / 3;
    let c5  = n / 5;
    let c15 = n / 15;

    let s3  = 3  * sum(c3);
    let s5  = 5  * sum(c5);
    let s15 = 15 * sum(c15);

    s3 + s5 - s15
}

fn main() {
   let n = 1000;
   println!("{} => {}", n, simple(n));
   println!("{} => {}", n, arithmetic_progression(n));

   for i in range(0, 5) {
     print!("{} ", i) // prints "0 1 2 3 4"
   }
}

