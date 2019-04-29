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
    update_status()


def set_hun_one_mean():
    global disp_mode
    global next_state
    next_state = 0
    disp_mode = "hun_one"
    update_status()


def set_hun_all_mean():
    global disp_mode
    global next_state
    next_state = 0
    disp_mode = "hun_all"
    update_status()


menu.add_command(label="English", command=set_eng)
menu.add_command(label="Hun one meaning", command=set_hun_one_mean)
menu.add_command(label="Hun all meanings", command=set_hun_all_mean)
top.config(menu=menu)

# text_word displays the actual word
text_word = Text(top)
text_word.config(height=3, width=20)
text_word.grid(row=1, column=1, rowspan=2)

# text_word displays the actual word meaning
text_meaning = Text(top)
text_meaning.config(height=3, width=20)
text_meaning.grid(row=1, column=2, rowspan=2)

# text_status displays some information about the current interogation
text_status = Text(top)
text_status.config(height=3, width=20)
text_status.grid(row=1, column=3, rowspan=2)


def update_status():
    global disp_mode
    global vocab_len
    text_status.delete("1.0", "end")
    text_status.insert(END, "Size: " + str(vocab_len) + "\nMode: " + str(disp_mode))


# labels
label_ask = Label(top, text="Asking:")
label_ask.grid(row=0, column=1)

label_mean = Label(top, text="Meaning:")
label_mean.grid(row=0, column=2)

label_status = Label(top, text="Status:")
label_status.grid(row=0, column=3)

label_remaining = Label(top, text="Remaining:")
label_remaining.grid(row=3, column=0)


vocab_len = len(words)
next_state = 0
word_index = 0
word_order = list(range(vocab_len))
random.shuffle(word_order)


def rand_word():
    global next_state
    global word_index
    global disp_mode
    if disp_mode == "hun_all":
        if next_state == 0:
            text_word.delete("1.0", "end")
            text_meaning.delete("1.0", "end")
            update_word = ""
            for i in words[word_order.index(word_index)].mean2:
                update_word = update_word + i + "\n"
            text_word.insert(END, update_word)
            next_state = 1
        else:
            update_meaning = words[word_order.index(word_index)].mean1
            text_meaning.insert(END, update_meaning)
            next_state = 0
            word_index += 1
    elif disp_mode == "hun_one":
        if next_state == 0:
            text_word.delete("1.0", "end")
            text_meaning.delete("1.0", "end")
            update_word = words[word_order.index(word_index)].mean2.iloc[random.randint(0, len(words[word_order.index(word_index)].mean2) - 1)]
            text_word.insert(END, update_word)
            next_state = 1
        else:
            update_meaning = words[word_order.index(word_index)].mean1
            text_meaning.insert(END, update_meaning)
            next_state = 0
            word_index += 1
    else:
        if next_state == 0:
            text_word.delete("1.0", "end")
            text_meaning.delete("1.0", "end")
            update_word = words[word_order.index(word_index)].mean1
            text_word.insert(END, update_word)
            next_state = 1
        else:
            update_meaning = ""
            for i in words[word_order.index(word_index)].mean2:
                update_meaning = update_meaning + i + "\n"
            text_meaning.insert(END, update_meaning)
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
    text_word.delete("1.0", "end")
    text_meaning.delete("1.0", "end")


# btn_next will display the next word (or show the actuals meaning)
btn_next = Button(top, text="Next", fg="black")
btn_next.grid(row=1, column=0, sticky="ew")
btn_next.configure(command=rand_word)

# btn_reset will start from the beginning the full word interrogate cycle ang generating the random order
btn_reset = Button(top, text="Reset", fg="red")
btn_reset.grid(row=2, column=0, sticky="ew")
btn_reset.configure(command=reset_order)

# initialize the states
disp_mode = "eng"
update_status()

top.mainloop()

