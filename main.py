import word as wd
from tkinter import *
import random

# fill the words array from file
words = wd.fill_vocab()

# gui
top = Tk()

# pop-up menu
menu = Menu(top)

disp_mode = 0


def set_eng():
    global disp_mode
    global next_state
    next_state = 0
    disp_mode = "eng"


def set_hun_one_mean():
    global disp_mode
    global next_state
    next_state = 0
    disp_mode = "hun_one"


def set_hun_all_mean():
    global disp_mode
    global next_state
    next_state = 0
    disp_mode = "hun_all"


menu.add_command(label="English", command=set_eng)
menu.add_command(label="Hun one meaning", command=set_hun_one_mean)
menu.add_command(label="Hun all meanings", command=set_hun_all_mean)
top.config(menu=menu)

# text_word displays the actual word
text_word = Text(top)
text_word.config(height=3, width=20)
text_word.grid(row=0, column=1, rowspan=2)


vocab_len = len(words)
next_state = 0
word_index = 0
word_order = list(range(vocab_len))
random.shuffle(word_order)


def rand_word():
    global next_state
    global word_index
    global disp_mode
    print("index: " + str(word_index))
    print("word num: " + str(word_order.index(word_index)))
    text_word.delete("1.0", "end")
    if disp_mode == "hun_all":
        if next_state == 0:
            update = ""
            for i in words[word_index].mean2:
                update = update + i + "\n"
            text_word.insert(END, update)
            next_state = 1
        else:
            update = words[word_index].mean1
            text_word.insert(END, update)
            next_state = 0
            word_index += 1
    elif disp_mode == "hun_one":
        if next_state == 0:
            update = words[word_index].mean2.iloc[random.randint(0, len(words[word_index].mean2) - 1)]
            text_word.insert(END, update)
            next_state = 1
        else:
            update = words[word_index].mean1
            text_word.insert(END, update)
            next_state = 0
            word_index += 1
    else:
        if next_state == 0:
            update = words[word_index].mean1
            text_word.insert(END, update)
            next_state = 1
        else:
            update = ""
            for i in words[word_index].mean2:
                update = update + i + "\n"
            text_word.insert(END, update)
            next_state = 0
            word_index += 1


def reset_order():
    global next_state
    global word_index
    global word_order
    word_index = 0
    next_state = 0
    word_order = list(range(vocab_len))
    random.shuffle(word_order)


# btn_next will display the next word (or show the actuals meaning)
btn_next = Button(top, text="Next", fg="black")
btn_next.grid(row=0, column=0)
btn_next.configure(command=rand_word)

# btn_reset will start from the beginning the full word interrogate cycle ang generating the random order
btn_reset = Button(top, text="Reset", fg="red")
btn_reset.grid(row=1, column=0)
btn_reset.configure(command=reset_order)


top.mainloop()

