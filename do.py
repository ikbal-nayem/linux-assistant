from voice_lab import voice_recognizer


class brightness:
    def __inti__(self):
        self.voice = voice_recognizer()

    def up(self):
        voice = voice_recognizer()
        try:
            with open('/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight/brightness', 'r') as f:
                value = f.read()
            value = int(value) + 50
            if value > 950:
                print('brightness maximum')
                voice.say(text="brightness maximum")
            else:
                with open('/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight/brightness', 'w') as f:
                    f.write(str(value))
                print("Done")
                voice.say(audio="done.mp3")
        except:
            print('something went wrong at brightness up section!!!')
            voice.say(text='something went wrong at brightness up section!!!')

    def down(self):
        voice = voice_recognizer()
        try:
            with open('/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight/brightness', 'r') as f:
                value = f.read()
            value = int(value) - 50
            if value < 150:
                print('brightness maximum')
                voice.say(text="brightness minimum")
            else:
                with open('/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight/brightness', 'w') as f:
                    f.write(str(value))
                print("Done")
                voice.say(audio="done.mp3")
        except:
            print('something went wrong at brightness down section!!!')
            voice.say(text='something went wrong at brightness down section!!!')

    def to(self, new_value):
        voice = voice_recognizer()
        try:
            v = int(new_value[0:-1])*10
            if v > 950:
                value = 950
            elif v < 150:
                value =150
            else:
                value = v
            with open('/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight/brightness', 'w') as f:
                f.write(str(value))
            print("Done")
            voice.say(audio="done.mp3")
        except:
            print('something went wrong at brightness up/down section!!!')
            voice.say(text='something went wrong at brightness up/down section!!!')

class date_time:

    def __init__(self):
        import datetime, time
        self.voice = voice_recognizer()
        self.time = datetime.datetime.now()
        self.date = time.asctime()

    def Date(self):
        d = self.date.split()[0]
        day = {"Mon":"Monday", "Tue":"Tuesday", "Wed":"Wednesday", "Thu":"Thursday", "Fri":"Friday", "Sat":"Saturday", "Sun":"Sunday"}
        date = self.date.split()[2]
        mon = self.date.split()[1]
        month = {"Jan":"January", "Feb":"February", "Mar":"March", "Apr":"April", "May":"May", "Jun":"June", "Jul":"July", "Aug":"August", "Sep":"September", "Sept":"september", "Oct":"October", "Nov":"November", "Dec":"December"}
        year = self.date.split()[4]
        form = "It's {}, {} {}, {}".format(day[d], date, month[mon], year)
        print(form)
        self.voice.say(text=form)

    def Time(self):
        form = "The time is {}:{} {}".format(self.time.hour%12 if self.time.hour > 12 else self.time.hour, self.time.minute, 'PM' if self.time.hour >= 12 else 'AM')
        print(form)
        self.voice.say(text=form)

class weather:

    def __init__(self):
        from weather import Weather
        self.voice = voice_recognizer()
        self.weather = Weather(unit='c')

    def update(self):
        location = self.weather.lookup_by_location('dhaka, bangladesh')
        condition = location.condition
        txt = "It's a {} day!! The current temperature of your location is {} degree celsius!!! have a good day!!!".format(condition.text, condition.temp)
        print(txt)
        self.voice.say(text=txt)
