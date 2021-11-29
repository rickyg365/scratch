// sec
// anime_doro
extern crate chrono;

use std::io::{stdin, stdout, Write};
use std::{thread, time};
use std::time::Instant;
use std::fmt::{self,Formatter, Display};

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


// fn run_timer(title: &str, time_interval: u32) -> () {
//     // Run a Timer
//     let seconds = time_interval * 60;
//     let mut current_elapsed;

//     for i in 1..seconds+1 {
        
//         current_elapsed = i;
//         if i > 60 {
//             let (minute, second) = sec_to_min(current_elapsed);
//             print!("\r[ {} ]:  {:02}:{:02}", title, minute, second);
//         } else {
//             print!("\r[ {} ]:  00:{:02}", title, current_elapsed)
//         }
//         // Sleep for 1 sec
//         thread::sleep(time::Duration::from_secs(1));
//         stdout().flush().unwrap();
//     }
//     println!("");
// }


struct Timer {
    // Timer Text
    title: &str,
    // Timer Duration
    time_interval: u32,
}

impl Timer {
    fn prettify_time(&self, current_time: u32) -> (u32, u32) {
        if current_time > 60 {
            let (minute, second) = sec_to_min(current_time);
            return (minute, second);
        }
        return (0, current_time);
    }
}

impl Timer {
    fn run(&self) {
        // Run a Timer
        let seconds = time_interval * 60;
        let mut current_elapsed;

        for i in 1..seconds+1 {
            
            current_elapsed = i;
            // if i > 60 {
            //     let (minute, second) = sec_to_min(current_elapsed);
            //     print!("\r[ {} ]:  {:02}:{:02}", title, minute, second);
            // } else {
            //     print!("\r[ {} ]:  00:{:02}", title, current_elapsed)
            // }
            current_elapsed_fmt = Timer.prettify_time(i);
            let (min, sec) = current_elapsed_fmt;
            print!("\r[ {} ]:  {:02}:{:02}", title, min, sec);

            // Sleep for 1 sec
            thread::sleep(time::Duration::from_secs(1));
            stdout().flush().unwrap();
        }
        println!("");
    }
}

impl Display for Timer {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let (min, sec) = self.prettify_time(self.time_interval);

        print!("\r[ {} ]:  {:02}:{:02}", title, min, sec);
    }
}


fn main() {
    let start_time = Local::now();
    let reference_time = Instant::now();

    // std::process::Command::new("cls").status().expect("process failed to execute");

    println!("\n[ Session Start ]:   {}\n", start_time.format("%Y-%m-%d %I:%M %p"));

    let work_time = 5;
    let anime_time = 5;
    let long_break = 8;

    let cycles = 4;
    let mut current_cycle = 1;

    // Work Timer
    let work_timer = Timer("Work Time", work_time);

    // Play Timer
    let play_timer = Timer("Anime Time", anime_time);
    
    // Long Timer
    let long_timer = Timer("Long Break", long_break);

    loop {
        if current_cycle == cycles {
            // run long break
            // run_timer("Work Time", work_time);
            // run_timer("Long Break", long_break);
            work_timer.run();
            long_timer.run();

            // Continue timer (user input)
            let u_input = get_input("Continue?");

            if u_input == "q" || u_input == "n" {
                break;
            }
            current_cycle = 1;
            continue;
        }
        // Regular Cycle
        // run_timer("Work Time", work_time);
        // run_timer("Anime Time", anime_time);
        work_timer.run();
        play_timer.run();

        println!("");
        current_cycle = current_cycle + 1;
    }
    let session_total = reference_time.elapsed();
    let finish_time = Local::now();

    println!("\n[ Session Finished ]: {}\n", finish_time.format("%Y-%m-%d %I:%M %p"));
    println!(" Total Session Time: {:.0?}\n", session_total);
}



