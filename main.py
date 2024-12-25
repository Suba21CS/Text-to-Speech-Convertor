from tkinter import *
from gtts import gTTS
import os
w=Tk()
w.title('Text to Speech')
w.geometry("500x500")
frame=Frame(w,bg="blue",height="150")
frame.pack(fill=X)
frame1=Frame(w,bg="lightpink",height="750")
frame1.pack(fill=X)

l=Label(frame,text="Text to Speech",font=("times",30,"bold"),bg="blue")
l.place(x=130,y=70)
entry=Entry(frame1,width="50",font=14)
entry.place(x=50,y=40)
entry.insert(0,"")
def play():
    language="en"
    myobj=gTTS(text=entry.get(),lang=language,slow="false")
    myobj.save("convert.wav")
    os.system("convert.wav")

b=Button(frame1,text="Submit",font=("times",15,"bold"),bg="green",fg="black",padx=10,pady=10,command=play)
b.place(x=200,y=120)
w.mainloop()