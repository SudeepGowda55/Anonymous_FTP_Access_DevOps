use std::io;

fn main() {
    println!("Guess The Number");

    println!("Enter the Number which You Guess");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess).expect("Failed to read the line");

    println!("Your Guess: {guess}");
}
