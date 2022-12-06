from tkinter import *
from tkinter import ttk
root = Tk()
"""
Binding Events Example

"""
l =ttk.Label(root, text="Starting...")
l.grid()

l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))

l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))

l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
# <3> === <ButtonPress-3>
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
# <Double-1> === <Double-ButtonPress-1>
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))

l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()
root.mainloop()

"""
Can also track more than one events
ex: <KeyPress-A><KeyPress-B> === <ab>
"""
