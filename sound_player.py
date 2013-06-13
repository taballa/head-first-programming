from sound_panel import *
from Tkinter import *
import pygame.mixer

mixer = pygame.mixer
mixer.init()

app = Tk()
app.title("Head First Mix")

panel = SoundPanel(app, mixer, "50459_M_RED_Nephlimizer.wav")
panel.pack()
panel = SoundPanel(app, mixer, "49119_M_RED_HardBouncer.wav")
panel.pack()

create_gui(app, mixer, "50459_M_RED_Nephlimizer.wav")
create_gui(app, mixer, "49119_M_RED_HardBouncer.wav")

app.mainloop()