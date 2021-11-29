// pomodoro
#[path = "general.rs"]
mod general;

#[path = "timer.rs"]
mod timer;

// extern crate chrono;
// use chrono::Local;

use self::general::{ get_input, parse_time };
use self::timer::Timer;

use std::time::Instant;
use std::fmt::{self,Formatter, Display};


// Pomodoro Object
pub struct Pomodoro {
    pub session_name: String,
    pub work_time: u32,
    pub short_break: u32,
    pub long_break: u32,

    pub cycles: u8,
}

impl Pomodoro {
    pub fn start(&self) {
        // let start_time = Local::now();
        let reference_time = Instant::now();

        // println!("\n[ {} ]:   \n", self.session_name, start_time.format("%Y-%m-%d %I:%M %p"));
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
        // let finish_time = Local::now();
        let session_total = reference_time.elapsed();

        let (final_min, final_sec) = parse_time(session_total.as_secs() as u32);

        // println!("\n[ {} Done ]: {}\n", self.session_name, finish_time.format("%Y-%m-%d %I:%M %p"));
        println!("\n[ Total Session Time ]: \n");
        println!(" Total Session Time: {:02} min. {:02} sec.\n", final_min, final_sec);
    }
}

impl Display for Pomodoro {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "\rSession: {} -> {} min | {} min | {} min | cycles-{}", self.session_name, self.work_time, self.short_break, self.long_break, self.cycles)
    }
}
