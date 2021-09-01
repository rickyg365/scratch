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
        intro = f"""

 1,1┃1,2┃1,3 
 ━━━╋━━━╋━━━ 
 2,1┃2,2┃2,3 
 ━━━╋━━━╋━━━ 
 3,1┃3,2┃3,3   


"""
        print(intro)

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

    def make_move(self, tup):
        player_turn = {
            0: 'o',
            1: 'x'
        }
        player = player_turn.get(self.turn)

        if tup in self.in_use:
            return False

        x, y = tup

        try:
            self.data[x-1][y-1] = player
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

    def run_match(self):
        self.reset()
        running = True

        while running:
            os.system('cls')

            if self.score == 9:
                running = False
                break
            print(self)
            user_input = input(f"[{'O' if self.turn == 0 else 'X'}]: ")

            x, y = user_input.split(',')

            new_pair = (int(x), int(y))

            self.make_move(new_pair)
            win_status = self.check_win()
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
    new_game.intro_screen()

    new_game.run_match()
