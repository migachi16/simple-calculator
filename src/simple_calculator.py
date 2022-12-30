import PySimpleGUI as psg
import helper_funcs as hf

# Set theme and font
psg.theme('TealMono')
psg.set_options(font = ("Fira Code", 14))

# Valid inputs
NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Window Title
TITLE = 'A Most Simple Calculator'

login_id = ''

# Verification handling
user_verified = False

# Initial login/registry window
layout = [
            [psg.T('Enter your Login ID and password or register for an account')],   

            [psg.T('Login ID: '), psg.Push(), psg.In(key = '-ID-')],    
            [psg.T('Password: '), psg.Push(), psg.In(key = '-PW-', password_char = '\u2022')], 
            [psg.T('Email if registering: '), psg.Push(), psg.In(key = '-EM-')],

            [psg.VPush()],

            [psg.B('Use AMSC as a guest'), psg.T('?', tooltip = 'With an account, your layout and settings are preserved')], 
            
            [psg.VPush()],

            [psg.B('Exit'), psg.Push(), psg.B('Register'), 
                psg.B('Login', bind_return_key = True)]
         ]

# Initialize window
window = psg.Window(TITLE, layout, return_keyboard_events = True, element_justification = 'c')

# Main window loop
while True:   

    # Default window interaction
    event, values = window.read()

    if event is psg.WIN_CLOSED or event == 'Exit':
        break
    
    # Store inputted values
    login_id = values['-ID-']
    password = values['-PW-']
    email = values['-EM-']

    match event:
        case 'Login':

            # hf is helper_funcs.py. Check if the user is verified 
            user_verified = hf.login(login_id, password)
            if not user_verified:
                psg.popup('Invalid ID or password.')
                continue
            else:
                break

        case 'Register':
            code = hf.register(login_id, password, email)
            match code:
                case 'IDExist':
                    psg.popup('This ID is already registered')
                case 'Invalid':
                    psg.popup('You must first fill out the form')
                case ',':
                    psg.popup('Invalid comma character in login ID')
                case '@':
                    psg.popup('Please enter a valid email address. We\'ll never spam you!')
                case 'Success':
                    psg.popup('Account successfully created. Please restart and login')

        case 'Use AMSC as a guest':
            login_id = 'USERNAME'
            break

window.close()

# Begin main calculator window

# TODO
# Top bar, left tab menu, individual user settings, integration, linalg, graphs,
# equation solving, etc.

psg.set_options(font = ("Fira Code", 14, 'bold'))

menu_def =  [
                ['File', ['Save log', 'Clear log', 'Reset', 'Quit',]],
                ['Help', ['AMSC Guide', 'Settings']]
            ]

layout =    [
                [psg.Menu(menu_def)],

                [psg.T('Input:'), psg.In(key = '-EXP-'), psg.T('Output:'), psg.Txt(key = '-EQL-'), psg.Push()], 

                [psg.VPush()],

                [psg.B(' 1 '), psg.B(' 2 '), psg.B(' 3 '), psg.B(' + '), psg.B('Del', tooltip = 'Delete the last value'), psg.Push()],
                [psg.B(' 4 '), psg.B(' 5 '), psg.Button(' 6 '), psg.B(' - '), psg.Push()],
                [psg.B(' 7 '), psg.B(' 8 '), psg.B(' 9 '), psg.B(' * '), psg.Push()],
                [psg.B(' . '), psg.B(' 0 '), psg.B(' ^ '), psg.B(' \u00f7 '), psg.Push()],
                [psg.B(' ( '), psg.B(' C ', tooltip = 'Clear input'), psg.B(' ) '), psg.B(' = ', enable_events = True, 
                    bind_return_key = True), psg.B('Ans', tooltip = 'Previous answer'), psg.Push()],

                [psg.VPush()],

                [psg.B(' \u221a '), psg.B(' E ', tooltip = 'Base 10 exponential'), psg.B(' e ', tooltip = 'Euler\'s number'), 
                    psg.B(' \u03c0 '), psg.B('sin'), psg.B('cos'), psg.B('tan'),],
                
                [psg.VPush()],
                [psg.VPush()],
                [psg.VPush()],
                [psg.VPush()],
                [psg.VPush()],
                [psg.VPush()],
                [psg.VPush()],

                [psg.B('Memory', tooltip = 'Show a log of the previous calculations'), psg.Push(), psg.B('Exit')]     
            ]

window = psg.Window(TITLE, layout, alpha_channel = 0.85, return_keyboard_events = True, 
    size = (1600, 900))

# TODO 
# Handle user settings
if not user_verified and login_id != 'USERNAME':
    window.close() 

expression = ''
exp_stack = []

left_stack = []

previous_ans = ''

# Memory button brings up a log of previous calculations stored in history
history = {}   

just_solved = False

# Main window loop
while True:
    event, vals = window.read()
    check_len = len(expression) 

    if event is psg.WIN_CLOSED or event == 'Exit':
        break

    event = event.strip()
    
    # Extended keyboard input handling for the form xxx:#
    if ':' in event:
        idx = event.index(':')      
        event = event[:-(len(event) - idx)] 

    if just_solved is True and event in {'+', 'plus', '-', 'minus', '\u00f7', 'slash',
            '/', '*', '^'}:  
        
        # Input of operator following a calculated output
        expression = previous_ans   
        exp_stack.append(previous_ans)    

    if event in NUMS:
        exp_stack.append(event)
        expression += event

    match event:
        case '(':
            left_stack.append(1)
            exp_stack.append('(')
            expression += '('
        case ')':
            if(left_stack):
                left_stack.pop()
                exp_stack.append(')')
                expression += ')'
            else:
                psg.popup_no_wait('You must open a parenthesis first!')
                continue
        case '^':
            left_stack.append(1)
            exp_stack.append('**(')
            expression += '^('
        case '*':
            exp_stack.append('*')
            expression += '*'
        case '+' | 'plus':
            exp_stack.append('+')
            expression += '+'
        case '-' | 'minus':
            exp_stack.append('-')
            expression += '-'
        case '\u00f7' | 'slash' | '/':
            exp_stack.append('/')
            expression += '\u00f7'    
        case '.' | 'period':
            exp_stack.append('.')
            expression += '.'       
        case 'BackSpace' | 'Del':
            if expression == '':
                continue 
            else:
                exp_stack.pop()
                expression = expression[:-1]
        case 'E':
            exp_stack.append('*10**')
            expression += 'E'
        case 'e':
            exp_stack.append('math.e')
            expression += 'e'
        case '\u03c0':
            exp_stack.append('math.pi')
            expression += '\u03c0'
        case 'sin':
            left_stack.append(1)
            exp_stack.append('math.sin(')
            expression += 'sin('
        case 'cos':
            left_stack.append(1)
            exp_stack.append('math.cos(')
            expression += 'cos('
        case 'tan':
            left_stack.append(1)
            exp_stack.append('math.tan(')
            expression += 'tan('
        case '\u221a':
            left_stack.append(1)
            exp_stack.append('math.sqrt(')
            expression += '\u221a('

        # TODO
        case '=':
            if expression == '' or just_solved:
                continue

            # Check if the parentheses in the expression are matching and valid
            valid = not left_stack

            if valid:
                # Execute the algebraic expression
                answer = hf.evaluate(exp_stack)         

                if answer is None:
                    psg.popup_no_wait('You tried to divide by 0!')
                    continue

                if answer == '!!!':
                    psg.popup_no_wait('Your expression is invalid!')
                    continue

                if answer == '???':
                    psg.popup_no_wait('The result is undefined')
                    continue

                if answer <= (1.23e-16) and answer >= 0:
                    answer = 0

                answer = str(answer)  
                just_solved = True
                previous_ans = answer
                history[expression] = answer
                exp_stack = []
                left_stack = []

                if len(answer) <= 10 and float(answer).is_integer():
                    window['-EQL-'].update(int(float(answer)))
                elif len(answer) <= 10:
                    window['-EQL-'].update(float(answer))
                else:
                    # TODO
                    # Cleaner scientific notation processing needed
                    window['-EQL-'].update(format(float(answer), '.9E'))
                continue
            else:
                psg.popup_no_wait('Your parentheses do not match, or you must check for invalid symbols.')

        case 'C':
            expression = ''
            exp_stack = []
            left_stack = []
            window['-EXP-'].update(expression)
        case 'Ans': 
            exp_stack.append(previous_ans)
            expression += previous_ans
        case 'Memory':
            psg.popup_scrolled(hf.history_list(history), title = 'Memory')


    if just_solved and len(expression) != check_len:
        just_solved = False         

    window['-EXP-'].update(expression)
    print(exp_stack)

window.close()

