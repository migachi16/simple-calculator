import PySimpleGUI as psg
import helper_funcs as hf

nums = '0123456789'

psg.theme('TealMono')
psg.set_options(font = ("Fira Code", 14))

title = 'Simple Calculator'

# TODO 
#   Implement
menu_def =  [
                ['File', ['Save log', 'Clear log', 'Reset', 'Quit',]],
                ['Help', ['About',]]
            ]

layout =    [

                [psg.T('Input an algebraic expression with the buttons or the keyboard.'), psg.Push()], 
                
                [psg.Menu(menu_def)],

                [psg.In(key = '-EXP-')],
                
                [psg.VPush()],

                [psg.B('1'), psg.B('2'), psg.B('3'), psg.B('+'),psg.Push(), psg.Push(), psg.B('ANS')],
                [psg.B('4'), psg.B('5'), psg.Button('6'), psg.B('-'), psg.Push(), psg.Push()],
                [psg.B('7'), psg.B('8'), psg.B('9'), psg.B('*'), psg.Push(), psg.Push()],

                [psg.B('.'), psg.B('0'), psg.B('^'), psg.B('\u00f7'), psg.Push(), psg.Push()],

                [psg.B('('), psg.B('C'), psg.B(')'), psg.B('=', enable_events = True), 
                    psg.Push(), psg.Push(), psg.B('Show Log')],

                [psg.VPush()],

                [psg.T('Result:'), psg.Txt(key = '-EQL-'), psg.Push(), psg.B('Exit')]
                
            ]

window =    psg.Window(title, layout, alpha_channel = 0.85, return_keyboard_events = True, 
            right_click_menu = psg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

expression = ''
previous_ans = ''
just_solved = False

"""
Main window event loop
"""
while True:
    event, vals = window.read()
    a = len(expression)

    if event is psg.WIN_CLOSED or event == 'Exit':
        break

    if ':' in event:
        idx = event.index(':')
        event = event[:-(len(event) - idx)] # Extended keyboard input handling for the form xxx:#

    if just_solved == True and event not in {'ANS', 'BackSpace'} and event not in '0123456789.()=':    # Input of operator following a calculated output
        expression = previous_ans

    match event:
        case 'Edit Me':
            psg.execute_editor(__file__)
        case 'Version': 
            psg.popup_scrolled(psg.get_versions())
        case '1':
            expression += '1'
        case '2':
            expression += '2'  
        case '3':
            expression += '3'
        case '4':
            expression += '4' 
        case '5':
            expression += '5'
        case '6':
            expression += '6'
        case '7':
            expression += '7'
        case '8':
            expression += '8' 
        case '9':
            expression += '9'
        case '0':
            expression += '0'    
        case '+' | 'equal' | 'plus':
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
        case '=' | 'Return':
            valid = hf.check_parentheses(expression)    # Parentheses matching
            if valid:
                answer = str(hf.unifier(expression)) # Execute the algebraic expression
                just_solved = True
                previous_ans = answer
                window['-EQL-'].update(answer) # Display the answer
                continue
            else:
                psg.popup_no_wait('Your parentheses do not match!')
        case 'C':   # Clear
            expression = ''
        case 'ANS': 
            expression += previous_ans

    if just_solved and len(expression) != a:
        just_solved = False

    window['-EXP-'].update(expression)

window.close()
