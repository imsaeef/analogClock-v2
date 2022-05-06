from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import time
from math import *
from datetime import *

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600+200+50")
        self.root.title("Analog Clock V2")
        self.root.config(bg="#91d04d")
        self.root.resizable(0, 0)
        self.root.iconbitmap("Clock.ico")


        #clock label
        self.label = Label(self.root, bg="#158283", bd=10, relief="raised")
        self.label.place(x=300, y=100, height=400, width=400)
        # self.clockImg()
        self.runClock()

    #clock img
    def clockImg(self, hr, mnt, sec):
        clock = Image.new("RGB", (400, 400), (21, 131, 132))
        draw = ImageDraw.Draw(clock)
        img = Image.open("clk1.png")
        img = img.resize((300, 300), Image.ANTIALIAS)
        clock.paste(img, (50, 50))

        #set origin
        origin = 200, 200
        #draw hr line
        draw.line((origin, 200+40*sin(radians(hr)), 200-40*cos(radians(hr))), fill="#00dd6f", width=4)
        #draw mnt line
        draw.line((origin, 200+60*sin(radians(mnt)), 200-60*cos(radians(mnt))), fill="yellow", width=3)
        #draw sec line
        draw.line((origin, 200+80*sin(radians(sec)), 200-80*cos(radians(sec))), fill="#ff00ff", width=2)
        #drwa circle
        draw.ellipse((195, 192, 210, 210), fill="#003d59")

        #save new img
        clock.save("newClock.png")
        # clock.show()

    def runClock(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h/12)*360
        mnt = (m/60)*360
        sec = (s/60)*360

        self.clockImg(hr, mnt, sec)
        self.img = ImageTk.PhotoImage(file="newClock.png")
        self.label.config(image=self.img)
        self.label.after(200, self.runClock)


if __name__=="__main__":
    root = Tk()
    app = AnalogClock(root)
    root.mainloop()
