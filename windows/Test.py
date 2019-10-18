import PySimpleGUI as sg
import subprocess


def runCommand(cmd, timeout=None):
    """ run shell command
	@param cmd: command to execute
	@param timeout: timeout for command execution
	@return: (return code from command, command output)
	"""

    prt('runCommand, cmd = ' + str(cmd))

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
    output = ''

    prt('runCommand, communicate')
    out, err = p.communicate()
    prt('runCommand, wait')
    p.wait(timeout)

    prt(out)
    prt(err)
    sg.Popup(out)

    return (out, err)


def prt(self, *args, sep=' ', end='\n', file=None):
    print()
    print(self, *args, sep=' ', end='\r\n', file=None)

# All the stuff inside your window.
layout = [
    [sg.Text('Some text on Row 1')]
    , [sg.Text('Enter something on Row 2'), sg.InputText()]
    , [sg.Button('Ok'), sg.Button('Cancel')]
    # , [sg.PopupScrolled('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')]
]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    if event in (None, 'Ok'):  # if user closes window or clicks cancel
            runCommand('ls')
    print('You entered ', values[0])

window.close()
