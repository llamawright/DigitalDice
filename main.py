from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty

from hashCalc import d, r

class MainForm(BoxLayout):
    howMany = NumericProperty(1)
    wasTen = BooleanProperty(False)
    isCaption = BooleanProperty(False)
    isProgram = BooleanProperty(False)


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
        return str(r(self.howMany, n))

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
            
            print self.code, 'Ha!'

class DigitalDiceApp(App):
    def build(self):
        return MainForm()

if __name__ == '__main__':
    DigitalDiceApp().run()
