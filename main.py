import word as wd
from tkinter import *
import random
import pandas as pd

# fill the words array from file
#words = wd.create_df()

# gui
top = Tk()


def create_new():
    global words
    global vocab_len
    words = wd.create_df()
    vocab_len = words.shape[0]
    reset_order()
    update_status()


def load_df():
    global words
    global vocab_len
    words = pd.read_pickle('vocab/dict.pkl')
    vocab_len = words.shape[0]
    reset_order()
    update_status()


def save_df():
    global words
    words.to_pickle('vocab/dict.pkl')


menubar = Menu(top)
menubar.add_command(label="Create", command=create_new)
menubar.add_command(label="Load", command=load_df)
menubar.add_command(label="Save", command=save_df)
top.config(menu=menubar)


def menu_callback(select):
    if select == "Eng":
        set_eng()
    elif select == "Hun one":
        set_hun_one_mean()
    elif select == "Hun all":
        set_hun_all_mean()


options = StringVar()
menu = OptionMenu(top, options, "Eng", "Hun one", "Hun all", command=menu_callback)
menu.config(width=8)
menu.grid(row=0, column=0, sticky="ew")
options.set("Eng")
disp_mode = "eng"


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


# text_word displays the actual word
text_word = Text(top)
text_word.config(height=3, width=20)
text_word.grid(row=2, column=1, rowspan=2)

# text_word displays the actual word meaning
text_meaning = Text(top)
text_meaning.config(height=3, width=20)
text_meaning.grid(row=2, column=2, rowspan=2)

# text_status displays some information about the current interogation
text_status = Text(top)
text_status.config(height=3, width=20)
text_status.grid(row=2, column=3, rowspan=2)
text_status.insert(END, "Create or load!")


def update_status():
    global disp_mode
    global vocab_len
    global word_index
    text_status.delete("1.0", "end")
    text_status.insert(END, "Size: " + str(vocab_len) + "\nMode: " + str(disp_mode) + "\nReamaining: " + str(vocab_len-word_index))


# labels
label_ask = Label(top, text="Asking:")
label_ask.grid(row=1, column=1)

label_mean = Label(top, text="Meaning:")
label_mean.grid(row=1, column=2)

label_status = Label(top, text="Status:")
label_status.grid(row=1, column=3)

next_state = 0
word_index = 0


def next_word():
    global next_state
    global word_index
    global disp_mode
    if disp_mode == "hun_all":
        if next_state == 0:
            text_word.delete("1.0", "end")
            text_meaning.delete("1.0", "end")
            # print all the hun meanings in new lines
            update_word = ""
            for i in words.loc[words.index[word_order.index(word_index)], 'hun']:
                update_word = update_word + i + "\n"
            text_word.insert(END, update_word)
            next_state = 1
            update_status()
        else:
            update_meaning = words.loc[words.index[word_order.index(word_index)], 'eng']
            text_meaning.insert(END, update_meaning)
            next_state = 0
            word_index += 1
    elif disp_mode == "hun_one":
        if next_state == 0:
            text_word.delete("1.0", "end")
            text_meaning.delete("1.0", "end")
            # select one of the hun meanings
            hun = words.loc[words.index[word_order.index(word_index)], 'hun']
            update_word = hun[random.randint(0, len(hun)-1)]
            text_word.insert(END, update_word)
            next_state = 1
            update_status()
        else:
            update_meaning = words.loc[words.index[word_order.index(word_index)], 'eng']
            text_meaning.insert(END, update_meaning)
            next_state = 0
            word_index += 1
    else:
        if next_state == 0:
            text_word.delete("1.0", "end")
            text_meaning.delete("1.0", "end")
            update_word = words.loc[words.index[word_order.index(word_index)], 'eng']
            text_word.insert(END, update_word)
            next_state = 1
            update_status()
        else:
            # print all the hun meanings in new lines
            update_meaning = ""
            for i in words.loc[words.index[word_order.index(word_index)], 'hun']:
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
    update_status()


# btn_next will display the next word (or show the actuals meaning)
btn_next = Button(top, text="Next", fg="black")
btn_next.grid(row=2, column=0, sticky="ew")
btn_next.configure(command=next_word)

# btn_reset will start from the beginning the full word interrogate cycle ang generating the random order
btn_reset = Button(top, text="Reset", fg="red")
btn_reset.grid(row=3, column=0, sticky="ew")
btn_reset.configure(command=reset_order)


top.mainloop()
