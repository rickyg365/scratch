import os
from sys import prefix
import time


class Timer:
    def __init__(self, duration, prefix="", suffix="", done="Done!"):
        # Timer Variables
        self.duration = duration
        self.duration_m, self.duration_s = self.parse_seconds(self.duration) 
        # Display Options
        self.prefix = prefix
        self.suffix = suffix
        self.done = done

    def __str__(self) -> str:
        text = f"{self.prefix}00:00{self.suffix}"

    def parse_seconds(self, raw_seconds):
        """ parses raw seconds to hours/minutes/seconds note: assumes no unit lower than seconds """
        if raw_seconds < 60:
            return 0, raw_seconds
        
        raw_minutes, final_seconds = raw_seconds//60, raw_seconds%60
        # Can go to days if we want
        return raw_minutes, final_seconds

    def start(self):
        # Create Reference Time and initial Time Difference
        start_time = time.time()
        time_diff = int(time.time() - start_time)

        while time_diff < self.duration:
            # Re-calculate Time Difference, for more accurate time
            time_diff = int(time.time() - start_time)
            
            # Parse raw seconds into  minutes and seconds and create timer display
            minutes, seconds = self.parse_seconds(time_diff)
            timer = f"{minutes:02}:{seconds:02}"

            # Display Time
            print(f"{self.prefix}{timer}{self.suffix}", end='\r')

            # Pause for 1 sec, dont need to change anything til at least 1 sec passes
            time.sleep(1)

        # Display Done
        print(f"{self.prefix}{self.done}{self.suffix}")


class CountdownTimer(Timer):
    def __init__(self, duration, prefix="", suffix="", done="Done!"):
        super().__init__(duration, prefix, suffix, done)

    def start(self):
        # Create Reference Time and initial Time Difference
        start_time = time.time()
        time_diff = int(time.time() - start_time)
        
        while time_diff < self.duration:
            # Re-calculate Time Difference, for more accurate time
            time_diff = int(time.time() - start_time)            
            time_left = self.duration - time_diff 

            # Parse raw seconds into  minutes and seconds and create timer display
            minutes, seconds = self.parse_seconds(time_left)
            timer = f"{minutes:02}:{seconds:02}"

            # Display Time
            print(f"{self.prefix}{timer}{self.suffix}", end='\r')
            
            # Pause for 1 sec, dont need to change anything til at least 1 sec passes
            time.sleep(1)

            # So it stops more accurately
            time_diff = int(time.time() - start_time)
        
        # Display Done
        print(f"{self.prefix}{self.done}{self.suffix}")


class Stopwatch(Timer):
    def __init__(self, prefix="", suffix="", done="Done!"):
        super().__init__(duration=0, prefix=prefix, suffix=suffix, done=done)
    
    def start(self):
        # Create Reference Time and initial Time Difference
        start_time = time.time()
        time_diff = int(time.time() - start_time)

        try:
            running = True

            while running:
                # Re-calculate Time Difference, for more accurate time
                time_diff = int(time.time() - start_time)
                
                # Parse raw seconds into  minutes and seconds and create timer display
                minutes, seconds = self.parse_seconds(time_diff)
                timer = f"{minutes:02}:{seconds:02}"

                # Display Time
                print(f"{self.prefix}{timer}{self.suffix}", end='\r')

                # Pause for 1 sec, dont need to change anything til at least 1 sec passes
                time.sleep(1)

        except KeyboardInterrupt:
            # Parse raw seconds into  minutes and seconds and create timer display
            minutes, seconds = self.parse_seconds(int(time.time() - start_time))
            timer = f"{minutes:02}:{seconds:02}"

            # Display Time
            print(f"[ Stopped ]: {timer}")
        
        # Display Done
        print(f"{self.prefix}{self.done}{self.suffix}")


class Pomodoro:
    def __init__(self, work_duration, short_break_duration, long_break_duration) -> None:
        # Timer Durations in Minutes
        self.work_time = work_duration
        self.short_break = short_break_duration
        self.long_break = long_break_duration

        self.cycles = 4

    def __str__(self) -> str:
        text = f""
        return text

    def start(self):
        current_cycle = 0

        short_timer = CountdownTimer(self.short_break, "[ Short Break ]: ", done="Back to Work!\n")
        long_timer = CountdownTimer(self.long_break, "[ Long Break ]: ", done="Back to Work!\n")

        work_timer = CountdownTimer(self.work_time, "[ Work Time ]: ", done="Break Time!")

        print("[ Pomodoro Session Started ]\n")

        try:
            while True:
                # Update Current Cycle
                current_cycle += 1

                #   Work Timer
                work_timer.start()

                #   Break Timer

                # Long, if 4th cycle or multiple of 4
                if current_cycle % 4 == 0:
                    long_timer.start()
                    continue
                
                # Short
                short_timer.start()
                
        except KeyboardInterrupt:
            print("\n\n[ Pomodoro Session Finished ]\n")


def main():
    # timer1 = Timer(120, prefix="[ Timer 1 ]: ")
    # timer2 = CountdownTimer(30, "[ Timer 2 ]")
    # timer3 = Stopwatch("[ Stopwatch ]: ")
    
    # timer1.start()
    # timer2.start()
    # timer3.start()

    p_session = Pomodoro(5, 4, 8)
    p_session.start()


if __name__ == "__main__":
    main()

