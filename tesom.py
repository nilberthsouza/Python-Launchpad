from tkinter import *

def sound_maker_one():
    print("sound_maker_one")

def sound_maker_two():
    print("sound_maker_two")

def sound_maker_three():
    print("sound_maker_three")

def sound_maker_four():
    print("sound_maker_four")

def sound_maker_five():
    print("sound_maker_five")

def sound_maker_six():
    print("sound_maker_six")


app = Tk()

#buttons
button_one = Button(app, text='sound 1', width=20, command=sound_maker_one)
button_one.grid(row=0, column=0, pady=20)

button_two = Button(app, text='sound 2', width=20, command=sound_maker_two)
button_two.grid(row=0, column=1, pady=20)

button_three = Button(app, text='sound 3', width=20, command=sound_maker_three)
button_three.grid(row=0, column=2, pady=20)

button_four = Button(app, text='sound 4', width=20, command=sound_maker_four)
button_four.grid(row=1, column=0, pady=20)

button_five = Button(app, text='sound 5', width=20, command=sound_maker_five)
button_five.grid(row=1, column=1, pady=20)

button_six = Button(app, text='sound 6', width=20, command=sound_maker_six)
button_six.grid(row=1, column=2, pady=20)


app.title('music creator')
app.geometry('700x400')
app.mainloop()

'''import pygame
import os
from pygame.mixer import Sound

pygame.init()
clip = os.path.abspath("palmas.wav")

def load_mus():
    pygame.mixer.music.load("palmas.wav")
    pygame.mixer.music.play()
    pygame.mixer.set_volume(4)
    pass

load_mus()

'''
