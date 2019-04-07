import pandas as pd
import word as wd
import os
import numpy as np

words_list = []
files = os.listdir('vocab')
for i in files:
    wi = pd.read_csv('vocab/'+i, header=None)
    for j in range(wi.shape[0]):
        words_list.append(wd.Word(wi, j))


w1 = pd.read_csv('vocab/words_19_03_10.csv', header=None)

l1 = wd.Word(w1, 0)

print(words_list[11].mean2)
