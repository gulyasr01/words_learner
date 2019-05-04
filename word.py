import pandas as pd
import os


# make a word object from a specified row of the csv
class Word:
    def __init__(self, pdf, row):
        self.lang1 = pdf.iloc[row, 0]
        self.lang2 = pdf.iloc[row, 1]
        self.mean1 = pdf.iloc[row, 2]
        self.mean2 = pd.Series(pdf.iloc[row, 3])
        for i in pdf.iloc[row, 4:]:
            if pd.isnull(i):
                break
            else:
                self.mean2 = self.mean2.append(pd.Series(i))


# fill the vocablurafy from the csvs in the 'vocab' directory
def fill_vocab():
    words_list = []
    files = os.listdir('words')
    for i in files:
        wi = pd.read_excel('words/' + i, header=None)
        for j in range(wi.shape[0]):
            words_list.append(Word(wi, j))
    return words_list


# make a padas dataframe from the xlsx-es
def create_df():
    files = os.listdir('words')
    eng = []
    hun = []
    for i in files:
        xls = pd.read_excel('words/' + i, header=None)
        for j in range(xls.shape[0]):
            eng.append(xls.iloc[j, 2])
            hun_means = []
            for k in xls.iloc[j, 3:]:
                if pd.isnull(k):
                    break
                else:
                    hun_means.append(k)
            hun.append(hun_means)
    df = pd.DataFrame(eng, columns=['eng'])
    df['hun'] = hun
    df['score'] = int(0)
    return df
