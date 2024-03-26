#We followed the process to import pandas library to find out the popular titles and group of patrons which is having the consequetuve duplicate.

import pandas as pd

# Extracted the json file and read the json records in the tabular format
df = pd.read_json('messages.json')

#print(df.head(4))

##popular_titles = df.groupby("item")['rating'].count()

#  1. What are the most popular titles?
df_frame = pd.DataFrame(df)

result = df_frame.groupby('item').size().reset_index(name='count').sort_values(by='count', ascending=False)

print(result)

## Title _16 is having the maximum count

#2. What groups of patrons are similar?

consecutive_duplicate = result[result['count'].eq(result['count'].shift())]

print(consecutive_duplicate)