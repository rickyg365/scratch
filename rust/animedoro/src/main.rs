// anime_doro
extern crate chrono;

use std::io::{stdin, stdout, Write};
use std::{thread, time};
use std::time::Instant;

use chrono::Local;


fn get_input(display_text: &str) -> String {
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


fn sec_to_min(unparsed_time: u32) -> (u32, u32) {
    let mut minutes = 0;
    let seconds = unparsed_time % 60;
    
    if unparsed_time > 60 {
        minutes = (unparsed_time - seconds)/60;
    }
    (minutes, seconds)
}


fn run_timer(title: &str, time_interval: u32) -> () {
    // Run a Timer
    let seconds = time_interval * 60;
    let mut current_elapsed;

    for i in 1..seconds+1 {
        
        current_elapsed = i;
        if i > 60 {
            let (minute, second) = sec_to_min(current_elapsed);
            print!("\r[ {} ]:  {:02}:{:02}", title, minute, second);
        } else {
            print!("\r[ {} ]:  00:{:02}", title, current_elapsed)
        }
        // Sleep for 1 sec
        thread::sleep(time::Duration::from_secs(1));
        stdout().flush().unwrap();
    }
    println!("");
}

fn main() {
    let start_time = Local::now();
    let reference_time = Instant::now();

    // std::process::Command::new("cls").status().expect("process failed to execute");


    println!("\n[ Session Start ]:   {}\n", start_time.format("%Y-%m-%d %I:%M %p"));

    let work_time = 15;
    let anime_time = 15;
    let long_break = 35;

    let cycles = 4;
    let mut current_cycle = 1;

    loop {
        if current_cycle == cycles {
            // run long break
            run_timer("Work Time", work_time);
            run_timer("Long Break", long_break);

            // Continue timer (user input)
            let u_input = get_input("Continue?");

            if u_input == "q" || u_input == "n" {
                break;
            }
            current_cycle = 1;
            continue;
        }
        // Regular Cycle
        run_timer("Work Time", work_time);
        run_timer("Anime Time", anime_time);
        println!("");
        current_cycle = current_cycle + 1;
    }
    let session_total = reference_time.elapsed();
    let finish_time = Local::now();

    println!("\n[ Session Finished ]: {}\n", finish_time.format("%Y-%m-%d %I:%M %p"));
    println!(" Total Session Time: {:.0?}\n", session_total);
}



