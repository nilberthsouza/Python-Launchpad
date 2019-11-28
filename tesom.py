from tkinter import *
import os
import pygame
from pygame.mixer import Sound

#functions

def sound_maker(sound_name):
    #função generica que é executada dentro de cada função executada pelo botão
    pygame.init()
    pygame.mixer.music.load(sound_name)
    return pygame.mixer.music.play()

def sound_maker_one():
    sound = "sons/Snare.wav"
    sound_maker(sound)

def sound_maker_two():
    sound = "sons/Crashprato.wav"
    sound_maker(sound)

def sound_maker_three():
    sound = "sons/hithatclose.wav"
    sound_maker(sound)

def sound_maker_four():
    sound = "sons/kick1.wav"
    sound_maker(sound)

def sound_maker_five():
    sound = "sons/ride.wav"
    sound_maker(sound)

def sound_maker_six():
    sound = "sons/tom1.wav"
    sound_maker(sound)




app = Tk()

#buttons
button_one = Button(app, text='sound 1', width=20, command=sound_maker_one)
button_one.grid(row=1, column=1, pady=20,padx=20)

button_two = Button(app, text='sound 2', width=20, command=sound_maker_two)
button_two.grid(row=1, column=2, pady=20,padx=20)

button_three = Button(app, text='sound 3', width=20, command=sound_maker_three)
button_three.grid(row=1, column=3, pady=20,padx=20)

button_four = Button(app, text='sound 4', width=20, command=sound_maker_four)
button_four.grid(row=2, column=1, pady=20,padx=20)

button_five = Button(app, text='sound 5', width=20, command=sound_maker_five)
button_five.grid(row=2, column=2, pady=20,padx=20)

button_six = Button(app, text='sound 6', width=20, command=sound_maker_six)
button_six.grid(row=2, column=3, pady=20,padx=20)


app.title('music creator')
app.geometry('700x400')
app.mainloop()

pygame.key.get_pressed()
