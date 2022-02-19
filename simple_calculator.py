import os
import PySimpleGUI as psg
import helper_funcs as hf

psg.theme('TealMono')
psg.set_options(font = ("Fira Code", 14))

NUMS = '0123456789'
TITLE = 'Simple Calculator'

# Initial login/registry window
layout = [
            [psg.T('Enter your Login ID or register'), psg.In(key = '-ID-')],          
            [psg.B('OK', bind_return_key = True), psg.B('Exit'), psg.B('Register') ]
         ]

window = psg.Window('Authentication', layout, return_keyboard_events = True)

while True:   
    event, values = window.read()

    if event is psg.WIN_CLOSED or event == 'Exit':
        break

    login_id = values['-ID-']
    match event:
        case 'OK':
            break
        case 'Register':
            break

window.close()

# Main calculator window

#TODO
# Top bar, left tab menu
menu_def =  [
                ['File', ['Save log', 'Clear log', 'Reset', 'Quit',]],
                ['Help', ['About',]]
            ]

layout =    [

                [psg.T('Input an algebraic expression with the buttons or the keyboard.'),
                    psg.Push()], 
                
                [psg.Menu(menu_def)],
                [psg.In(key = '-EXP-')],
                
                [psg.VPush()],

                [psg.B('1'), psg.B('2'), psg.B('3'), psg.B('+'),psg.Push(), psg.B('ANS')],
                [psg.B('4'), psg.B('5'), psg.Button('6'), psg.B('-'), psg.Push()],
                [psg.B('7'), psg.B('8'), psg.B('9'), psg.B('*'), psg.Push()],
                [psg.B('.'), psg.B('0'), psg.B('^'), psg.B('\u00f7'), psg.Push()],
                [psg.B('('), psg.B('C'), psg.B(')'), psg.B('=', enable_events = True, 
                    bind_return_key = True), psg.Push(), psg.B('Show Log')],

                [psg.VPush()],

                [psg.T('Result:'), psg.Txt(key = '-EQL-'), psg.Push(), psg.B('Exit')]
                
            ]

window = psg.Window(TITLE, layout, alpha_channel = 0.85, return_keyboard_events = True, 
         right_click_menu = psg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

user_verified = False

expression = ''
previous_ans = ''
history = []        # Log button brings up a log of previous calculations stored here
just_solved = False

# Main window loop
while True:
    event, vals = window.read()
    a = len(expression)

    if event is psg.WIN_CLOSED or event == 'Exit':
        break

    if ':' in event:
        idx = event.index(':')
        event = event[:-(len(event) - idx)] # Extended keyboard input handling for the form xxx:#

    if just_solved is True and event in {'+', 'plus', '-', 'minus', 
                                            '\u00f7', 'slash', '/', '*', '^'}:  # Input of operator following a calculated output
        expression = previous_ans

    if event in NUMS:
        expression += event

    match event:
        case 'Edit Me':
            psg.execute_editor(__file__)
        case 'Version': 
            psg.popup_scrolled(psg.get_versions())
        case '+' | 'plus':
            expression += '+'
        case '-' | 'minus':
            expression += '-'
        case '\u00f7' | 'slash' | '/':
            expression += '\u00f7'
        case '*':
            expression += '*'    
        case '.' | 'period':
            expression += '.'    
        case '^':
            expression += '^'    
        case '(':
            expression += '('   
        case ')':
            expression += ')'   
        case 'BackSpace':
            if len(expression) == 0:
                continue 
            expression = expression[:-1]
        case '=':
            if expression == '':
                continue
            valid = hf.check_parentheses(expression)

            if valid:
                answer = str(hf.unifier(expression)) # Execute the algebraic expression
                just_solved = True
                previous_ans = answer
                if len(answer) <= 10 and float(answer).is_integer():
                    window['-EQL-'].update(int(float(answer))) # Display the answer
                else:
                    window['-EQL-'].update(format(float(answer), '.9E')) # Display the answer
                continue
            else:
                psg.popup_no_wait('Your parentheses do not match, or check for invalid symbols.')

        case 'C':   # Clear
            expression = ''
            window['-EXP-'].update(expression)
        case 'ANS': 
            expression += previous_ans

    if just_solved and len(expression) != a:
        just_solved = False

    window['-EXP-'].update(expression)

window.close()

