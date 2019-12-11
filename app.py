from tkinter import *
import pygame
from pygame.mixer import Sound
import tkinter as tk
from tkinter import filedialog

#aplicaçao principal/Classe GUI

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title = ("Python Launchpad")
        #Width height
        master.geometry("700x350")
        #create widgets and grid
        self.create_widgets()
        #selected button item var
        self.SOUND ="" 
    def create_widgets(self):
        #button one
        self.button_one = tk.Button(self.master,bg="blue" , width=15,height=7, command=self.sound_maker_one)
        self.button_one.grid(row=1, column=1, pady=10,padx=10)

        #button two
        self.button_two = tk.Button(self.master, text='CRASH', width=7,height=7, command=self.sound_maker_two)
        self.button_two.grid(row=1, column=2, pady=10,padx=10)
        #button three

        self.button_three = tk.Button(self.master, text='HIHATc', width=20, command=self.sound_maker_three)
        self.button_three.grid(row=1, column=3, pady=20,padx=20)

        #button_four
        self.button_four = tk.Button(self.master, text='KICK', width=20, command=self.sound_maker_four)
        self.button_four.grid(row=2, column=1, pady=20,padx=20)

        #button_five
        self.button_five = tk.Button(self.master, text='RIDE', width=20, command=self.sound_maker_five)
        self.button_five.grid(row=2, column=2, pady=20,padx=20)

        #button_six
        self.button_six = tk.Button(self.master, text='', width=20, command=self.sound_maker_six)
        self.button_six.grid(row=2, column=3, pady=20,padx=20)

        #button_seven
        self.button_seven= tk.Button(self.master, text='', width=20, command=self.sound_maker_seven)
        self.button_seven.grid(row=3, column=1, pady=20,padx=20)

        #button_eight
        self.button_eight = tk.Button(self.master, text='', width=20, command=self.sound_maker_eight)
        self.button_eight.grid(row=3, column=2, pady=20,padx=20)

        #button_nine
        self.button_nine = tk.Button(self.master, text='', width=20, command=self.sound_maker_nine)
        self.button_nine.grid(row=3, column=3, pady=20,padx=20)

        #button_ten
        self.button_ten = tk.Button(self.master, text='', width=20, command=self.sound_maker_ten)
        self.button_ten.grid(row=4, column=1, pady=20,padx=20)

        #buton eleven
        self.button_eleven = tk.Button(self.master, text='', width=20, command=self.sound_maker_eleven)
        self.button_eleven.grid(row=4, column=2, pady=20,padx=20)

        #button twelve
        self.button_twelve = tk.Button(self.master, text='', width=20, command=self.sound_maker_twelve)
        self.button_twelve.grid(row=4, column=3, pady=20,padx=20)

 
    def sound_define(self):
        global file_path
        file_path = filedialog.askopenfilename()
        return file_path


    def sound_define_one(self):
        global SOUND
        SOUND = self.sound_define()
        return SOUND

    def sound_maker(self,sound_name):
        pygame.init()
        pygame.mixer.music.load(sound_name)
        return pygame.mixer.music.play()

    def sound_maker_one(self):
        sound = "sons/Snare.wav"
        self.sound_maker(sound)

    def sound_maker_two(self):
        sound = "sons/Crashprato.wav"
        self.sound_maker(sound)

    def sound_maker_three(self):
        sound = "sons/hithatclose.wav"
        self.sound_maker(sound)


    def sound_maker_four(self):
        sound = "sons/kick1.wav"
        self.sound_maker(sound)

    def sound_maker_five(self):
        sound = "sons/ride.wav"
        self.sound_maker(sound)

    def sound_maker_six(self):
        sound = "sons/tom1.wav"
        self.sound_maker(sound)

    def sound_maker_seven(self):
        sound = "sons/Snare.wav"
        self.sound_maker(sound)

    def sound_maker_eight(self):
        sound = "sons/Crashprato.wav"
        self.sound_maker(sound)

    def sound_maker_nine(self):
        sound = "sons/hithatclose.wav"
        self.sound_maker(sound)

    def sound_maker_ten(self):
        sound = "sons/kick1.wav"
        self.sound_maker(sound)

    def sound_maker_eleven(self):
        sound = "sons/ride.wav"
        self.sound_maker(sound)

    def sound_maker_twelve(self):
        sound = "sons/tom1.wav"
        self.sound_maker(sound)
root = tk.Tk()
app= Application(master=root)
root["bg"]="black"
app.mainloop()
