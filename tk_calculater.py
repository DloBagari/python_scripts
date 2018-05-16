from tkinter import *
root = Tk()
root.title("Style")
root.option_readfile("style2.txt")
root.configure(background="#4D4D4D")
mytext= Text(root,width=25,height=4, relief="sunken",borderwidth=10,
             background='#101010', foreground="#D6D6D6")
mytext.insert(END,"typeypu numbers")
mytext.grid(row=0, column=0, columnspan=6,padx=5,pady=5)
Button(root, text="*").grid(row=1, column=1)
Button(root, text="^").grid(row=1, column=2)
Button(root, text="#").grid(row=1, column=3)
Button(root, text="<").grid(row=2, column=1)
Button(root, text="OK",cursor="target").grid(row=2, column=2)
Button(root, text=">").grid(row=2, column=3)
Button(root, text="+").grid(row=3, column=1)
Button(root, text="V").grid(row=3, column=2)
Button(root, text="-").grid(row=3, column=3)
for i in range(1,10):
    Button(root,text=str(i)).grid(column=3 if i % 3 == 0 \
                                  else( 1 if i % 3 == 1 else 2),
                                  row=4 if i <= 3 else( 5 if i<= 6 else 6),pady=2,padx=2)
mybitmaps = ['info','error', 'hourglass',  'questhead','question', 'warning']
for b in mybitmaps:
    Button(root, bitmap=b,width=40, height=44).grid(row=mybitmaps.index(b)+1,
                                                   column=4, sticky="w",pady=2,padx=2)
root.mainloop()
