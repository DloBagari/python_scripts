from tkinter import *
root = Tk()
root.title("Find & Repalce")
Label(root, text="Find:").grid(row=0, column=0, sticky=E)
Entry(root).grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)
Button(root, text="Find").grid(row=0, column=10,padx=2, pady=2, sticky='ew')
Label(root, text="Replace:").grid(row=1, column=0)
Entry(root).grid(row=1, column=1, padx=2, pady=2, sticky='we', columnspan=9)
Button(root, text="Find All").grid(row=1, column=10,padx=2, pady=2, sticky='ew')
Checkbutton(root,text="Match whole word only").grid(row=2, column=1,columnspan=4,sticky="w")
Checkbutton(root,text="Match Case").grid(row=3, column=1,columnspan=4,sticky="w")
Checkbutton(root,text="Wrap around").grid(row=4, column=1,columnspan=4,sticky="w")
Label(root, text="Diection:").grid(row=2, column=6,sticky='E')
Label(root, text="       ").grid(row=2, column=5,sticky='w')
Button(root, text="Relapce").grid(row=2, column=10,padx=2,pady=2,sticky='ew')
Radiobutton(root, text="Up",valu=1).grid(row=3, column=6,sticky='w')
Radiobutton(root, text="Down    ",valu=2).grid(row=3, column=7,sticky='w')
root.mainloop()
