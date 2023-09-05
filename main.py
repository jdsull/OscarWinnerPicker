'''
A program to rank actors and actresses by number of awards won.
'''

import pandas as pd

def readFile():
    df = pd.read_csv('data/oscar_data.csv')
    print(df.toString())

readFile()

