import PySimpleGUI as psg

psg.theme('DarkPurple1')

title = 'Simple Calculator'

layout = [[psg.Text('The Simple Calculator')], 
          [psg.Text('Input an algebraic expression to be computed with the buttons or the keyboard.'), psg.InputText()],
          [psg.Button('1'), psg.Button('2'), psg.Button('3'), psg.Button('+')],
          [psg.Button('4'), psg.Button('5'), psg.Button('6'), psg.Button('-')],
          [psg.Button('7'), psg.Button('8'), psg.Button('9'), psg.Button('*')],
          [psg.Button('Clear'), psg.Button('0'), psg.Button('\u00f7'), psg.Button('=')],
          [psg.Button('Exit')]]

window = psg.Window(title, layout)

while True:
    event, vals = window.read()
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    print('Your expression is', vals[0])

window.close()
