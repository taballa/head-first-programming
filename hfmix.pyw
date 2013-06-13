from Tkinter import *
import pygame.mixer
from tkMessageBox import askokcancel

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)

def track_stop():
    track.stop()

def track_start():
    track.play(loops = -1)

def shutdown():
    track.stop()
    if askokcancel(title="Are you sure?", message= "Do you really want to quit?"):
        app.destroy()

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    elif track_playing.get() == 0:
        track.stop()

app = Tk()
app.title("Head First Mix")

stop_botton = Button(app, command = track_stop, text = "Stop")
stop_botton.pack(side = RIGHT)

track_playing = IntVar()
Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file).pack()

start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

app.geometry('255x100+200+100')
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()