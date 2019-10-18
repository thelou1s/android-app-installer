# https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_EXE_Maker.py

import PySimpleGUI as sg
import subprocess
from shutil import copyfile
import shutil
import os


def prt(self, *args, sep=' ', end='\n', file=None):
    print()
    print(self, *args, sep=' ', end='\r\n', file=None)


def Launcher():
    sg.ChangeLookAndFeel('LightGreen')

    layout = [
        [sg.T('PyInstaller EXE Creator', font='Any 15')],
        [sg.T('Source Python File'), sg.In(key='_sourcefile_', size=(45, 1)), sg.FileBrowse(file_types=(("Python Files", "*.py"),))],
        [sg.T('Icon File'), sg.In(key='_iconfile_', size=(45, 1)), sg.FileBrowse(file_types=(("Icon Files", "*.ico"),))],
        [sg.T('Keystore'), sg.In(key='_keystore_file_', size=(45, 1)), sg.FileBrowse(file_types=(("Icon Files", "*.ico"),))],
        [sg.Frame('Output', font='Any 15', layout=[[sg.Output(size=(65, 15), font='Courier 10')]])],
        [sg.ReadFormButton('Make EXE', bind_return_key=True), sg.SimpleButton('Quit', button_color=('white', 'firebrick3')), ]
    ]

    window = sg.Window('PySimpleGUI EXE Maker',
                       auto_size_text=False,
                       auto_size_buttons=False,
                       default_element_size=(20, 1,),
                       text_justification='right')

    window.Layout(layout)

    # ---===--- Loop taking in user input --- #
    while True:
        (button, values) = window.Read()
        if button in ('Quit', None):
            break  # exit button clicked

        source_file = values['_sourcefile_']
        icon_file = values['_iconfile_']
        keystore_file = values['_keystore_file_']

        icon_option = '-i "{}"'.format(icon_file) if icon_file else ''
        source_path, source_filename = os.path.split(source_file)
        workpath_option = '--workpath "{}"'.format(source_path)
        dispath_option = '--distpath "{}"'.format(source_path)
        specpath_option = '--specpath "{}"'.format(source_path)
        folder_to_remove = os.path.join(source_path, source_filename[:-3])
        file_to_remove = os.path.join(source_path, source_filename[:-3] + '.spec')
        # command_line = 'pyinstaller -wF "{}" {} {} {} {}'.format(source_file, icon_option, workpath_option,
        #                                                          dispath_option, specpath_option)
        command_line = 'java -jar {} build-apks --bundle={} --output=app.apks --ks={} --ks-pass=pass:88326590 --ks-key-alias=imoblife_android_keystore --key-pass=pass:88326590'.format(
            icon_file, source_file, keystore_file)
        command_install_apks = 'java -jar {} install-apks --apks=app.apks'.format(icon_file)

        if button == 'Make EXE':
            prt('source_file: ' + str(source_file))
            prt('Making EXE... this will take a while.. the program has NOT locked up...')
            window.Refresh()

            command("pwd", source_file, window)
            command(command_line, source_file, window)
            command(command_install_apks, source_file, window)


def command(command_line, source_file, window):
    try:
        prt('window.Refresh')
        window.Refresh()
        runCommand(command_line)
        # shutil.rmtree(folder_to_remove)
        # os.remove(file_to_remove)
        prt('**** DONE ****')
    except Exception as e:
        # sg.PopupError('Something went wrong')
        prt("Launcher, Exception = " + e)


def runCommand(cmd, timeout=None):
    """ run shell command
    @param cmd: command to execute
    @param timeout: timeout for command execution
    @return: (return code from command, command output)
    """

    prt('runCommand, cmd = ' + str(cmd))

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''

    prt('runCommand, communicate')
    out, err = p.communicate()
    prt('runCommand, wait')
    p.wait(timeout)

    prt('out = ' + str(out))
    prt('err = ' + str(err))

    return (out, err)


if __name__ == '__main__':
    Launcher()
