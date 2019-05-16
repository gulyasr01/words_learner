import word as wd
from tkinter import *
import random
import pandas as pd

# global variables
mistake = 0

# gui
top = Tk()


# menu to select the actual dataset
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


# menu to select the interrogation mode
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


# menu to select the random generation mode
random_mode = "full"


def menu_rand_callback(select):
    global random_mode
    if select == "Random":
        random_mode = "full"
    elif select == "Decrease":
        random_mode = "decrease"


opts_rand = StringVar()
menu_rand = OptionMenu(top, opts_rand, "Random", "Decrease", command=menu_rand_callback)
menu_rand.config(width=8)
menu_rand.grid(row=0, column=1, sticky="w")
opts_rand.set("Random")

# text_word displays the actual word
text_word = Text(top)
text_word.config(height=6, width=20)
text_word.grid(row=2, column=1, rowspan=4)

# text_word displays the actual word meaning
text_meaning = Text(top)
text_meaning.config(height=6, width=20)
text_meaning.grid(row=2, column=2, rowspan=4)

# text_status displays some information about the current interogation
text_status = Text(top)
text_status.config(height=6, width=20)
text_status.grid(row=2, column=3, rowspan=4)
text_status.insert(END, "Create or load!")


def update_status():
    global disp_mode
    global vocab_len
    global word_index
    global words
    global mistake
    text_status.delete("1.0", "end")
    text_status.insert(END, "Size: " + str(vocab_len) + "\nMode: " + str(disp_mode) + "\nReamaining: "
                       + str(vocab_len-word_index) + "\nScore: " + str(words.loc[words.index[word_index], 'score'])
                       + "\nMiss: " + str(mistake))


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
    global vocab_len
    if word_index > (vocab_len - 1):
        text_word.delete("1.0", "end")
        text_meaning.delete("1.0", "end")
        text_word.insert(END, "Done!")
    else:
        if disp_mode == "hun_all":
            if next_state == 0:
                text_word.delete("1.0", "end")
                text_meaning.delete("1.0", "end")
                # print all the hun meanings in new lines
                update_word = ""
                for i in words.loc[words.index[word_index], 'hun']:
                    update_word = update_word + i + "\n"
                text_word.insert(END, update_word)
                next_state = 1
                update_status()
            else:
                update_meaning = words.loc[words.index[word_index], 'eng']
                text_meaning.insert(END, update_meaning)
                next_state = 0
                word_index += 1
        elif disp_mode == "hun_one":
            if next_state == 0:
                text_word.delete("1.0", "end")
                text_meaning.delete("1.0", "end")
                # select one of the hun meanings
                hun = words.loc[words.index[word_index], 'hun']
                update_word = hun[random.randint(0, len(hun)-1)]
                text_word.insert(END, update_word)
                next_state = 1
                update_status()
            else:
                update_meaning = words.loc[words.index[word_index], 'eng']
                text_meaning.insert(END, update_meaning)
                next_state = 0
                word_index += 1
        else:
            if next_state == 0:
                text_word.delete("1.0", "end")
                text_meaning.delete("1.0", "end")
                update_word = words.loc[words.index[word_index], 'eng']
                text_word.insert(END, update_word)
                next_state = 1
                update_status()
            else:
                # print all the hun meanings in new lines
                update_meaning = ""
                for i in words.loc[words.index[word_index], 'hun']:
                    update_meaning = update_meaning + i + "\n"
                text_meaning.insert(END, update_meaning)
                next_state = 0
                word_index += 1


def reset_order():
    global next_state
    global word_index
    global random_mode
    global mistake
    word_index = 0
    next_state = 0
    if random_mode == "full":
        full_rand()
    elif random_mode == "decrease":
        decrease_rand()
    text_word.delete("1.0", "end")
    text_meaning.delete("1.0", "end")
    mistake = 0
    update_status()


def full_rand():
    global words
    words = words.sample(frac=1).reset_index(drop=True)


def decrease_rand():
    global words
    words = words.sample(frac=1).reset_index(drop=True)
    words = words.sort_values(by='score', ascending=True).reset_index(drop=True)


# btn_next will display the next word (or show the actuals meaning)
btn_next = Button(top, text="Next", fg="black")
btn_next.grid(row=2, column=0, sticky="ew")
btn_next.configure(command=next_word)

# btn_reset will start from the beginning the full word interrogate cycle ang generating the random order
btn_reset = Button(top, text="Reset", fg="red")
btn_reset.grid(row=5, column=0, sticky="ew")
btn_reset.configure(command=reset_order)


# btn to increase score
def inc_score():
    global words
    if next_state == 0:
        words.loc[words.index[word_index-1], 'score'] = words.loc[words.index[word_index-1], 'score'] + 1
    next_word()


def dec_score():
    global words
    global mistake
    if next_state == 0:
        words.loc[words.index[word_index-1], 'score'] = words.loc[words.index[word_index-1], 'score'] - 1
        mistake = mistake + 1
    next_word()


btn_plus = Button(top, text="+", fg="black")
btn_plus.grid(row=3, column=0, sticky="ew")
btn_plus.configure(command=inc_score)

# btn to decrease score
btn_minus = Button(top, text="-", fg="black")
btn_minus.grid(row=4, column=0, sticky="ew")
btn_minus.configure(command=dec_score)

top.mainloop()
