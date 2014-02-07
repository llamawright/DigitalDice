from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty

from json import loads, dumps
from hashCalc import d, r, statements

class MainForm(BoxLayout):

    def starter(self):

        self.recover()
        self.ids.b0.text = self.persist[0][0]
        self.ids.b0.code = self.persist[0][1]

        self.ids.b1.text = self.persist[1][0]
        self.ids.b1.code = self.persist[1][1]

        self.ids.b2.text = self.persist[2][0]
        self.ids.b2.code = self.persist[2][1]

        self.ids.b3.text = self.persist[3][0]
        self.ids.b3.code = self.persist[3][1]

        self.ids.b4.text = self.persist[4][0]
        self.ids.b4.code = self.persist[4][1]

        self.ids.b5.text = self.persist[5][0]
        self.ids.b5.code = self.persist[5][1]

        self.ids.b6.text = self.persist[6][0]
        self.ids.b6.code = self.persist[6][1]

        self.ids.b7.text = self.persist[7][0]
        self.ids.b7.code = self.persist[7][1]

        self.ids.b8.text = self.persist[8][0]
        self.ids.b8.code = self.persist[8][1]

        self.ids.b9.text = self.persist[9][0]
        self.ids.b9.code = self.persist[9][1]


    howMany = NumericProperty(1)
    wasTen = BooleanProperty(False)
    isCaption = BooleanProperty(False)
    isProgram = BooleanProperty(False)
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

    def roll(self, n):
        k = self.howMany
        self.howMany = 1
        return str(r(k, n))

    def clearAll(self):
        self.ids.s0.text = '0'
        self.ids.s1.text = '0'
        self.ids.s2.text = '0'
        self.ids.s3.text = '0'
        self.ids.s4.text = '0'
        self.ids.s5.text = '0'
        self.ids.s6.text = '0'
        self.ids.s7.text = '0'
        self.ids.s8.text = '0'
        self.ids.s9.text = '0'
        self.howMany = 1
        self.isCaption = False
        self.isProgram = False
        self.was10=False
        self.ids.t0.text = ''

# This method is horrible as I don't know how to array widgets, yet.
    def macro(self, id ):
        if self.isCaption:
            if id == 0:
                self.ids.b0.text = self.ids.t0.text
            if id == 1:
                self.ids.b1.text = self.ids.t0.text
            if id == 2:
                self.ids.b2.text = self.ids.t0.text
            if id == 3:
                self.ids.b3.text = self.ids.t0.text
            if id == 4:
                self.ids.b4.text = self.ids.t0.text
            if id == 5:
                self.ids.b5.text = self.ids.t0.text
            if id == 6:
                self.ids.b6.text = self.ids.t0.text
            if id == 7:
                self.ids.b7.text = self.ids.t0.text
            if id == 8:
                self.ids.b8.text = self.ids.t0.text
            if id == 9:
                self.ids.b9.text = self.ids.t0.text
            # put in persist for reloading later
            self.persist[id][0] = self.ids.t0.text
            self.stash()
            self.isCaption = False
        elif self.isProgram:
            if id == 0:
                self.ids.b0.code = self.ids.t0.text
            if id == 1:
                self.ids.b1.code = self.ids.t0.text
            if id == 2:
                self.ids.b2.code = self.ids.t0.text
            if id == 3:
                self.ids.b3.code = self.ids.t0.text
            if id == 4:
                self.ids.b4.code = self.ids.t0.text
            if id == 5:
                self.ids.b5.code = self.ids.t0.text
            if id == 6:
                self.ids.b6.code = self.ids.t0.text
            if id == 7:
                self.ids.b7.code = self.ids.t0.text
            if id == 8:
                self.ids.b8.code = self.ids.t0.text
            if id == 9:
                self.ids.b9.code = self.ids.t0.text
            # put in persist for reloading later
            self.persist[id][1] = self.ids.t0.text
            self.stash()
            self.isProgram = False
        else:
            if id == 0:
                self.code = self.ids.b0.code
            if id == 1:
                self.code = self.ids.b1.code
            if id == 2:
                self.code = self.ids.b2.code
            if id == 3:
                self.code = self.ids.b3.code
            if id == 4:
                self.code = self.ids.b4.code
            if id == 5:
                self.code = self.ids.b5.code
            if id == 6:
                self.code = self.ids.b6.code
            if id == 7:
                self.code = self.ids.b7.code
            if id == 8:
                self.code = self.ids.b8.code
            if id == 9:
                self.code = self.ids.b9.code
            
            self.ids.t0.text = self.code
            # Now process the statements
            # for this application fold all to lower case.
            self.code = self.code.lower()
            assigns = statements(self.code)
            curOP = 0 # current output set to first one
            for ass in assigns:
                if ass[0] == 'output':
                    # destined for screen
                    if ass[1]:
                        op = eval(ass[1])
                    else:
                        op = '0'
                    self.display(op, curOP)
                    curOP += 1
                else:
                    lvalue = ass[0]
                    rvalue = ass[1]
                    locals()[lvalue] = eval(rvalue)

    def display(self, value, position):
            if position == 0:
                self.ids.s0.text = str(value)
            if position == 1:
                self.ids.s1.text = str(value)
            if position == 2:
                self.ids.s2.text = str(value)
            if position == 3:
                self.ids.s3.text = str(value)
            if position == 4:
                self.ids.s4.text = str(value)
            if position == 5:
                self.ids.s5.text = str(value)
            if position == 6:
                self.ids.s6.text = str(value)
            if position == 7:
                self.ids.s7.text = str(value)
            if position == 8:
                self.ids.s8.text = str(value)
            if position == 9:
                self.ids.s9.text = str(value)

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
