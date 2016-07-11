from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

from json import loads, dumps
from hashCalc import d, r, statements

class MainForm(BoxLayout):

    howMany = NumericProperty(1)
    wasTen = BooleanProperty(False)
    isCaption = BooleanProperty(False)
    isProgram = BooleanProperty(False)

    def starter(self):

        self.anim = []
        for i in range(10):
            self.anim.append(Animation(
                    duration=0,
                    color=[1,1,1,1]
                    ))
            self.anim[i] += Animation(
                    duration=0.5,
                    color=[0,0.7,0.7,1]
                    )
        self.recover()
        for i in range(10):
            index = 'b' + str(i)
            self.ids[index].text = self.persist[i][0]
            self.ids[index].code = self.persist[i][1]

    persist = [
            ['Ping',''],
            ['Ping',''],
            ['Ping',''],
            ['Ping',''],
            ['Ping',''],
            ['Ping',''],
            ['Ping',''],
            ['Ping',''],
            ['Ping',''],
            ['Ping','']
            ]


    def number(self, n):
        if n == 10:
            if self.wasTen:
                self.howMany += 10
            else:
                self.howMany = 10
            self.wasTen = True
        else:
            if self.wasTen:
                self.howMany += n
                self.wasTen = False
            else:
                self.howMany = n


    def dice(self, n):
        return str(d(n))

    def roll(self, widget):
        '''roll a simple number'''
        k = self.howMany
        self.howMany = 1
	self.wasTen = False
        n = int(widget.text[1:])
        value = str(r(k, n))
        position = widget.dx
        self.display(value, position)

    def clear_all(self, keep=False):
        self.ids.s0.text = ''
        self.ids.s1.text = ''
        self.ids.s2.text = ''
        self.ids.s3.text = ''
        self.ids.s4.text = ''
        self.ids.s5.text = ''
        self.ids.s6.text = ''
        self.ids.s7.text = ''
        self.ids.s8.text = ''
        self.ids.s9.text = ''
        self.howMany = 1
        self.isCaption = False
        self.isProgram = False
        self.was10=False
        if not keep:
            self.ids.t0.text = ''

        sound = SoundLoader.load('affirmative.wav')
        if sound:
            sound.play()

    def macro(self, id ):
        '''execute a program button'''
        index = 'b'+str(id)
        if self.isCaption:
            self.ids[index].text = self.ids.t0.text
            self.persist[id][0] = self.ids.t0.text
            self.stash()
            self.isCaption = False
        elif self.isProgram:
            self.ids[index].code = self.ids.t0.text
            # put in persist for reloading later
            self.persist[id][1] = self.ids.t0.text
            self.stash()
            self.isProgram = False
        else:
            self.code = self.ids[index].code
            self.ids.t0.text = self.code
            self.dorolls()

    def dorolls(self):
        '''process the statements'''
        # for this application fold all to lower case.
        self.code = self.code.lower()
        assigns = statements(self.code)
        curOP = 0 # current output set to first one
        for ass in assigns:
            if ass[0] == 'output':
                # destined for screen
                if ass[1] == 'clr':
                    self.clear_all(keep=True)
                    continue
                if ass[1]:
                    op = eval(ass[1])
                else:
                    op = '0'
                self.display(op, curOP)
                curOP += 1
            else:
                if '0' <= ass[0] <= '9':
                    op = eval(ass[1])
                    self.display(op, int(ass[0]))
                else:
                    lvalue = ass[0]
                    rvalue = ass[1]
                    globals()[lvalue] = eval(rvalue)

    def display(self, value, position):
        index = 's'+str(position)
        self.ids[index].text = str(value)
        self.anim[position].start(self.ids[index])

    def stash(self):
        contents = dumps(self.persist)
        with open('dicedata', 'w') as ofile:
            ofile.write(contents)

    def recover(self):
        try:
            with open('dicedata', 'r') as ifile:
                contents = ifile.read()
            self.persist = loads(contents)
        except:
            pass




class DigitalDiceApp(App):
    def build(self):
        return MainForm()
    
    def on_start(self):
        self.root.starter()

if __name__ == '__main__':
    DigitalDiceApp().run()
