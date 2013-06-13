from Tkinter import *
import pygame.mixer

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)

def track_stop():
    track.stop()

def track_start():
    track.play(loops = -1)

app = Tk()
app.title("Head First Mix")

stop_botton = Button(app, command = track_stop, text = "Stop")
stop_botton.pack(side = RIGHT)

start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

app.geometry('255x100+200+100')
app.mainloop()