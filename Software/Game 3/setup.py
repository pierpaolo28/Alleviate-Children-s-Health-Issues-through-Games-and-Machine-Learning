import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\hp\\Anaconda3\\pkgs\\python-3.6.6-hea74fb7_0\\tcl"
os.environ['TK_LIBRARY'] = "C:\\Users\\hp\\Anaconda3\\pkgs\\python-3.7.0-hea74fb7_0\\tcl\\tk8.6"

cx_Freeze.setup(
    name="Game 7",
    version = "0.1",
    author = "Pier Paolo Ippolito",
    options={"build_exe": {"packages":["pyautogui", "pygame", "time"],
                           "include_files": ["ico.png", "square.png","btn1.PNG", "btn2.PNG","back.jpg"]}},
    executables=[cx_Freeze.Executable("game7.py")]
    )