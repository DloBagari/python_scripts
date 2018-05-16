from tkinter import *
root = Tk()
Label(root, text="chick some where in\n the frame").pack()
def respondes(event):
    print("you have clicked at x=%d and y=%d"%(event.x, event.y))
def rooted(event):
    print("root")
root.bind("<Button-1>", rooted)
frame = Frame(root, bg="khaki", width=150, height= 150)
frame.bind("<Button-1>", respondes)
frame.pack()
root.mainloop()
