from tkinter import *
root =Tk()
root.title("fuck off")
root.geometry("450x100+400+500")
root.option_readfile("style.txt")
#root.overrideredirect(1)
def clicked(a):
    print(str(number.get()))
    print(emp.get(),a)
    print(remeber.get())
Label(root, text="Employee Numer:").grid(row=0,column=0, sticky='w')
number= StringVar()
Entry(root,textvariable=number,width=40).grid(row=0, column=1,padx=2,pady=1,columnspan=9)
Label(root, text="Login Passowrd:").grid(row=1,column=0,sticky='e')
emp=StringVar()
Entry(root,textvariable=emp, show="-",width=40).grid( row=1, column=1,columnspan=9)
remeber=BooleanVar()
remeber.set(True)
Checkbutton(root, text="remember me", variable=remeber).grid(row=2, column=3)
Button(root, text="Login", command=lambda: clicked("hello")).grid(row=2, column=9, sticky='e')
root.mainloop()

