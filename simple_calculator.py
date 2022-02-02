import PySimpleGUI as psg
import helper_funcs as hf

psg.theme('dark green 7')

title = 'Simple Calculator'

layout =  [

          [psg.T('Input an algebraic expression with the buttons or the keyboard.')], 
          
          [psg.In(key = '-EXP-')],

          [psg.B('1'), psg.B('2'), psg.B('3'), psg.B('+')],
          [psg.B('4'), psg.B('5'), psg.Button('6'), psg.B('-')],
          [psg.B('7'), psg.B('8'), psg.B('9'), psg.B('*')],

          [psg.B('.'), psg.B('0'), psg.B('^'), psg.B('\u00f7')],

          [psg.B('('), psg.B('C'), psg.B('=', enable_events = True), psg.B(')')],

          [psg.T('Result:'), psg.Output(size = (25, 4), key = '-EQL-'), psg.B('Exit')]
          
          ]

window = psg.Window(title, layout, return_keyboard_events = True, element_justification = 'c')

expression = ''
previous_ans = ''
all_keys = ['1:10', '2:11', '3:12', '4:13', '5:14', '6:15', '7:16',
            '8:17', '9:18', '0:19', 'minus:20', 
            'equal:21', 'BackSpace:22', 'slash:61', 'period:60', 
            'Return:36', 'Shift_R:62', 'Shift_L:50',]


while True:
    event, vals = window.read()
    match event:
        #
        case psg.WIN_CLOSED:
            break   
        case 'Exit':
            break
        #
        case '1' | '1:10':
            expression += '1'
        case '2' | '2:11':
            expression += '2'  
        case '3' | '3:12':
            expression += '3'
        case '4' | '4:13':
            expression += '4' 
        case '5' | '5:14':
            expression += '5'
        case '6' | '6:15':
            expression += '6'
        case '7' | '7:16':
            expression += '7'
        case '8' | '8:17':
            expression += '8' 
        case '9' | '9:18':
            expression += '9'
        case '0' | '0:19':
            expression += '0'    
        case '+':
            expression += '+'
        case '-' | 'minus:20':
            expression += '-'
        case '\u00f7' | 'slash:61':
            expression += '\u00f7'
        case '*':
            expression += '*'    
        case '.' | 'period:60':
            expression += '.'    
        case '^':
            expression += '^'    
        case '(':
            expression += '('   
        case ')':
            expression += ')'   
        case 'BackSpace:22':
                if len(expression) == 0:
                    continue
                li = list(expression)
                li.pop()
                expression = ''.join(li)
        #       
        #   Mundane buttons ^
        #
        case '=' | 'Return:36':
            valid = hf.check_parentheses(expression)
            if valid:
                #
                answer = hf.execute(expression) # Execute the algebraic expression
                #
                print(str(answer))
            else:
                print('Your parentheses do not match!')
        case 'C': # clear
            expression = ''

    window['-EXP-'].update(expression)

window.close()
