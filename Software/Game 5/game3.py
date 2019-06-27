from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from itertools import count, cycle # Library to play GIF
from sys import byteorder # Libraries to record audio
from array import array
from struct import pack
import pyaudio
import wave

THRESHOLD = 200 # Constants used to record audio
CHUNK_SIZE = 2048
FORMAT = pyaudio.paInt16
RATE = 44100


# Audio Recording and storing from StackOverflow:
# https://stackoverflow.com/questions/892199/detect-record-audio-in-python
def is_silent(snd_data):
    # Returns 'True' if below the 'silent' threshold
    return max(snd_data) < THRESHOLD


def normalize(snd_data):
    # Average the volume out
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r


def trim(snd_data):
    # Trim the blank spots at the start and end
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data


def add_silence(snd_data, seconds):
    # Add silence to the start and end of 'snd_data' of length 'seconds' (float)
    r = array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r


def record():
    # Record a word or words from the microphone and return the data as an array of signed shorts.
    # Normalizes the audio, trims silence from the start and end, and pads with 0.5 seconds of
    # blank sound to make sure VLC et al can play it without getting chopped off.
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r


def record_to_file(path):
    # Records from the microphone and outputs the resulting data to 'path'
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

# Creating root window and window icon
window = Tk()
window.iconbitmap(r'icon.ico')


# ImageButton class from Reddit thread: https://www.reddit.com/r/learnpython/comments/822k04/gif_playing_in_gui_tkinter/
# Running a GIF using TkInter
class ImageButton(tk.Button):

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


# Creating Level 1 game top level window
def create_window():
    newwindow = tk.Toplevel(window)
    newwindow.configure(background='orange')  # Adding background colour
    newwindow.iconbitmap(r'icon.ico')
    newwindow.title("Level 1")
    newwindow.geometry('800x600')
    # Making widget resize and relocate when changing window size
    newwindow.grid_columnconfigure(0, weight=1)
    newwindow.grid_columnconfigure(1, weight=1)
    newwindow.grid_columnconfigure(2, weight=1)
    newwindow.grid_rowconfigure(0, weight=1)
    newwindow.grid_rowconfigure(1, weight=1)
    # Adding label with game title and making label background transparent
    newlbl = Label(newwindow, text="Which images are not a dog? Why not?", font=("Arial Bold", 14),
                   background='orange')
    # The window can ba considered as a matrix
    # Placing label in the desired position in the window and setting the distance between label and other widgets
    newlbl.grid(column=1, row=0, padx=10, pady=10)

    # Creating pop up windows functions when clicking on game images (Winning or Losing image)
    def clicked_right():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl1_horse.wav')
        print("Finished the result is written to Lvl1_horse.wav")

    def clicked_right2():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl1_cat.wav')
        print("Finished the result is written to Lvl1_cat.wav")

    def clicked_wrong():
        messagebox.showinfo('Try again', 'The selected answer is not the right one', parent=newwindow)

    # Storing images to be used on the game buttons
    image1 = Image.open("dog1.png")
    photo1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("dog2.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("notdog.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("notdog1.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    image5 = Image.open("dog3.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    image6 = Image.open("dog4.jpg")
    photo6 = ImageTk.PhotoImage(image6)

    # Creating buttons, corresponding actions and background pictures
    newbtn = Button(newwindow, bg="orange", command=clicked_wrong, height=180, width=180,
                    image = photo1)
    newbtn.image = photo1
    newbtn2 = Button(newwindow, bg="blue", command=clicked_wrong, height=180, width=180,
                     image = photo2)
    newbtn2.image = photo2
    newbtn3 = Button(newwindow, bg="green", command=clicked_right, height=180, width=180,
                     image = photo3)
    newbtn3.image = photo3
    newbtn4 = Button(newwindow, bg="orange", command=clicked_right2, height=180, width=180,
                    image = photo4)
    newbtn4.image = photo4
    newbtn5 = Button(newwindow, bg="blue", command=clicked_wrong, height=180, width=180,
                     image = photo5)
    newbtn5.image = photo5
    newbtn6 = Button(newwindow, bg="green", command=clicked_wrong, height=180, width=180,
                     image = photo6)
    newbtn6.image = photo6
    newbtn7 = Button(newwindow, text="Exit", bg="yellow", fg="red", command=newwindow.destroy, height=3, width=12)

    # Placing buttons on the window matrix
    newbtn.grid(column=0, row=6, padx=10, pady=10)
    newbtn2.grid(column=1, row=6, padx=10, pady=10)
    newbtn3.grid(column=2, row=6, padx=10, pady=10)
    newbtn4.grid(column=0, row=7, padx=10, pady=10)
    newbtn5.grid(column=1, row=7, padx=10, pady=10)
    newbtn6.grid(column=2, row=7, padx=10, pady=10)
    newbtn7.grid(column=1, row=8, padx=10, pady=20)


# Creating Level 2 game top level window
def create_window2():
    newwindow2 = tk.Toplevel(window)
    newwindow2.iconbitmap(r'icon.ico')
    newwindow2.configure(background='grey')  # Adding background colour
    newwindow2.title("Level 2")
    newwindow2.geometry('800x600')
    # Making widget resize and relocate when changing window size
    newwindow2.grid_columnconfigure(0, weight=1)
    newwindow2.grid_columnconfigure(1, weight=1)
    newwindow2.grid_columnconfigure(2, weight=1)
    newwindow2.grid_rowconfigure(0, weight=1)
    newwindow2.grid_rowconfigure(1, weight=1)
    # Adding label with game title and making label background transparent
    newlbl2 = Label(newwindow2, text="Which animals cant't fly? Describe", font=("Arial Bold", 16),
                    background='grey')
    # The window can ba considered as a matrix
    # Placing label in the desired position in the window and setting the distance between label and other widgets
    newlbl2.grid(column=1, row=0, padx=10, pady=10)

    # Creating pop up windows functions when clicking on game images (Winning or Losing image)
    def clicked_right():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow2)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl2_unicorn.wav')
        print("Finished the result is written to Lvl2_unicorn.wav")

    def clicked_right2():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow2)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl2_penguin.wav')
        print("Finished the result is written to Lvl2_penguin.wav")

    def clicked_wrong():
        messagebox.showinfo('Try again', 'The selected answer is not the right one', parent=newwindow2)

    # Storing images to be used on the game buttons
    image1 = Image.open("bird1.jpg")
    photo1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("bird5.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("bird3.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("notbird.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    image5 = Image.open("bird4.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    image6 = Image.open("notbird1.jpg")
    photo6 = ImageTk.PhotoImage(image6)

    # Storing images to be used on the game buttons
    newbtn = Button(newwindow2, bg="orange", command=clicked_wrong, height=180, width=180,
                    image = photo1)
    newbtn.image = photo1
    newbtn2 = Button(newwindow2, bg="blue", command=clicked_wrong, height=180, width=180,
                     image = photo2)
    newbtn2.image = photo2
    newbtn3 = Button(newwindow2, bg="green", command=clicked_wrong, height=180, width=180,
                     image = photo3)
    newbtn3.image = photo3
    newbtn4 = Button(newwindow2, bg="orange", command=clicked_right, height=180, width=180,
                    image = photo4)
    newbtn4.image = photo4
    newbtn5 = Button(newwindow2, bg="blue", command=clicked_wrong, height=180, width=180,
                     image = photo5)
    newbtn5.image = photo5
    newbtn6 = Button(newwindow2, bg="green", command=clicked_right2, height=180, width=180,
                     image = photo6)
    newbtn6.image = photo6
    newbtn7 = Button(newwindow2, text="Exit", bg="yellow", fg="red", command=newwindow2.destroy, height=3, width=12)

    # Placing buttons on the window matrix
    newbtn.grid(column=0, row=6, padx=10, pady=10)
    newbtn2.grid(column=1, row=6, padx=10, pady=10)
    newbtn3.grid(column=2, row=6, padx=10, pady=10)
    newbtn4.grid(column=0, row=7, padx=10, pady=10)
    newbtn5.grid(column=1, row=7, padx=10, pady=10)
    newbtn6.grid(column=2, row=7, padx=10, pady=10)
    newbtn7.grid(column=1, row=8, padx=10, pady=20)


# Creating Level 3 game top level window
def create_window3():
    newwindow3 = tk.Toplevel(window)
    newwindow3.iconbitmap(r'icon.ico')
    newwindow3.configure(background='green')   # Adding background colour
    newwindow3.title("Level 3")
    newwindow3.geometry('800x600')
    # Making widget resize and relocate when changing window size
    newwindow3.grid_columnconfigure(0, weight=1)
    newwindow3.grid_columnconfigure(1, weight=1)
    newwindow3.grid_columnconfigure(2, weight=1)
    newwindow3.grid_rowconfigure(0, weight=1)
    newwindow3.grid_rowconfigure(1, weight=1)
    # Adding label with game title and making label background transparent
    newlbl3 = Label(newwindow3, text="Which can you drive? Explain", font=("Arial Bold", 18),
                    background='green')
    # The window can ba considered as a matrix
    # Placing label in the desired position in the window and setting the distance between label and other widgets
    newlbl3.grid(column=1, row=0, padx=10, pady=10)

    # Creating pop up windows functions when clicking on game images (Winning or Losing image)
    def clicked_right1():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow3)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl3_car.wav')
        print("Finished the result is written to Lvl3_car.wav")

    def clicked_right2():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow3)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl3_van.wav')
        print("Finished the result is written to Lvl3_van.wav")

    def clicked_right3():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow3)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl3_bus.wav')
        print("Finished the result is written to Lvl3_bus.wav")

    def clicked_right4():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow3)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl3_scooter.wav')
        print("Finished the result is written to Lvl3_scooter.wav")

    def clicked_wrong():
        messagebox.showinfo('Try again', 'The selected answer is not the right one', parent=newwindow3)

    # Storing images to be used on the game buttons
    image1 = Image.open("notcar.jpg")
    photo1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("car1.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("car2.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("notcar1.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    image5 = Image.open("car3.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    image6 = Image.open("car4.jpg")
    photo6 = ImageTk.PhotoImage(image6)

    # Storing images to be used on the game buttons
    newbtn = Button(newwindow3, bg="orange", command=clicked_wrong, height=180, width=180,
                    image = photo1)
    newbtn.image = photo1
    newbtn2 = Button(newwindow3, bg="blue", command=clicked_right1, height=180, width=180,
                     image = photo2)
    newbtn2.image = photo2
    newbtn3 = Button(newwindow3, bg="green", command=clicked_right2, height=180, width=180,
                     image = photo3)
    newbtn3.image = photo3
    newbtn4 = Button(newwindow3, bg="orange", command=clicked_wrong, height=180, width=180,
                    image = photo4)
    newbtn4.image = photo4
    newbtn5 = Button(newwindow3, bg="blue", command=clicked_right3, height=180, width=180,
                     image = photo5)
    newbtn5.image = photo5
    newbtn6 = Button(newwindow3, bg="green", command=clicked_right4, height=180, width=180,
                     image = photo6)
    newbtn6.image = photo6
    newbtn7 = Button(newwindow3, text="Exit", bg="yellow", fg="red", command=newwindow3.destroy, height=3, width=12)

    # Placing buttons on the window matrix
    newbtn.grid(column=0, row=6, padx=10, pady=10)
    newbtn2.grid(column=1, row=6, padx=10, pady=10)
    newbtn3.grid(column=2, row=6, padx=10, pady=10)
    newbtn4.grid(column=0, row=7, padx=10, pady=10)
    newbtn5.grid(column=1, row=7, padx=10, pady=10)
    newbtn6.grid(column=2, row=7, padx=10, pady=10)
    newbtn7.grid(column=1, row=8, padx=10, pady=20)


# Creating Level 4 game top level window
def create_window4():
    newwindow4 = tk.Toplevel(window)
    newwindow4.iconbitmap(r'icon.ico')
    newwindow4.configure(background='purple')   # Adding background colour
    newwindow4.title("Level 4")
    newwindow4.geometry('800x600')
    # Making widget resize and relocate when changing window size
    newwindow4.grid_columnconfigure(0, weight=1)
    newwindow4.grid_columnconfigure(1, weight=1)
    newwindow4.grid_columnconfigure(2, weight=1)
    newwindow4.grid_rowconfigure(0, weight=1)
    newwindow4.grid_rowconfigure(1, weight=1)
    # Adding label with game title and making label background transparent
    newlbl4 = Label(newwindow4, text="Which is not a cartoon? Why not?", font=("Arial Bold", 15),
                    background='purple')
    # The window can ba considered as a matrix
    # Placing label in the desired position in the window and setting the distance between label and other widgets
    newlbl4.grid(column=1, row=0, padx=10, pady=10)

    # Creating pop up windows functions when clicking on game images (Winning or Losing image)
    def clicked_right():
        messagebox.showinfo('Congratulations!', 'You selected the right answer! \n Now close this window and record '
                                                'your answer', parent=newwindow4)
        print("Please speak into the microphone")
        # Recording and storing audio after correct answer
        record_to_file('Lvl4_human.wav')
        print("Finished the result is written to Lvl4_human.wav")

    def clicked_wrong():
        messagebox.showinfo('Try again', 'The selected answer is not the right one', parent=newwindow4)

    # Storing GIFs to be used on the game buttons using the ImageButton Class
    gifbtn1 = ImageButton(newwindow4, command=clicked_wrong, compound=tk.TOP)
    gifbtn1.load('gif1.gif')
    gifbtn2 = ImageButton(newwindow4, command=clicked_wrong, compound=tk.TOP)
    gifbtn2.load('gif2.gif')
    gifbtn3 = ImageButton(newwindow4, command=clicked_wrong, compound=tk.TOP)
    gifbtn3.load('gif3.gif')
    gifbtn4 = ImageButton(newwindow4, command=clicked_right, compound=tk.TOP)
    gifbtn4.load('notgif.gif')
    gifbtn5 = ImageButton(newwindow4, command=clicked_wrong, compound=tk.TOP)
    gifbtn5.load('gif4.gif')
    gifbtn6 = ImageButton(newwindow4, command=clicked_wrong, compound=tk.TOP)
    gifbtn6.load('gif5.gif')
    newbtn7 = Button(newwindow4, text="Exit", bg="yellow", fg="red", command=newwindow4.destroy, height=3, width=12)

    # Placing buttons on the window matrix
    gifbtn1.grid(column=0, row=6, padx=10, pady=10)
    gifbtn2.grid(column=1, row=6, padx=10, pady=10)
    gifbtn3.grid(column=2, row=6, padx=10, pady=10)
    gifbtn4.grid(column=0, row=7, padx=10, pady=10)
    gifbtn5.grid(column=1, row=7, padx=10, pady=10)
    gifbtn6.grid(column=2, row=7, padx=10, pady=10)
    newbtn7.grid(column=1, row=8, padx=10, pady=20)


window.configure(background='blue')  # Setting window background colour

window.title("Identify Objects")
window.geometry('600x450')
# Making widget resize and relocate when changing window size
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
lbl = Label(window, text="Identify objects", font=("Arial Bold", 30), background='blue')
lbl.grid(row=0, column=1, columnspan=1) # Positioning label title

# Placing buttons to choose the different game level difficulty
btn = Button(window, text="Level 1", bg="orange", fg="red", command=create_window, height = 3, width = 12,
             font=("Arial Bold", 12))
btn2 = Button(window, text="Level 2", bg="grey", fg="red", command=create_window2, height = 3, width = 12,
              font=("Arial Bold", 12))
btn3 = Button(window, text="Level 3", bg="green", fg="red", command=create_window3, height = 3, width = 12,
              font=("Arial Bold", 12))
btn4 = Button(window, text="Level 4", bg="purple", fg="red", command=create_window4, height = 3, width = 12,
              font=("Arial Bold", 12))
btn5 = Button(window, text="Exit", bg="yellow", fg="red", command=window.destroy, height = 3, width = 12,
              font=("Arial Bold", 12))

# Placing buttons on the window matrix
btn.grid(column=0, row=1, padx=10, pady=10)
btn2.grid(column=2, row=1, padx=10, pady=10)
btn3.grid(column=0, row=2, padx=10, pady=10)
btn4.grid(column=2, row=2, padx=10, pady=10)
btn5.grid(column=1, row=3, padx=10, pady=10)

window.mainloop()