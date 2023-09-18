import pandas as pd

# Read the CSV data into a Pandas DataFrame
df = pd.read_csv('oscar_data.csv')

# Create a dictionary to store the number of awards won by actors and actresses
awards_count = {}

# Iterate through the DataFrame to count the awards for actors and actresses
for index, row in df.iterrows():
    entity = row['entity']
    category = row['category']
    winner = row['winner']

    # Check if the category is 'ACTOR' or 'ACTRESS'
    if winner and (category == 'ACTOR' or category == 'ACTRESS'):
        if entity in awards_count:
            awards_count[entity] += 1
        else:
            awards_count[entity] = 1

# Create a DataFrame from the dictionary
awards_df = pd.DataFrame(list(awards_count.items()), columns=['Actor/Actress', 'Awards Won'])

# Sort the DataFrame by the number of awards won in descending order
awards_df = awards_df.sort_values(by='Awards Won', ascending=False)

# Display the ranking
print("Ranking of Actors and Actresses by Number of Awards Won:")
print(awards_df)


# Display the ranking
print("Ranking of Actors and Actresses by Number of Awards Won:")
print(awards_df)
