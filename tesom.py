from tkinter import *
import os
import pygame
from pygame.mixer import Sound

#functions
def sound_maker(sound_name):
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

def sound_maker_seven():
    sound = "sons/Snare.wav"
    sound_maker(sound)

def sound_maker_eight():
    sound = "sons/Crashprato.wav"
    sound_maker(sound)

def sound_maker_nine():
    sound = "sons/hithatclose.wav"
    sound_maker(sound)

def sound_maker_ten():
    sound = "sons/kick1.wav"
    sound_maker(sound)

def sound_maker_eleven():
    sound = "sons/ride.wav"
    sound_maker(sound)

def sound_maker_twelve():
    sound = "sons/tom1.wav"
    sound_maker(sound)

app = Tk()

#buttons


button_one = Button(app, text='SNARE', width=20, command=sound_maker_one)

button_two = Button(app, text='CRASH', width=20, command=sound_maker_two)

button_three = Button(app, text='HIHATc', width=20, command=sound_maker_three)

button_four = Button(app, text='KICK', width=20, command=sound_maker_four)

button_five = Button(app, text='RIDE', width=20, command=sound_maker_five)

button_six = Button(app, text='', width=20, command=sound_maker_six)

button_seven= Button(app, text='', width=20, command=sound_maker_seven)

button_eight = Button(app, text='', width=20, command=sound_maker_eight)

button_nine = Button(app, text='', width=20, command=sound_maker_nine)

button_ten = Button(app, text='', width=20, command=sound_maker_ten)

button_eleven = Button(app, text='', width=20, command=sound_maker_eleven)

button_twelve = Button(app, text='', width=20, command=sound_maker_twelve)

#grids
button_one.grid(row=1, column=1, pady=20,padx=20)

button_two.grid(row=1, column=2, pady=20,padx=20)

button_three.grid(row=1, column=3, pady=20,padx=20)


button_four.grid(row=2, column=1, pady=20,padx=20)

button_five.grid(row=2, column=2, pady=20,padx=20)

button_six.grid(row=2, column=3, pady=20,padx=20)


button_seven.grid(row=3, column=1, pady=20,padx=20)

button_eight.grid(row=3, column=2, pady=20,padx=20)

button_nine.grid(row=3, column=3, pady=20,padx=20)


button_ten.grid(row=4, column=1, pady=20,padx=20)

button_eleven.grid(row=4, column=2, pady=20,padx=20)

button_twelve.grid(row=4, column=3, pady=20,padx=20)

#colors

app["bg"]="purple"

button_one["fg"] ="black"
button_one["bg"] ="white"

button_two["fg"] ="black"
button_two["bg"] ="white"

button_three["fg"] ="black"
button_three["bg"] ="white"

button_four["fg"] ="black"
button_four["bg"] ="white"

button_five["fg"] ="black"
button_five["bg"] ="white"

button_six["fg"] ="black"
button_six["bg"] ="white"

button_seven["fg"] ="black"
button_seven["bg"] ="white"

button_eight["fg"] ="black"
button_eight["bg"] ="white"

button_nine["fg"] ="black"
button_nine["bg"] ="white"

button_ten["fg"] ="black"
button_ten["bg"] ="white"

button_eleven["fg"] ="black"
button_eleven["bg"] ="white"

button_twelve["fg"] ="black"
button_twelve["bg"] ="white"


#run project
app.title('Python Launchpad')
app.geometry('700x400')
app.mainloop()

