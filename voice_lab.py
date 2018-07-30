import speech_recognition as sr
from pygame import mixer
from gtts import gTTS
import os, sys, time


class voice_recognizer:

    def __init__(self):
        self.sound_dir = '/root/Program/projrct/voice_command/sounds'
        self.voice_dir = '/root/Program/projrct/voice_command/voice'
        self.r = sr.Recognizer()
        mixer.init()
        self.start = mixer.Sound(os.path.join(self.sound_dir, 'start_rec.ogg'))
        self.stop = mixer.Sound(os.path.join(self.sound_dir, 'stop_rec.ogg'))

    # def introduce(self):
    #     print('Hey!!! who are you?')
    #     self.say(audio='hey!_who_are_you?.mp3')
    #     audio = self.get_voice()
    #     return self.recognizer(audio)

    def get_voice(self):
        mixer.Sound.play(self.start)
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source=source)
            print('Listening...')
            audio = self.r.listen(source)
        mixer.Sound.play(self.stop)
        return audio

    def recognizer(self, audio):
        audio = audio
        try:
            txt = self.r.recognize_google(audio)
            print(txt)
        except sr.UnknownValueError:
            txt = "voice error."
            print(txt)
            self.say(audio="sorry_i_didnt_catch_you.mp3")
        except sr.RequestError:
            print("NO internet connection...! please try again later.")
            self.say(audio="connection_error.mp3")
            sys.exit()
        return txt

    def say(self, text=None, audio=None):
        if text != None:
            try:
                tts = gTTS(text)
                tts.save(os.path.join(self.voice_dir, "temp.mp3"))
                Audio = "temp.mp3"
            except:
                print("NO internet connection...! please try again later.")
                self.say(audio="connection_error.mp3")
                sys.exit()
        else:
            Audio = audio
        Audio = os.path.join(self.voice_dir, Audio)
        mixer.music.load(Audio)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)
        # os.remove(os.path.join(self.voice_dir, "temp.mp3"))
