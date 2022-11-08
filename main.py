import time
from kivy.uix.boxlayout import BoxLayout

import threading

from kivy.app import App

from moviepy.editor import *


class MyLayout(BoxLayout):
    def selected(self, filename):
        self.filename = filename
        self.ids.my_video.source = self.filename[0]

    def convert_to_mp3(self):
        videofile = self.filename[0]
        audiofile = 'myaudio.mp3'

        videoclip = VideoFileClip(videofile)
        audioclip = videoclip.audio
        audioclip.write_audiofile(audiofile)

        while True:
            self.ids.show_process.value += 1
            time.sleep(.01)
            if self.ids.show_process.value >= 100:
                break

        videoclip.close()
        audioclip.close()

    def run_threading(self):
        t = threading.Thread(target=self.convert_to_mp3)
        t.start()


class Mp3RH(App):
    pass


Mp3RH().run()
