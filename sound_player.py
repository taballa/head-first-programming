from sound_panel import create_gui
from Tkinter import *
import pygame.mixer

mixer = pygame.mixer

app = Tk()
app.title("Head First Mix")

create_gui(app, mixer, "50459_M_RED_Nephlimizer.wav")
