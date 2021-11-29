// General Useful Functions
use std::io::{stdin, stdout, Write};


#[allow(dead_code)]
pub fn get_input(display_text: &str) -> String {
    // Display prompt to user
    print!("\n{}: ", display_text);
    stdout().flush().unwrap();
    
    // Create new string obj and read in data
    let mut buffer = String::new();
    match stdin().read_line(&mut buffer) {
        Ok(_goes_into_input_above) => {},
        Err(_no_updates_is_fine) => {},
    }
    // trim and convert data to string
    buffer.trim().to_string()
}

#[allow(dead_code)]
pub fn parse_time(unparsed_time: u32) -> (u32, u32) {
    // Seconds -> (Minutes, Seconds)
    let seconds = unparsed_time % 60;
    
    if unparsed_time > 60 {
        let minutes = (unparsed_time - seconds)/60;
        return (minutes, seconds);
    }
    (0, seconds)
}

#[allow(dead_code)]
fn test_get_input() -> u8 {
    let _test_run = get_input(">>> ");
    return 1;
}

#[allow(dead_code)]
fn test_parse_time() -> u8 {
    let _test_run = parse_time(61);
    return 1;
}
