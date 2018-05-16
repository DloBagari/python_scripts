from tkinter import *
root = Tk()
newicon = PhotoImage(file='/home/kobani/test/icons/new_file.gif')
openicon = PhotoImage(file='/home/kobani/test/icons/open_file.gif')
saveicon = PhotoImage(file='/home/kobani/test/icons/save.gif')
cuticon = PhotoImage(file='/home/kobani/test/icons/cut.gif')
copyicon = PhotoImage(file='/home/kobani/test/icons/copy.gif')
pasteicon = PhotoImage(file='/home/kobani/test/icons/paste.gif')
undoicon = PhotoImage(file='/home/kobani/test/icons/undo.gif')
redoicon = PhotoImage(file='/home/kobani/test/icons/redo.gif')
menubar= Menu(root)

filemenu = Menu(menubar, tearoff=0)
#compound it let us add image beside the common text
"""underline specify the index of a character in the menu text to be underlined
the index start at 0  which means that sprecifying underline =1 underlines
the secound  character of the text,  tkinter also users it to define the
default bindings for keyboard traversal of menus
 with this we can select menu other with mouse pointer or with  the
 atl+<character_at_inderlined_index> """
filemenu.add_command(label="New", accelerator="Ctrl+N", compound=LEFT,
                     image=newicon, underline=0)
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT,
                     image=openicon, underline =0)
filemenu.add_command(label="Save", accelerator='Ctrl+S',compound=LEFT,
                     image=saveicon,underline=0)
filemenu.add_command(label="Save as",accelerator='Shift+Ctrl+S')
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Shift+Ctrl+S")
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",compound=LEFT,  image=undoicon,
                     accelerator='Ctrl+Z')
editmenu.add_command(label="Redo",compound=LEFT,  image=redoicon,
                     accelerator='Ctrl+Y')
editmenu.add_separator() 
editmenu.add_command(label="Cut", compound=LEFT, image=cuticon,
                     accelerator='Ctrl+X')
editmenu.add_command(label="Copy", compound=LEFT, image=copyicon,
                     accelerator='Ctrl+C')
editmenu.add_command(label="Paste",compound=LEFT, image=pasteicon,
                     accelerator='Ctrl+V')
editmenu.add_separator()
editmenu.add_command(label="Find",underline= 0, accelerator='Ctrl+F')
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=7, accelerator='Ctrl+A')
menubar.add_cascade(label="Edit", menu=editmenu)

viewmenu = Menu(menubar, tearoff=0)
showline=IntVar()
showline.set(1)
viewmenu.add_checkbutton(label="Show Line Number", variable=showline)
showInfo=IntVar()
showInfo.set(1)
viewmenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showInfo)
highlight=IntVar()
viewmenu.add_checkbutton(label="Highlight Current Line", onvalue=1, offvalue=0,
                         variable=highlight)
themesmenu = Menu(viewmenu, tearoff=0)
viewmenu.add_cascade(label="Themes", menu=themesmenu)
clrschms = {
'1. Default White': 'FFFFFF',
'2. Greygarious Grey':'D1D4D1',
'3. Lovely Lavender':'E1E1FF' , 
'4. Aquamarine': 'D1E7E0',
'5. Bold Beige': 'FFF0E1',
'6. Cobalt Blue':'333AA',
'7. Olive Green': '5B8340',
}
themechoice = StringVar()
themechoice.set(' Default White')
for i in sorted(clrschms):
    themesmenu.add_radiobutton(label=i[2:], variable=themechoice)
menubar.add_cascade(label="View", menu=viewmenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About")
aboutmenu.add_command(label="Help")
menubar.add_cascade(label="About", menu=aboutmenu)
root.config(menu=menubar)

shortcutbar = Frame(root, height=25, bg="light sea green")
shortcutbar.pack(expand=NO, fill=X)
inlabel = Label(root, width=2, bg="antique white")
inlabel.pack(side=LEFT, anchor="nw", fill=Y)

textpad = Text(root)
textpad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textpad)
textpad.configure(yscrollcommand=scroll.set)
scroll.config(command=textpad.yview)
scroll.pack(side=RIGHT, fill=Y,ipadx=2)
root.mainloop()
