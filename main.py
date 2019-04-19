import word as wd
from tkinter import *


words = wd.fill_vocab()

top = Tk()
text1 = Text(top)
text1.insert(END, words[0].mean2.iloc[1])
text1.pack()
top.mainloop()

print(words[2].mean2)
