// Timer Objects & Functions
#[path = "general.rs"]
mod general;

use self::general::parse_time;

use std::io::{stdout, Write};
use std::{thread, time};
use std::fmt::{self,Formatter, Display};

// Timer Object
pub struct Timer {
    // Title and Duration
    pub title: String,
    pub time_interval: u32,
}

impl Timer {
    pub fn run(&self) {
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
