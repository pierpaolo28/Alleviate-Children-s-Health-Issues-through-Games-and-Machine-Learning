# Following: https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06

from tkinter import *
from tkinter.colorchooser import askcolor
import matlab.engine
from threading import Thread

#  EEG readings pre-game and set-up
eng = matlab.engine.start_matlab()
eng.addpath(r'C:\Users\hp\Dropbox\Individual Project\Researches\EEG\MatNIC_v03.08', nargout=0)
tf = eng.setupscript(nargout=0)
print(tf)


# Defining threading function to get and store eeg data while playing
def eeg_func():
    # EEG readings during-game
    eng = matlab.engine.start_matlab()
    eng.addpath(r'C:\Users\hp\Dropbox\Individual Project\Researches\EEG\MatNIC_v03.08', nargout=0)
    tf3 = eng.setupscript3(nargout=0)
    print(tf3)


class Painting(object):

    DEFAULT_PEN_SIZE = 10.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1100x600")  # Giving a fixed window size
        self.root.configure(background='green')  # Setting window background color
        self.root.title('Drawing canvas for two users')  # Setting window name
        self.root.resizable(width=False, height=False)  # Making window not resizable
        self.root.iconbitmap('icons.ico')  # Setting window icon

        #  Adding button to chose pen
        self.pen_b = Button(self.root, text='Pen', command=self.use_pen, bg='orange')
        self.pen_b.grid(row=0, column=2)

        #  Adding button to chose color
        self.color_b = Button(self.root, text='Color', command=self.choose_color, bg='orange')
        self.color_b.grid(row=3, column=1)

        #  Adding button to chose eraser
        self.eraser_b = Button(self.root, text='Eraser', command=self.use_eraser, bg='orange')
        self.eraser_b.grid(row=3, column=3)

        #  Adding button to chose font size
        self.choose_b = Scale(self.root, from_=1, to=30, orient=HORIZONTAL, bg='orange')
        self.choose_b.grid(row=3, column=2)

        #  Adding button to reset canvas1
        self.reset_b = Button(self.root, text='Reset1', command=self.reset_b1, bg='orange')
        self.reset_b.grid(row=0, column=1)

        #  Adding button to reset canvas2
        self.reset_b = Button(self.root, text='Reset2', command=self.reset_b2, bg='orange')
        self.reset_b.grid(row=0, column=3)

        #  Making the first drawing canvas
        self.board = Canvas(self.root, bg='white', width=500, height=500)
        self.board.grid(row=1, column=1)

        #  Making the second drawing canvas
        self.board2 = Canvas(self.root, bg='white', width=500, height=500)
        self.board2.grid(row=1, column=3)

        #  Making run setup function
        self.setup()
        #  Keep looping to continue the game
        self.root.mainloop()

    #  Setup all the necessary dependencies
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.old_x2 = None
        self.old_y2 = None
        # Getting the size of the font from the slider button
        self.line_width = self.choose_b.get()
        # Setting default pen color to black
        self.color = self.DEFAULT_COLOR
        # At start of the game is selected the pen, not the eraser
        self.eraser_on = False
        self.active_button = self.pen_b
        # Actions to do when interacting with the two canvas
        self.board.bind('<B1-Motion>', self.paint)
        self.board.bind('<ButtonRelease-1>', self.reset)
        self.board2.bind('<B1-Motion>', self.paint2)
        self.board2.bind('<ButtonRelease-1>', self.reset2)

    # Action to execute when pressing the pen button
    def use_pen(self):
        self.activate_b(self.pen_b)

    # Action to execute when pressing the reset1 button (clear canvas1)
    def reset_b1(self):
        self.board.delete("all")

    # Action to execute when pressing the reset2 button (clear canvas2)
    def reset_b2(self):
        self.board2.delete("all")

    # Action to execute when pressing the choose color button slider
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    # Action to execute when pressing the eraser button
    def use_eraser(self):
        self.activate_b(self.eraser_b, eraser_mode=True)

    # When activated the button is raised, when deactivated is sunken
    def activate_b(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    # Making lines appear on the first canvas when dragging mouse
    def paint(self, event):
        self.line_width = self.choose_b.get()  # Use font size of the slider button
        paint_color = 'white' if self.eraser_on else self.color  # If the erase button is pressed paint color=white
        if (event.x or event.y == self.board):  # If the mouse is clicked on the first canvas
            if self.old_x and self.old_y:  # Drawing
                self.board.create_line(self.old_x, self.old_y, event.x, event.y,
                                       width=self.line_width, fill=paint_color,
                                       capstyle=ROUND, smooth=TRUE, splinesteps=33)
            self.old_x = event.x
            self.old_y = event.y

    # Making lines appear on the second canvas when dragging mouse
    def paint2(self, event):
        self.line_width = self.choose_b.get() # Use font size of the slider button
        paint_color = 'white' if self.eraser_on else self.color  # If the erase button is pressed paint color=white
        if (event.x or event.y == self.board2):  # If the mouse is clicked on the first canvas
            if self.old_x2 and self.old_y2:  # Drawing
                 self.board2.create_line(self.old_x2, self.old_y2, event.x, event.y,
                                       width=self.line_width, fill=paint_color,
                                       capstyle=ROUND, smooth=TRUE, splinesteps=33)
            self.old_x2 = event.x
            self.old_y2 = event.y

    # Setting up reset function for first canvas
    def reset(self, event):
        self.old_x, self.old_y = None, None

    # Setting up reset function for second canvas
    def reset2(self, event):
        self.old_x2, self.old_y2 = None, None

# Executing threads. Run the painting class while recording the EEG data!
Thread(target = Painting).start()
Thread(target = eeg_func).start()