# -*- coding: utf-8 -*-

from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack() # pack()方法把Widget加入到父容器中，并实现布局。
        self.quitButton = Button(self, text='Quit', command=self.master.destory)
        self.quitButton.pack()

app = Application()
app.master.title('Hello World')
app.mainloop()
