# Partially following: https://sefiks.com/2018/01/10/real-time-facial-expression-recognition-on-streaming-data/


# Importing all the necessary libraries
import numpy as np
import cv2
from keras.preprocessing import image
from keras.models import model_from_json
from tkinter import *
from tkinter import messagebox
import queue
from PIL import ImageTk, Image


# Creating a queue to use the value of the variable emotion detected simultaneously both in the video recording gui and
# in the instruction/result GUI
q = queue.Queue()


# Defying the main function to run the game
def videostream():
    # Creating secondary GUI, setting basic properties and designing labels
    window = Tk()
    window.geometry('430x370')
    window.configure(background='blue')
    window.title("Computer Vision game")
    imageback = Image.open("faces.jpg")
    photo = ImageTk.PhotoImage(imageback)
    label9 = Label(image=photo)
    label9.imageback = photo
    label9.grid(row=0, column= 1)
    lb2 = Label(window, text='Make this expression: ........')
    lb2.config(font=("Courier", 16))
    lb2.grid(column=1, row=2)

    # Importing face recognition trained model and dependacies (initializing camera GUI)
    # Sources: https://github.com/serengil/tensorflow-101/blob/master/model/facial_expression_model_structure.json
    # https://github.com/serengil/tensorflow-101/blob/master/model/facial_expression_model_weights.h5
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    model = model_from_json(open("facial_expression_model_structure.json", "r").read())
    model.load_weights('facial_expression_model_weights.h5')  # load weights
    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

    # Loop to control secondary GUI. Create a list (emo) of emotions to imitate and loop through it.
    # Send the detected facial expressions and check if the correspond
    # with the requested ones, if so message-box appears to congratulate and we move to the next expression.
    # Repeat this process for 5qqqq times and then congratulate the user
    emo = ['angry', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    emo = np.array(emo)
    for i in range(0,5):
        for k in range(0, len(emo)):
            emotion = "-1"
            faces = ()
            # If a face is not recorded keep the stream video running
            while faces == ():
                ret, img = cap.read()
                cv2.imshow('img', img)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                # Creating a label to inform the user if the face has been detected at all or not
                lb3 = Label(window, text=' No face detected ')
                lb3.config(font=("Courier", 18))
                lb3.grid(column=1, row=1)
                window.update()
            lb2 = Label(window, text=('Make this expression:', emo[k]))
            lb2.config(font=("Courier", 16))
            lb2.grid(column=1, row=2)
            lb3.config(text = "Face been detected",font=("Courier", 18))
            window.update()

            while emotion != emo[k]:
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                # If a face is not recorded keep the stream video running
                while faces == ():
                    ret, img = cap.read()
                    cv2.imshow('img', img)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    # Creating a label to inform the user if the face has been detected at all or not
                    lb3 = Label(window, text=(' No face detected '))
                    lb3.config(font=("Courier", 18))
                    lb3.grid(column=1, row=1)
                    window.update()
                lb3.config(text = "Face been detected", font=("Courier", 18))
                window.update()
                # Code used to detect the face, draw a rectangle around it and write the expression name
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # draw rectangle to main image

                    detected_face = img[int(y):int(y + h), int(x):int(x + w)]  # crop detected face
                    detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)  # transform to gray scale
                    detected_face = cv2.resize(detected_face, (48, 48))  # resize to 48x48

                    img_pixels = image.img_to_array(detected_face)
                    img_pixels = np.expand_dims(img_pixels, axis=0)

                    img_pixels /= 255  # pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

                    predictions = model.predict(img_pixels)  # store probabilities of 7 expressions

                    # find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
                    max_index = np.argmax(predictions[0])
                    emotion = emotions[max_index]
                    q.put(emotion)
                    # write emotion text above rectangle
                    cv2.putText(img, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                emotion = q.get()

                if emotion == emo[k]:
                    messagebox.showinfo("Well Done!", "Congratulation!")
                    window.update()
                # process on detected face end
                cv2.imshow('img', img)

                if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
                    cv2.destroyAllWindows()
                    cap.release()
                    window.destroy()

        if i == 4:
            # Game finished message
            messagebox.showinfo("Well Done!", "Game finished")
            window.update()
            cv2.destroyAllWindows()
            cap.release()
            window.destroy()

    window.mainloop()

    # Close all windows if the user press q to quit to game
    cv2.destroyAllWindows()
    cap.release()

# Run game function to start the game
videostream()