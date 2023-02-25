from pygame import mixer
from tkinter import *

mixer.init() # initializing the mixer

mixer.music.load("/media/fady/MiNa/eminem/2-River.mp3") # loading the song
mixer.music.play() # playing the song

mixer.music.stop() # closing the mixer