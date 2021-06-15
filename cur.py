# Clear the screen and hold it for 3 seconds
import curses
import time


# screen = curses.initscr()
# # screen.clear()
#
# # Update the buffer, adding text at different locations
# screen.addstr(0, 0, "This string gets printed at position (0, 0)")
# screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
# screen.addstr(4, 4, "X")
# screen.addch(5, 5, "Y")
#
# # Changes go in to the screen buffer and only get
# # displayed after calling `refresh()` to update
# screen.refresh()
#
# curses.napms(3000)
#
# time.sleep(3)
#
# curses.endwin()


screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()
curses.endwin()

print("Rows:    %d" % num_rows)
print("Columns: %d" % num_cols)

#
# screen = curses.initscr()
#
# # Make a pad 100 lines tall 20 chars wide
# # Make the pad large enough to fit the contents you want
# # You cannot add text larger than the pad
# # We are only going to add one line and barely use any of the space
# pad = curses.newpad(100, 100)
# pad.addstr("This text is thirty characters")
#
# # Start printing text from (0,2) of the pad (first line, 3rd char)
# # on the screen at position (5,5)
# # with the maximum portion of the pad displayed being 20 chars x 15 lines
# # Since we only have one line, the 15 lines is overkill, but the 20 chars
# # will only show 20 characters before cutting off
# pad.refresh(0, 2, 5, 5, 15, 20)
#
# curses.napms(3000)
# curses.endwin()


# # The `screen` is a window that acts as the master window
# # that takes up the whole screen. Other windows created
# # later will get painted on to the `screen` window.
# screen = curses.initscr()
#
# # lines, columns, start line, start column
# my_window = curses.newwin(15, 20, 0, 0)
#
# # Long strings will wrap to the next line automatically
# # to stay within the window
# my_window.addstr(4, 4, "Hello from 4,4")
# my_window.addstr(5, 15, "Hello from 5,15 with a long string")
#
# # Print the window to the screen
# my_window.refresh()
# curses.napms(2000)
#
# # Clear the screen, clearing my_window contents that were printed to screen
# # my_window will retain its contents until my_window.clear() is called.
# screen.clear()
# screen.refresh()
#
# # Move the window and put it back on screen
# # If we didn't clear the screen before doing this,
# # the original window contents would remain on the screen
# # and we would see the window text twice.
# my_window.mvwin(10, 10)
# my_window.refresh()
# curses.napms(1000)
#
# # Clear the window and redraw over the current window space
# # This does not require clearing the whole screen, because the window
# # has not moved position.
# my_window.clear()
# my_window.refresh()
# curses.napms(1000)
#
# curses.endwin()
