import os
import sys


def clear_screen():
    platform = sys.platform

    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def buildHPBar(hp_amount, total_hp, hp_bar_length=10):
    hp_fraction = hp_amount/total_hp 
    hp_in_bar = int(hp_fraction * hp_bar_length)
    free_space = hp_bar_length - hp_in_bar

    new_bar = f"{'■'*hp_in_bar}{'□'*free_space}" 
    
    return new_bar

def box(inner_text:list[str], style_choice="round", justify='left') -> str:
    """ assuming every line is the same length """
    if justify == 'right':
        cols, rows = os.get_terminal_size()

    num_lines = len(inner_text)
    line_length = len(inner_text[0])

    styles = {
        "regular": {
            'tlcorner': '┌',
            'trcorner': '┐',
            'blcorner': '└',
            'brcorner': '┘',
            'horizontal': '─',
            'vertical': '│'
        },
        "bold": {
            'tlcorner': '┏',
            'trcorner': '┓',
            'blcorner': '┗',
            'brcorner': '┛',
            'horizontal': '━',
            'vertical': '┃'
        },
        "round": {
            'tlcorner': '╭',
            'trcorner': '╮',
            'blcorner': '╰',
            'brcorner': '╯',
            'horizontal': '─',
            'vertical': '│'
        }
    }

    current_style = styles[style_choice]

    # Top Row
    final_box = ""

    if justify == 'right':
        top_row = f"{current_style['tlcorner']}{current_style['horizontal']*line_length}{current_style['trcorner']}"
        final_box += f"{top_row:>{cols}}"
    else:
        final_box += f"{current_style['tlcorner']}{current_style['horizontal']*line_length}{current_style['trcorner']}"
    
    # Dynamic Middle
    for i in range(num_lines):
        if justify == 'right':
            new_row = f"{current_style['vertical']}{inner_text[i]}{current_style['vertical']}"
            final_box += f"\n{new_row:>{cols}}"
            continue
        final_box += f"\n{current_style['vertical']}{inner_text[i]}{current_style['vertical']}"

    # Bot Row
    if justify == 'right':
        final_row = f"{current_style['blcorner']}{current_style['horizontal']*line_length}{current_style['brcorner']}"
        final_box += f"\n{final_row:>{cols}}"
    else:
        final_box += f"\n{current_style['blcorner']}{current_style['horizontal']*line_length}{current_style['brcorner']}"
    
    return final_box


