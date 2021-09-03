import os

"""
Program: Tic Tac Toe
Author: rickyg3
Date: 09/01/21
"""


# Variables
"""

       0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
U+250x ─  ━  │  ┃  ┄  ┅
U+251x
U+252x
U+253x
U+254x
U+255x
U+256x
U+257x


 123456789AB 
 ........... 
    ┃   ┃    - 1
 ━━━╋━━━╋━━━ - 2
    ┃   ┃    - 3
 ━━━╋━━━╋━━━ - 4
    ┃   ┃    - 5
     
     
u254B: ╋
u2501: ━
u2503: ┃
     
row1 = f"{data[0]:^3}{unicode_col}{data[0]:^3}{unicode_col}{data[0]:^3}"
row2 = '\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501'

"""


# Classes
class TicTacToe:
    def __init__(self):
        self.score = 0

        self.player_moves = []
        self.other_moves = []

        self.data = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.in_use = []

        self.turn = 0

        self.o_moves = []
        self.x_moves = []

        self.display = str(self)

    def __str__(self):
        text = f"Turn: {'O' if self.turn == 0 else 'X'}\n"

        # Variables
        uni_column = '\u2503'
        uni_row = '\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501'

        for _, row in enumerate(self.data):
            text += f"\n{row[0]:^3}{uni_column}{row[1]:^3}{uni_column}{row[2]:^3}"
            if _ != 2:
                text += f"\n{uni_row}"

        text += '\n'

        return text

    def reset(self):
        self.data = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.display = str(self)

    @staticmethod
    def intro_screen():
        intro = f"""Turn: (current player)

 1 ┃ 2 ┃ 3  
━━━╋━━━╋━━━ 
 4 ┃ 5 ┃ 6  
━━━╋━━━╋━━━ 
 7 ┃ 8 ┃ 9    

Choose spot: N
"""
        print(intro)
        input("Press Enter to continue...")

    def switch_turns(self):
        self.score += 1
        if self.turn < 1:
            self.turn += 1
            return
        self.turn -= 1

    def append_player_move(self, data):
        if self.turn == 0:
            self.o_moves.append(data)
            return

        self.x_moves.append(data)
        return

    def make_move(self, choice):
        player_turn = {
            0: 'O',
            1: 'X'
        }
        player = player_turn.get(self.turn)

        key_map = {
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2)
        }

        tup = key_map.get(choice)
        if tup in self.in_use:
            return False

        x, y = tup

        try:
            self.data[x][y] = player
        except Exception as e:
            print(e)
        self.in_use.append(tup)

        self.append_player_move(tup)

        self.switch_turns()

        return True

    def check_win(self):

        current_turn = f"{'o' if self.turn == 0 else 'x'}"

        for i in range(3):
            new_column = []
            new_row = []
            for j in range(3):
                # Row
                new_row.append(self.data[i][j])
                # Col
                new_column.append(self.data[j][i])

            # Check each row
            if len(new_row) >= 3:
                empty_row_condition = new_row[1] != ' '
                if new_row[0] == new_row[1] and new_row[1] == new_row[2] and empty_row_condition:
                    return True

            # Check each col
            if len(new_column) >= 3:
                empty_col_condition = new_column[1] != ' '
                if new_column[0] == new_column[1] and new_column[1] == new_column[2] and empty_col_condition:
                    return True

        # Diagonal
        diag_empty = self.data[1][1] != ' '
        if self.data[0][0] == self.data[1][1] and self.data[1][1] == self.data[2][2] and diag_empty:
            return True

        if self.data[0][2] == self.data[1][1] and self.data[1][1] == self.data[2][0] and diag_empty:
            return True

        return False

    @staticmethod
    def validate_input(some_input):
        valid_input = [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9'
        ]
        if some_input not in valid_input:
            return False

        return True

    def run_match(self):
        # Reset Board
        self.reset()
        running = True

        # Main Game loop
        while running:
            os.system('cls')
            # if more than 9 rounds end game, because board is full
            if self.score == 9:
                running = False
                break

            # display board
            print(self)

            # User input
            try:
                user_input = input(f"Choose spot: ")
                input_status = self.validate_input(user_input)
                if not input_status:
                    input("Invalid Input, try again sucker.")
                    continue

                self.make_move(user_input)
            except KeyboardInterrupt:
                print("\n \n[Program Closed]\n")
                break

            # Check for win
            win_status = self.check_win()

            # for a win
            if win_status:
                os.system('cls')
                print(self)
                print(f"\n{'X' if self.turn==0 else 'O'} Wins! ")
                running = False
                break


if __name__ == "__main__":
    # list_uni_char = []
    # for i in range(8):
    #     base = f'25{i}'
    #     for j in range(16):
    #         text = f"{j}"
    #         if j >= 10:
    #             ch_map = {
    #                 10: 'A',
    #                 11: 'B',
    #                 12: 'C',
    #                 13: 'D',
    #                 14: 'E',
    #                 15: 'F'
    #             }
    #             text = ch_map.get(j)
    #         new_base = base + text
    #
    #         # print(f"\\u{new_base}")
    #         list_uni_char.append(f"\\u{new_base}".encode())
    #
    # # print(list_uni_char)
    # for ele in list_uni_char:
    #     print(ele, ele.decode("unicode-escape")*3)

    new_game = TicTacToe()
    os.system('cls')
    new_game.intro_screen()

    new_game.run_match()

