from Tkinter import *

class SoundPanel(Frame):
    """docstring for SoundPanel"""
    def __init__(self, app, mixer, sound_file):
        # super(SoundPanel, self).__init__() # automatic adds
        Frame.__init__(self, app) # NOTE: why initialization Frame and use app parameter?
        self.track = mixer.Sound(sound_file) # NOTE: why everyone variable used self?
        self.track_playing = IntVar()
        # self.app = app # automatic adds
        track_button = Checkbutton(self, variable = self.track_playing, command = self.track_toggle, text = sound_file) # NOTE: why used self not use app
        track_button.pack(side = LEFT)

        # NOTE: 看来是，变量用 self 开头，volume_scale 和 track_button 之类的组件不用 self 开头
        self.volume = DoubleVar()
        self.volume.set(self.track.get_volume())
        volume_scale = Scale(
            self,
            variable = self.volume,
            from_ = 0.0,
            to = 1.0,
            resolution = 0.1,
            command = self.change_volume,
            label = "Volume",
            orient = HORIZONTAL)
        volume_scale.pack(side = RIGHT)

    def track_toggle(self):
        if self.track_playing.get() == 1:
            self.track.play(loops = -1)
        else:
            self.track.stop()

    def change_volume(self, v):
        self.track.set_volume(self.volume.get())


def create_gui(app, mixer, sound_file):
    track = mixer.Sound(sound_file)

    def track_toggle():
        if track_playing.get() == 1:
            track.play(loops = -1)
        elif track_playing.get() == 0:
            track.stop()

    def change_volume(v):
        track.set_volume(volume.get())

    track_playing = IntVar()
    Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file).pack(side = LEFT)

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
    volume_scale.pack(side = RIGHT)


