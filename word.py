import pandas as pd
import os


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
