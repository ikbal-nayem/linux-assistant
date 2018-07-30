#!/usr/bin/python3

import voice_lab
import operation_section as op_sec

voice = voice_lab.voice_recognizer()
print("Hey how may I help you?")
voice.say(audio="hay_how_may_i_help_you.mp3")
no = ['no', 'nothing', 'not', 'bye', 'goodbye', 'stop', 'shut up', 'nothing else', 'cancel',
      'f*** yourself', 'f*** off', 'f*** of', 'no thanks', 'now f*** yourself']

while True:
    a = voice.get_voice()
    txt = voice.recognizer(a)
    if txt == "voice error.":
        continue
    elif txt in no:
        voice.say(audio="okay_see_you_later.mp3")
        break
    # voice.say(text=txt)
    o = op_sec.operations(txt)
    o.analysis()
    print("Anything else?")
    voice.say(audio="anything_else.mp3")
