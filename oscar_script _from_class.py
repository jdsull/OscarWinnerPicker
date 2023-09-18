"""
    Perform Oscars task using Pandas
"""
import pandas as pd

def main():
    filename = 'oscar_data.csv'

    # read csv data from the file
    df = pd.read_csv(filename)

    # what (data) type is this?
    print(type(df))

    # What variables or factors are available?
    print(df.columns)

    # what are the possible categories?
    categories = df['category'].unique()

    # sort the results and print the first 5.
    categories.sort()
    print(categories[:5])

    # get a index of the categorys that are form the subset.
    filter_index = df['category'].isin(['ACTOR', 'ACTOR IN A LEADING ROLE'])
    # print the index
    print(filter_index)

    # check the type of the index
    print(type(filter_index))

    # get the rows of df that match the index.
    actors = df[filter_index]

    # filter the actors for the winners
    winners = actors[actors['winner'] == True]

    # a complex query of the resulting subset.
    # try tp figure out what it is doing.
    print(winners.groupby('entity').size().sort_values(ascending=False)[:10])


main()