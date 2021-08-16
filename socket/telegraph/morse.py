"""
Program: Morse Code Converter
Author: RickyG3
Date: 08/09/21
"""

# MORSE FUNCTION
# def msg_morse(text):
#     morse_code = {
#         'a': '.-',
#         'b': '-...',
#         'c': '-.-.',
#         'd': '-..',
#         'e': '.',
#         'f': '..-.',
#         'g': '--.',
#         'h': '....',
#         'i': '..',
#         'j': '.---',
#         'k': '-.-',
#         'l': '.-..',
#         'm': '--',
#         'n': '-.',
#         'o': '---',
#         'p': '.--.',
#         'q': '--.-',
#         'r': '.-.',
#         's': '...',
#         't': '-',
#         'u': '..-',
#         'v': '...-',
#         'w': '.--',
#         'x': '-..-',
#         'y': '-.--',
#         'z': '--..'
#     }
#
#     morse = ""
#     for char in text:
#         if char == ' ':
#             morse += '  '
#         else:
#             morse += f"{morse_code[char.lower()]} "
#     return morse
#
#
# def morse_msg(morse):
#     not_morse_code = {
#         '.-': 'a',
#         '-...': 'b',
#         '-.-.': 'c',
#         '-..': 'd',
#         '.': 'e',
#         '..-.': 'f',
#         '--.': 'g',
#         '....': 'h',
#         '..': 'i',
#         '.---': 'j',
#         '-.-': 'k',
#         '.-..': 'l',
#         '--': 'm',
#         '-.': 'n',
#         '---': 'o',
#         '.--.': 'p',
#         '--.-': 'q',
#         '.-.':  'r',
#         '...': 's',
#         '-': 't',
#         '..-': 'u',
#         '...-':  'v',
#         '.--': 'w',
#         '-..-': 'x',
#         '-.--': 'y',
#         '--..': 'z'
#     }
#     words = morse.split("   ")
#
#     text = ""
#     for word in words:
#         letters = word.split(' ')
#         w = ""
#         for letter in letters:
#             if letter in not_morse_code:
#                 w += not_morse_code[letter]
#             else:
#                 w += letter
#         text += f"{w} "
#     return text


def convert_morse(raw_input, is_morse=False):
    # Conversion Data
    morse_code = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..'
    }
    not_morse_code = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z'
    }

    output = ""

    # For Alphanumeric
    if not is_morse:
        for char in raw_input:
            if char == ' ':
                output += '  '
            else:
                output += f"{morse_code.get(char.lower(), char)} "
        return output

    # For Morse
    words = raw_input.split("   ")

    for word in words:
        letters = word.split(' ')
        w = ""
        for letter in letters:
            if letter in not_morse_code:
                w += not_morse_code[letter]
            else:
                w += letter
        output += f"{w} "
    return output


if __name__ == "__main__":
    # Simple Test
    message = "Hi, this is a test!"

    morse_message = convert_morse("testing, 12  fuck testing  yup")

    print(convert_morse(message))

    print(convert_morse(morse_message, True))

    # Simple loop
    while True:
        msg = input("\n>>> ")
        if msg.lower() == 'q':
            break

        print(convert_morse(msg))
