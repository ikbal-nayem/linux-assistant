import do
from voice_lab import voice_recognizer


class operations:

    def __init__(self, text):
        self.voice = voice_recognizer()
        if len(text.split()) != 1:
            self.command = text.split()[0]
            j = []
            for i in range(1, len(text.split())):
                j.append(text.split()[i])
            self.task = ' '.join(j)
        else:
            self.command = text

    def analysis(self):
        commands = ["brightness", "weather", "whats", "what", "what\'s", "how", "date", "time"]
        if self.command in commands:
                                                    ### brightness ###
            if self.command == 'brightness':
                x = self.task.split()
                op = do.brightness()
                if len(self.task.split()) == 1:
                    if self.task == 'app' or self.task == 'up':
                        op.up()
                    elif self.task == 'down':
                        op.down()
                    elif '%' in self.task:
                        op.to(self.task)
                elif x[0]=='up' or x[0]=='down' and x[1]=='to' or x[1]=='into' or x[1]=='in':
                    op.to(x[-1])
                else:
                    print("Command error")
                    self.voice.say(text="Command error!!!")

            elif self.command == 'date':
                date = do.date_time()
                date.Date()

            elif self.command == 'time':
                t = do.date_time()
                t.Time()

            elif self.command == 'weather':
                w = do.weather()
                w.update()

            elif self.command=='what' or self.command=='whats' or self.command=="what\'s" or self.command=='how':
                self.what()

        else:
            print('command not found!')
            self.voice.say(audio='command_not_found.mp3')

    def what(self):
        if 'about today' in self.task:
            w = do.weather()
            d = do.date_time()
            d.Date()
            w.update()

        elif 'date' in self.task:
            d = do.date_time()
            d.Date()

        elif 'time' in self.task:
            t = do.date_time()
            t.Time()

        elif 'weather' in self.task:
            w = do.weather()
            w.update()



        else:
            print('command not found!')
            self.voice.say(audio='command_not_found.mp3')