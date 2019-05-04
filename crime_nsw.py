import csv
import pandas as pd

def crime_total(filename_csv):
    df = pd.read_csv(filename_csv)

    cols = list(df.columns.values)

    for index, cell in enumerate(cols):
        if 'Jan 2010' in cell:
            index_start = index
        elif 'Dec 2018' in cell:
            index_finish = index


    df['Total'] = df.iloc[:, index_start:index_finish+1].sum(axis=1)
    df = (df[df['Total'] > 0]) # table only contains rows where total column > 1

    cols = list(df.columns.values)
    df = df[cols[0:3] + [cols[-1]]] # simplify table
    df = df.reset_index(drop=True)

    df = df.groupby('Suburb')['Total'].sum()

    # Granville Zetland --- > index
    #  15         30    --- > value

    data_dict = df.to_dict()

    return data_dict

