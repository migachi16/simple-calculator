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

window = psg.Window(title, layout, element_justification = 'c')

expression = ''
previous_ans = ''

while True:
    event, vals = window.read()
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
        case '+':
            expression += '+'
        case '-':
            expression += '-'
        case '\u00f7':
            expression += '\u00f7'
        case '*':
            expression += '*'    
        case '.':
            expression += '.'    
        case '^':
            expression += '^'    
        case '(':
            expression += '('   
        case ')':
            expression += ')'    
        #
        #   Mundane buttons ^
        #
        case '=':
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
