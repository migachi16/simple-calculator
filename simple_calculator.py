import PySimpleGUI as psg
import helper_funcs as hf

nums = '0123456789'

psg.theme('dark green 7')
psg.set_options(font = ("Fira Code", 16))

title = 'Simple Calculator'

# TODO 
#   Implement
menu_def =  [
                ['File', ['Save log', 'Clear log', 'Reset', 'Quit',]],
                ['Help', ['About',]]
            ]

layout =    [

                [psg.T('Input an algebraic expression with the buttons or the keyboard.')], 
                
                [psg.Menu(menu_def)],

                [psg.In(key = '-EXP-')],

                [psg.B('1'), psg.B('2'), psg.B('3'), psg.B('+'), psg.B('ANS')],
                [psg.B('4'), psg.B('5'), psg.Button('6'), psg.B('-')],
                [psg.B('7'), psg.B('8'), psg.B('9'), psg.B('*')],

                [psg.B('.'), psg.B('0'), psg.B('^'), psg.B('\u00f7')],

                [psg.B('('), psg.B('C'), psg.B('=', enable_events = True), psg.B(')')],

                [psg.T('Result:'), psg.Output(size = (25, 5), key = '-EQL-'), psg.B('Exit')]
                
            ]

window = psg.Window(title, layout, return_keyboard_events = True, element_justification = 'c')

expression = ''
previous_ans = ''
just_solved = False

while True:
    event, vals = window.read()

    if ':' in event:
        idx = event.index(':')
        event = event[:-(len(event) - idx)] # extended keyboard input handling for the form xxx:#

    #if just_solved == True and event not in nums:
        
    match event:
        #
        case psg.WIN_CLOSED:
            break   
        case 'Exit':
            break
        #
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
        #       
        #   Mundane buttons ^
        #
        case '=' | 'Return':
            valid = hf.check_parentheses(expression) # Parentheses matching
            if valid:
                #
                answer = hf.execute(expression) # Execute the algebraic expression
                #
                just_solved = True
                previous_ans = str(answer)
                print(str(answer))
            else:
                print('Your parentheses do not match!')
        case 'C': # clear
            expression = ''
        case 'ANS': 
            expression += previous_ans

    window['-EXP-'].update(expression)

window.close()
