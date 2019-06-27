import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\hp\\Anaconda3\\pkgs\\python-3.6.6-hea74fb7_0\\tcl"
os.environ['TK_LIBRARY'] = "C:\\Users\\hp\\Anaconda3\\pkgs\\python-3.7.0-hea74fb7_0\\tcl\\tk8.6"

cx_Freeze.setup(
    name="Avalance Escape!",
    version = "0.1",
    author = "Pier Paolo Ippolito",
    options={"build_exe": {"packages":["pygame","time","random"],
                           "include_files": ["user.png", "girl.png", "Background.jpg", "object.jpg",
                                             "intro.jpg", "instra.jpg", "win.wav", "gameover.wav", "Zelda.wav"]}},
    executables=[cx_Freeze.Executable("game.py")]
    )