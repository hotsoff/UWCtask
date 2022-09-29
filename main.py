import tkinter as tk
import time
window = tk.Tk()
frame = tk.Frame(master=window, width=200, height=200, bg = 'black')
frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


count = 0
def Alarm():
    global count
    count += 1
    return label1.configure(bg='red'),label2.configure(bg='black')


def Retreat():
    if count == 0:
        return 1
    else:
        return label2.configure(bg='green'), label1.configure(bg='black')


label1 = tk.Label(
    master = frame,
    text='Alarm',
    fg="white",
    bg="black",
    width = 10,
    height = 5
)


button1 = tk.Button(
    master = frame,
    text='Alarm',
    bg="gray",
    fg="black",
    width = 10,
    height = 5,
    command=Alarm
)

label2 = tk.Label(
    master = frame,
    text='Retreat',
    fg="white",
    bg="black",
    width = 10,
    height = 5
)


button2 = tk.Button(
    master = frame,
    text='Retreat',
    bg="gray",
    fg="black",
    width = 10,
    height = 5,
    command = Retreat

)


label1.place(x=0,y=0)
button1.place(x=0,y=100)
label2.place(x=100,y=0)
button2.place(x=100,y=100)
window.mainloop()