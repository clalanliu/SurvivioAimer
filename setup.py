import sys
import os

from cx_Freeze import setup, Executable

build_exe_options = {'packages':['numpy', 'PIL', 'skimage', 'keyboard', 'pyautogui', 'matplotlib']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = Executable('SurvivioAimer.pyw', base=base)

os.environ['TCL_LIBRARY'] = r'C:\Users\user\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\user\AppData\Local\Programs\Python\Python35\tcl\tk8.6'


setup(
        name = "SurvivioAimer",
        version = "0.1",
        description = "SurvivioAimer",
        options = {'build_exe': build_exe_options},
        executables = [executable])