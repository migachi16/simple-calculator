import PySimpleGUI as psg

psg.theme('DarkPurple1')

title = 'Simple Calculator'

layout = [[psg.T('The Simple Calculator')], 
          [psg.T('Input an algebraic expression to be computed with the buttons or the keyboard.'), psg.In(key = '-EXP-')],
          [psg.B('1'), psg.B('2'), psg.B('3'), psg.B('+')],
          [psg.B('4'), psg.B('5'), psg.Button('6'), psg.B('-')],
          [psg.B('7'), psg.B('8'), psg.B('9'), psg.B('*')],
          [psg.B('Clear'), psg.B('0'), psg.B('\u00f7'), psg.B('=', enable_events = True)],
          [psg.B('Exit')],
          [psg.T('Result:'), psg.Output(size = (10,5), key = '-EQL-')]]

window = psg.Window(title, layout)

while True:
    event, vals = window.read()
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    match event:
        case '1':
            window['-EXP-'].update(1)
        case '2':
            window['-EXP-'].update(2)    
        case '3':
            window['-EXP-'].update(3)
        case '4':
            window['-EXP-'].update(4) 


         
    print('Your expression is', vals['-EXP-'])

window.close()
