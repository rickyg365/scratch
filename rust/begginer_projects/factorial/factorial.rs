// Factorial Program
use std::io;  // <-- read in user input
use std::io::Write;  // <-- bring flush() into scope

// Function to flush std buffer
fn no_new_line() {
    io::stdout().flush().unwrap();  // flush std
}

fn factorial (num: u128) -> u128 {
    // Initialize product as 1
    let mut product = 1;

    // Loop from 2(inclusive) to the num + 1(exclusive)
    for i in 2..num+1 {
        product = product * i;  // new product is equal to the product times the current i
    }
    product
}

fn main() {
    let mut user_input = String::new();

    // Prompt user for input, remove new line using print! and flushing std(no_new_line)
    print!("Input a number: ");  
    no_new_line();

    // Read in user input
    io::stdin()
        .read_line(&mut user_input)
        .expect("Failed to read line");

    let user_input: u128 = user_input.trim().parse::<u128>().expect("Please give a valid number!");  // parses user input from string into u128

    let f_output = factorial(user_input);

    // Print results
    println!("You inputed {}! -> {}", user_input, f_output);
}
