import os

"""
╭───╮
│   │
╰───╯

╭──────────────────╮
│  This is a msg   │
│                  │
│                  │
╰──────────────────╯

┼



╔═══╗
║   ║
╚═══╝

╔══════════════════╗
║                  ║
║     Fuck You     ║
║                  ║
╚══════════════════╝

  ╦  
╠ ╬ ╣
  ╩
"""


def process_raw(raw):
    new_obj = raw.encode('utf-8')

    return new_obj.decode("unicode-escape")


def build_msg_box(message, line_length=20):
    # Box Variables
    tl_corner = '\u256D'
    tr_corner = '\u256E'
    bl_corner = '\u2570'
    br_corner = '\u256F'

    horizontal = '\u2500'
    vertical = '\u2502'

    body = f"{vertical}{'None':^{line_length}}{vertical}\n"

    if type(message) is list:
        body = ""
        for line in message:
            msg_length = len(line)

            difference = line_length - msg_length

            if difference < 0:
                # Need to add new lines
                number_lines = msg_length//line_length + 1

                body = ""
                counter = 0
                for i in range(number_lines):
                    start_point = counter
                    end_point = counter + line_length

                    body += f"{vertical}{line[start_point:end_point]:^{line_length}}{vertical}\n"

                    # adjust variables
                    counter += line_length

            if difference >= 0:
                body += f"{vertical}{line:^{line_length}}{vertical}\n"

    if type(message) is str:
        msg_length = len(message)

        difference = line_length - msg_length

        if difference < 0:
            # ''' or if line is too long use .split to split into a list of words'''
            # list_of_words = message.split(' ')
            #
            # return draw_msg_box(list_of_words, line_length)

            # Need to add new lines
            number_lines = msg_length // line_length + 1

            body = ""
            counter = 0
            for i in range(number_lines):
                start_point = counter
                end_point = counter + line_length
                body += f"{vertical}{message[start_point:end_point]:>{line_length}}{vertical}\n"

                # adjust variables
                counter += line_length

        if difference >= 0:
            body = f"{vertical}{message:^{line_length}}{vertical}\n"

    # Build Box
    box = f"{tl_corner}{horizontal * line_length}{tr_corner}\n"
    box += body
    box += f"{bl_corner}{horizontal * line_length}{br_corner}\n"

    return box


if __name__ == "__main__":
    message_is = input("message is: ")  # ['fuck', 'you']
    line = int(input("line length: "))

    print(build_msg_box(message_is, line))
