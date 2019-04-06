import pandas as pd
import math


class Word:
    def __init__(self, pdf, row):
        self.lang1 = pdf.iloc[row, 0]
        self.lang2 = pdf.iloc[row, 1]
        self.mean1 = pdf.iloc[row, 2]
        self.mean2 = pd.Series(pdf.iloc[row, 3])
        for i in pdf.iloc[row, 4:]:
            if i == 'NaN':
                break
            else:
                self.mean2 = self.mean2.append(pd.Series(i))
