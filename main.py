import pandas as pd
import word as wd

w1 = pd.read_csv('words1.csv', header=None)

l1 = wd.Word(w1, 0)

print(l1.mean2)
