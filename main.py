import word as wd
from tkinter import *
from random import randint


words = wd.fill_vocab()

top = Tk()
text1 = Text(top)
text1.insert(END, words[1].mean2.iloc[0])
text1.pack(side=RIGHT)


vocab_len = len(words)


def rand_word():
    text1.delete("1.0", "end")
    update = words[randint(0, vocab_len-1)].mean2.iloc[0]
    print(update)
    text1.insert(END, update)


button1 = Button(top, text="Red", fg="red")
button1.pack(side=LEFT)

button1.configure(command=rand_word)


top.mainloop()

print(len(words))
