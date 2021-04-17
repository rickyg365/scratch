import PySimpleGUI as sg

"""
Author: Izzy Analytics @youtube
"""

# Default Settings
bw = {'size': (4, 1), 'font': ('Franklin Gothic Book', 24), 'button_color': ("black", "#F8F8F8")}
bt = {'size': (4, 1), 'font': ('Franklin Gothic Book', 24), 'button_color': ("black", "#F1EABC")}
bo = {'size': (9, 1), 'font': ('Franklin Gothic Book', 24), 'button_color': ("black", "#ECA527"), 'focus': True}

layout = [
    [sg.Text('PyDataMath_II', size=(50, 1), justification='right', background_color="#272533", text_color="white", font=('Franklin Gothic Book', 15, 'bold'))],
    [sg.Text('0.0000', size=(50, 1), justification='right', background_color="black", text_color="red", relief='sunken', key="_DISPLAY_")],
    [sg.Button('C', **bt), sg.Button('CE', **bt), sg.Button('%', **bt), sg.Button('/', **bt)],
    [sg.Button('7', **bw), sg.Button('8', **bw), sg.Button('9', **bw), sg.Button('*', **bt)],
    [sg.Button('4', **bw), sg.Button('5', **bw), sg.Button('6', **bw), sg.Button('+', **bt),],
    [sg.Button('1', **bw), sg.Button('2', **bw), sg.Button('3', **bw), sg.Button('-', **bt),],
    [sg.Button('0', **bw), sg.Button('.', **bw), sg.Button('=', **bo)],
]
window = sg.Window('PyDataMath_II', layout=layout, background_color="#272533", size=(360, 420))

# CALCULATOR FUNCTIONS
var: dict = {'front': [], 'back': [], 'decimal': False, 'x_val': 0.0, 'y_val': 0.0, 'result': 0.0, 'operator': ''}


# HELPER FUNCTIONS
def format_number() -> float:
    ''' Create a consolidated string of numbers from front and back lists '''
    return float(''.join(var['front']) + '.' + ''.join(var['back']))


def update_display(display_value):
    ''' Update the calculator display after an event click '''
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)


# -----CLICK EVENTS
def number_click(event: str):
    ''' Number button button click event '''
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())


def clear_click():
    ''' CE or C button click event '''
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False


def operator_click(event: str):
    ''' + - / * button click event '''
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()


def calculate_click():
    ''' Equals button click event '''
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()
    except:
        update_display("ERROR! DIV/0")
        clear_click()


# -----MAIN EVENT LOOP------------------------------------##
while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        number_click(event)
    if event in ['Escape:27', 'C', 'CE']:  # 'Escape:27 for keyboard control
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+', '-', '*', '/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        var['decimal'] = True
    if event == '%':
        update_display(var['result'] / 100.0)

window.close()