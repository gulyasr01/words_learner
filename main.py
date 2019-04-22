import word as wd
from tkinter import *
from random import randint

# fill the words array from file
words = wd.fill_vocab()

# gui
top = Tk()

# pop-up menu
menu = Menu(top)

disp_mode = 0


def set_eng():
    disp_mode = 0


def set_hun_one_mean():
    disp_mode = 1


def set_hun_all_mean():
    disp_mode = 2


menu.add_command(label="English", command=set_eng)
menu.add_command(label="Hun one meaning", command=set_hun_one_mean)
menu.add_command(label="Hun all meanings", command=set_hun_all_mean)
top.config(menu=menu)

# text_word displays the actual word
text_word = Text(top)
text_word.pack(side=RIGHT)


vocab_len = len(words)
next_state = 0
word_index = 0


def rand_word():
    global next_state
    global word_index
    text_word.delete("1.0", "end")
    if next_state == 0:
        word_index = randint(0, vocab_len-1)
        update = words[word_index].mean2.iloc[0]
        text_word.insert(END, update)
        next_state = 1
    else:
        update = words[word_index].mean1
        text_word.insert(END, update)
        next_state = 0


# btn_next will display the next word (or show the actuals meaning)
btn_next = Button(top, text="Next", fg="black")
btn_next.pack(side=LEFT)
btn_next.configure(command=rand_word)


top.mainloop()

