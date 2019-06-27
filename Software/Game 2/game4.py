from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from pygame import mixer # Library for playing sounds
from tkinter import simpledialog # Library for pop up window to type answers

# Creating root window and window icon
window = Tk()
window.iconbitmap(r'icon.ico')


# Creating Level 1 game top level window
def create_window():
    newwindow = tk.Toplevel(window)
    newwindow.configure(background='orange')  # Adding background colour
    newwindow.iconbitmap(r'icon.ico')
    newwindow.title("Animals")
    newwindow.geometry('1000x600')
    # Resizing & Repositioning widgets according to window size
    newwindow.grid_columnconfigure(0, weight=1)
    newwindow.grid_columnconfigure(1, weight=1)
    newwindow.grid_columnconfigure(2, weight=1)
    newwindow.grid_rowconfigure(0, weight=1)
    newwindow.grid_rowconfigure(1, weight=1)
    # Adding label with game title and making label background transparent
    newlbl = Label(newwindow, text="What are the sounds of these animals?", font=("Arial Bold", 16),
                   background='orange')
    # The window can ba considered as a matrix
    # Placing label in the desired position in the window and setting the distance between label and other widgets
    newlbl.grid(row=0, column=1, columnspan=2, ipadx=50)

    # Playing animals sounds and creating a pop up window where to write animal name when clicking on game images
    # Successively creating another pop up to show if the answer was right or wrong x8 times
    def clicked_image1():
        animal = 'dog'
        mixer.init()
        mixer.music.load('dog.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    def clicked_image2():
        animal = 'bird'
        mixer.init()
        mixer.music.load('bird.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    def clicked_image3():
        animal = 'cat'
        mixer.init()
        mixer.music.load('cat.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    def clicked_image4():
        animal = 'horse'
        mixer.init()
        mixer.music.load('horse.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    def clicked_image5():
        animal = 'lion'
        mixer.init()
        mixer.music.load('lion.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    def clicked_image6():
        animal = 'monkey'
        mixer.init()
        mixer.music.load('monkey.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    def clicked_image7():
        animal = 'pig'
        mixer.init()
        mixer.music.load('pig.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    def clicked_image8():
        animal = 'snake'
        mixer.init()
        mixer.music.load('snake.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow)

    # Storing images to be used on the game buttons
    image1 = Image.open("dog1.png")
    photo1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("bird1.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("cat.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("horse.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    image5 = Image.open("lion.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    image6 = Image.open("monkey.jpg")
    photo6 = ImageTk.PhotoImage(image6)
    image7 = Image.open("pig.jpg")
    photo7 = ImageTk.PhotoImage(image7)
    image8 = Image.open("snake.jpg")
    photo8 = ImageTk.PhotoImage(image8)

    # Creating buttons, corresponding pressed actions and background pictures
    newbtn = Button(newwindow, bg="orange", command=clicked_image1, height=180, width=180,
                    image = photo1)
    newbtn.image = photo1
    newbtn2 = Button(newwindow, bg="blue", command=clicked_image2, height=180, width=180,
                     image = photo2)
    newbtn2.image = photo2
    newbtn3 = Button(newwindow, bg="green", command=clicked_image3, height=180, width=180,
                     image = photo3)
    newbtn3.image = photo3
    newbtn4 = Button(newwindow, bg="orange", command=clicked_image4, height=180, width=180,
                    image = photo4)
    newbtn4.image = photo4
    newbtn5 = Button(newwindow, bg="blue", command=clicked_image5, height=180, width=180,
                     image = photo5)
    newbtn5.image = photo5
    newbtn6 = Button(newwindow, bg="green", command=clicked_image6, height=180, width=180,
                     image = photo6)
    newbtn6.image = photo6
    newbtn7 = Button(newwindow, bg="green", command=clicked_image7, height=180, width=180,
                     image = photo7)
    newbtn7.image = photo7
    newbtn8 = Button(newwindow, bg="green", command=clicked_image8, height=180, width=180,
                     image = photo8)
    newbtn8.image = photo8
    newbtn9 = Button(newwindow, text="Exit", bg="yellow", fg="red", command=newwindow.destroy, height=3, width=12)

    # Placing buttons on the window matrix
    newbtn.grid(column=0, row=1, padx=0, pady=10)
    newbtn2.grid(column=1, row=1, padx=0, pady=10)
    newbtn3.grid(column=2, row=1, padx=0, pady=10)
    newbtn4.grid(column=3, row=1, padx=0, pady=10)
    newbtn5.grid(column=0, row=2, padx=10, pady=10)
    newbtn6.grid(column=1, row=2, padx=10, pady=10)
    newbtn7.grid(column=2, row=2, padx=10, pady=10)
    newbtn8.grid(column=3, row=2, padx=10, pady=10)
    newbtn9.grid(row=3, column=1, columnspan=2)


# Creating Level 2 game top level window
def create_window2():
    newwindow2 = tk.Toplevel(window)
    newwindow2.iconbitmap(r'icon.ico')
    newwindow2.configure(background='green')  # Adding background colour
    newwindow2.title("Animals")
    newwindow2.geometry('1000x600')
    # Resizing & Repositioning widgets according to window size
    newwindow2.grid_columnconfigure(0, weight=1)
    newwindow2.grid_columnconfigure(1, weight=1)
    newwindow2.grid_columnconfigure(2, weight=1)
    newwindow2.grid_rowconfigure(0, weight=1)
    newwindow2.grid_rowconfigure(1, weight=1)
    # Adding label with game title and making label background transparent
    newlbl2 = Label(newwindow2, text="To which animals corresponds these sounds? \n"
                                     "Click on the boxes and write your guess", font=("Arial Bold", 16),
                    background='green')
    # The window can ba considered as a matrix
    # Placing label in the desired position in the window and setting the distance between label and other widgets
    newlbl2.grid(row=0, column=1, columnspan=2, ipadx=50)

    # Playing animals sounds and creating a pop up window where to write animal name when clicking on game images
    # Successively creating another pop up to show if the answer was right or wrong x8 times
    def clicked_image1():
        animal = 'dog'
        mixer.init()
        mixer.music.load('dog.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    def clicked_image2():
        animal = 'bird'
        mixer.init()
        mixer.music.load('bird.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    def clicked_image3():
        animal = 'cat'
        mixer.init()
        mixer.music.load('cat.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    def clicked_image4():
        animal = 'horse'
        mixer.init()
        mixer.music.load('horse.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    def clicked_image5():
        animal = 'lion'
        mixer.init()
        mixer.music.load('lion.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    def clicked_image6():
        animal = 'monkey'
        mixer.init()
        mixer.music.load('monkey.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    def clicked_image7():
        animal = 'pig'
        mixer.init()
        mixer.music.load('pig.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    def clicked_image8():
        animal = 'snake'
        mixer.init()
        mixer.music.load('snake.mp3')
        mixer.music.play()
        name = simpledialog.askstring('Sound Playing', 'What\'s the name of this animal?', parent=newwindow2)
        if name.lower() in animal.lower():
            if name.lower() != '':
                messagebox.showinfo('Well Done', 'That\'s right!', parent=newwindow2)
            else:
                messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)
        else:
            messagebox.showinfo('Try again', 'Wrong Answer', parent=newwindow2)

    # Creating buttons and corresponding actions
    newbtn = Button(newwindow2, text="Sound 1", fg="black", bg="orange", command=clicked_image1, height=3, width=15,
                    font=("Arial Bold", 12))
    newbtn2 = Button(newwindow2, text="Sound 7", fg="black", bg="blue", command=clicked_image2, height=3, width=15,
                     font=("Arial Bold", 12))
    newbtn3 = Button(newwindow2, text="Sound 8", fg="black", bg="red", command=clicked_image3, height=3, width=15,
                     font=("Arial Bold", 12))
    newbtn4 = Button(newwindow2, text="Sound 6", fg="black", bg="grey", command=clicked_image4, height=3, width=15,
                     font=("Arial Bold", 12))
    newbtn5 = Button(newwindow2, text="Sound 5", fg="black", bg="purple", command=clicked_image5, height=3, width=15,
                     font=("Arial Bold", 12))
    newbtn6 = Button(newwindow2, text="Sound 4", fg="black", bg="yellow", command=clicked_image6, height=3, width=15,
                     font=("Arial Bold", 12))
    newbtn7 = Button(newwindow2, text="Sound 2", fg="black", bg="brown", command=clicked_image7, height=3, width=15,
                     font=("Arial Bold", 12))
    newbtn8 = Button(newwindow2, text="Sound 3", fg="black", bg="white", command=clicked_image8, height=3, width=15,
                     font=("Arial Bold", 12))
    newbtn9 = Button(newwindow2, text="Exit", bg="yellow", fg="black", command=newwindow2.destroy, height=3, width=12,
                     font=("Arial Bold", 12))

    # Placing buttons on the window matrix (randomizing buttons order to increase difficulty)
    newbtn.grid(column=0, row=1, padx=0, pady=10)
    newbtn2.grid(column=2, row=2, padx=10, pady=10)
    newbtn3.grid(column=3, row=2, padx=10, pady=10)
    newbtn4.grid(column=1, row=2, padx=10, pady=10)
    newbtn5.grid(column=0, row=2, padx=10, pady=10)
    newbtn6.grid(column=3, row=1, padx=0, pady=10)
    newbtn7.grid(column=1, row=1, padx=0, pady=10)
    newbtn8.grid(column=2, row=1, padx=0, pady=10)
    newbtn9.grid(row=3, column=1, columnspan=2)

window.columnconfigure(0, weight=1)  # Centering the widgets at the centre of the window


window.configure(background='blue')  # Setting window background colour

window.title("Recognise/Imitate Sounds")
window.geometry('600x450')

lbl = Label(window, text="Recognise/Imitate Sounds", font=("Arial Bold", 30), background='blue')
lbl.grid(column=0, row=0, padx=10, pady=10)

# Placing buttons to choose the different game level difficulty
btn = Button(window, text="Recognise/Imitate Animals sounds", bg="orange", fg="black", command=create_window,
             height = 3, width = 27, font=("Arial Bold", 12))
btn2 = Button(window, text="Recognise Sounds", bg="green", fg="black", command=create_window2, height = 3, width = 27,
              font=("Arial Bold", 12))
btn3 = Button(window, text="Exit", bg="yellow", fg="black", command=window.destroy, height = 3, width = 27,
              font=("Arial Bold", 12))

# Placing buttons on the window matrix
btn.grid(column=0, row=6, padx=10, pady=10)
btn2.grid(column=0, row=7, padx=10, pady=10)
btn3.grid(column=0, row=8, padx=10, pady=10)

window.mainloop()