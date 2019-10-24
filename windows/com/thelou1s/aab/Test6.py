# https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_EXE_Maker.py

import PySimpleGUI as sg
import subprocess
from shutil import copyfile
import shutil
import os
import sys

# ------ Menu Definition ------ #
menu_def = [['Help', 'About'], ]


# https://cx-freeze.readthedocs.io/en/latest/faq.html#data-files
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    return os.path.join(datadir, filename)


def Launcher():
    app_name = 'Aab File Installer'
    app_version = ' v1.0'
    app_title = app_name + app_version
    btn_install = 'Install'
    btn_quit = 'Quit'

    sg.ChangeLookAndFeel('LightGreen')

    layout = [
        [sg.Menu(menu_def, tearoff=True)],

        [sg.T('Select .aab file to install', font='Any 15', size=(28, 1))],

        [sg.T('Aab Files', size=(8, 1)), sg.In(key='_sourcefile_', size=(47, 1)),

         sg.FileBrowse(file_types=(("Aab Files", "*.aab"),))],

        # [sg.T('Jar File'), sg.In(key='_iconfile_', size=(45, 1)),
        #
        #  sg.FileBrowse(file_types=(("Jar File", "*.jar"),))],
        #
        # [sg.T('Keystore File'), sg.In(key='_keystore_file_', size=(45, 1)),
        #
        #  sg.FileBrowse(file_types=(("Keystore File", "*.*"),))],

        [sg.Frame('Output', font='Any 15', layout=[[sg.Output(size=(65, 15), font='Courier 10')]])],

        [sg.ReadFormButton(btn_install, bind_return_key=True),

         sg.SimpleButton(btn_quit, button_color=('white', 'firebrick3')), ]
    ]

    window = sg.Window(app_title,
                       auto_size_text=False,
                       auto_size_buttons=False,
                       default_element_size=(20, 1,),
                       text_justification='right')

    window.Layout(layout)

    # ---===--- Loop taking in user input --- #
    while True:
        (button, values) = window.Read()
        if button in (btn_quit, None):
            break  # exit button clicked

        aab_file = values['_sourcefile_']
        jar_file = find_data_file('bundletool-all-0.10.2.jar')
        keystore_file = find_data_file('imoblife.android.keystore')
        adb_file = find_data_file('adb.exe')
        # jar_file = values['_iconfile_']
        # keystore_file = values['_keystore_file_']

        icon_option = '-i "{}"'.format(jar_file) if jar_file else ''
        source_path, source_filename = os.path.split(aab_file)
        workpath_option = '--workpath "{}"'.format(source_path)
        dispath_option = '--distpath "{}"'.format(source_path)
        specpath_option = '--specpath "{}"'.format(source_path)
        folder_to_remove = os.path.join(source_path, source_filename[:-3])
        file_to_remove = os.path.join(source_path, source_filename[:-3] + '.spec')

        command_output_apks = 'java -jar {} build-apks --bundle={} --output=app.apks --ks={} --ks-pass=pass:88326590 --ks-key-alias=imoblife_android_keystore --key-pass=pass:88326590'.format(
            jar_file, aab_file, keystore_file)
        command_install_apks = 'java -jar {} install-apks --adb={} --apks=app.apks'.format(jar_file, adb_file)

        if button == btn_install:
            prt('aab_file = ' + aab_file)
            prt('jar_file = ' + jar_file)
            prt('keystore_file = ' + keystore_file)

            runCommandWrapper("pwd", window)
            runCommandWrapper(adb_file, window)
            runCommandWrapper(command_output_apks, window, file_to_remove, folder_to_remove)
            runCommandWrapper(command_install_apks, window, './app.apks', folder_to_remove)


        if button == 'About':
            sg.popup('support: thelou1s@yahoo.com')


def runCommandWrapper(command, window, file_to_remove=None, folder_to_remove=None):
    try:
        prt(command)
        # prt('Making EXE... this will take a while.. the program has NOT locked up...')
        window.Refresh()
        # prt('Running command {}'.format(command_line))
        runCommand(command)

        if file_to_remove is not None or folder_to_remove is not None:
            removeFile(file_to_remove, folder_to_remove)

    except Exception as e:
        prt('runCommandWrapper, Exception = ' + str(e))
        # sg.PopupError('runCommandWrapper, Exception = ' + str(e))


def removeFile(file_to_remove, folder_to_remove):
    try:
        prt('runCommandWrapper, remove ' + file_to_remove)
        # shutil.rmtree(folder_to_remove)
        os.remove(file_to_remove)
        prt('**** DONE ****')
    except Exception as e:
        prt('runCommandWrapper, Exception = ' + str(e))


def runCommand(cmd, timeout=None):
    """ run shell command
	@param cmd: command to execute
	@param timeout: timeout for command execution
	@return: (return code from command, command output)
	"""
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
    output = ''

    out, err = p.communicate()
    p.wait(timeout)

    prt('out = ' + str(out))
    prt('err = ' + str(err))

    return (out, err)


def prt(self, *args, sep=' ', end='\n', file=None):
    print()
    print(self, *args, sep=' ', end='\r\n', file=None)


if __name__ == '__main__':
    Launcher()
