// anime_doro

use std::io::{stdin, stdout, Write};
use std::{thread, time};
use std::time::Instant;
use std::fmt::{self,Formatter, Display};


// General Useful Functions
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


fn parse_time(unparsed_time: u32) -> (u32, u32) {
    // Seconds -> (Minutes, Seconds)
    let seconds = unparsed_time % 60;
    
    if unparsed_time > 60 {
        let minutes = (unparsed_time - seconds)/60;
        return (minutes, seconds);
    }
    (0, seconds)
}


// Timer Objects & Functions
struct Timer {
    // Title and Duration
    title: String,
    time_interval: u32,
}

impl Timer {
    fn run(&self) {
        // Run a Timer
        for i in 1..self.time_interval+1 {
            let (min, sec) = parse_time(i);
            print!("\r[ {} ]:  {:02}:{:02}", self.title, min, sec);

            // Sleep for 1 sec
            thread::sleep(time::Duration::from_secs(1));
            stdout().flush().unwrap();
        }
        println!("");
    }
}

impl Display for Timer {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let (min, sec) = parse_time(self.time_interval);

        write!(f, "\r[ {} ]:  {:02}:{:02}", self.title, min, sec)
    }
}


// Pomodoro Object
struct Pomodoro {
    session_name: String,
    work_time: u32,
    short_break: u32,
    long_break: u32,

    cycles: u8,
}

impl Pomodoro {
    fn start(&self) {
        // let start_time = Local::now();
        let reference_time = Instant::now();

        println!("\n[ {} ]:   \n", self.session_name);

        let mut current_cycle = 1;

        // Create Timers 
        let work_timer = Timer{ title: "Work Time".to_string(), time_interval: self.work_time };
        let play_timer = Timer{ title: "Anime Time".to_string(), time_interval: self.short_break };
        let long_timer = Timer{ title: "Long Break".to_string(), time_interval: self.long_break };

        loop {
            if current_cycle == self.cycles {
                // run long break
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
            work_timer.run();
            play_timer.run();

            println!("");
            current_cycle = current_cycle + 1;
        }
        let session_total = reference_time.elapsed();

        let (final_min, final_sec) = parse_time(session_total.as_secs() as u32);

        println!("\n[ Total Session Time ]: \n");
        println!(" Total Session Time: {:02} min. {:02} sec.\n", final_min, final_sec);
    }
}

impl Display for Pomodoro {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "\rSession: {} -> {} min | {} min | {} min | cycles-{}", self.session_name, self.work_time, self.short_break, self.long_break, self.cycles)
    }
}


fn main() {
    let session1 = Pomodoro{
        session_name: "Morning".to_string(),
        work_time: 5,
        short_break: 5,
        long_break: 15,
        cycles: 4,
    };
    println!("{}", session1);
    session1.start();
}