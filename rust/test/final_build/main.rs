// main
mod pomodoro;

use self::pomodoro::Pomodoro;


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
