use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess The Number");

    let comp = rand::thread_rng().gen_range(1..=100);

    println!("The Computer has generated {comp} as its random number");

    println!("Enter the Number which You Guess");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess).expect("Failed to read the line");

    println!("Your Guess: {guess}");

    let guess : u32 = guess.trim().parse().expect("Please Enter a Valid Number");

    match  guess.cmp(&comp) {
        Ordering::Less => println!("Too Small"),
        Ordering::Equal => println!("You won"),
        Ordering::Greater => println!("Too Big")
    }
}
