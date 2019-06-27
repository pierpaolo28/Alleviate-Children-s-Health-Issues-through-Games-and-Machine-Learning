from cx_Freeze import setup, Executable
import os

base = None

executables = [Executable("game3.py", base=base)]

packages = ["idna","tkinter","itertools", "PIL", "os"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

os.environ['TCL_LIBRARY'] = "C:\\Users\\hp\\Anaconda3\\pkgs\\python-3.6.6-hea74fb7_0\\tcl"
os.environ['TK_LIBRARY'] = "C:\\Users\\hp\\Anaconda3\\pkgs\\python-3.7.0-hea74fb7_0\\tcl\\tk8.6"

setup(
    name = "GAME",
    options = options,
    version = "0.1",
    description = 'Game3',
    executables = executables
)