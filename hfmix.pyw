from Tkinter import *
import pygame.mixer
from tkMessageBox import askokcancel

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)

def track_stop():
    track.stop()
    track_playing.set(0)

def track_start():
    track.play(loops = -1)
    track_playing.set(1)

def shutdown():
    track.stop()
    if askokcancel(title="Are you sure?", message= "Do you really want to quit?"):
        app.destroy()

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    elif track_playing.get() == 0:
        track.stop()

def change_volume(v):
    track.set_volume(volume.get())

app = Tk()
app.title("Head First Mix")

volume = DoubleVar()
volume.set(track.get_volume())
volume_scale = Scale(
    app,
    variable = volume,
    from_ = 0.0,
    to = 1.0,
    resolution = 0.1,
    command = change_volume,
    label = "Volume",
    orient = HORIZONTAL)

volume_scale.pack()

stop_botton = Button(app, command = track_stop, text = "Stop")
stop_botton.pack(side = RIGHT)

track_playing = IntVar()
Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file).pack()

start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

app.geometry('255x100+200+100')
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()