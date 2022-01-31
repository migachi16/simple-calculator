import PySimpleGUI as psg

psg.theme('dark green 7')

title = 'Simple Calculator'

layout =  [

          [psg.T('Input an algebraic expression with the buttons or the keyboard.')], 
          
          [psg.In(key = '-EXP-')],

          [psg.B('1'), psg.B('2'), psg.B('3'), psg.B('+')],
          [psg.B('4'), psg.B('5'), psg.Button('6'), psg.B('-')],
          [psg.B('7'), psg.B('8'), psg.B('9'), psg.B('*')],
          [psg.B('Clear'), psg.B('0'), psg.B('\u00f7'), psg.B('=', enable_events = True)],

          [psg.B('Exit')],

          [psg.T('Result:'), psg.Output(size = (20, 1), key = '-EQL-')]
          
          ]

window = psg.Window(title, layout, element_justification = 'c')

while True:
    expression = ''
    event, vals = window.read()
    match event:
        case psg.WIN_CLOSED:
            break
        case 'Exit':
            break
        case '1':
            window['-EXP-'].update(1)
        case '2':
            window['-EXP-'].update(2)    
        case '3':
            window['-EXP-'].update(3)
        case '4':
            window['-EXP-'].update(4) 
        case '5':
            window['-EXP-'].update(5)
        case '6':
            window['-EXP-'].update(6)    
        case '7':
            window['-EXP-'].update(7)
        case '8':
            window['-EXP-'].update(8) 
        case '9':
            window['-EXP-'].update(9)
        case '0':
            window['-EXP-'].update(0)    
        case '+':
            window['-EXP-'].update('+')
        case '-':
            window['-EXP-'].update('-') 
        case '\u00f7':
            window['-EXP-'].update('\u00f7')
        case '*':
            window['-EXP-'].update('*')    
        case '=':
            print('Your expression is', expression)
            window['-EXP-'].update()

window.close()
