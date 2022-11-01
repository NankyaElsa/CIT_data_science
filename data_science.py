# import pandas as pd
# data_set= {
#     "name": ["elsa", "mike", "kelly", "anthony", "arnold"],
#     "marks":[92, 70, 82, 54, 60]
# }

# data_frame=pd.DataFrame(data_set)
# print(data_frame)

# #panda series
# #a panda serie is a column in a table
# arr= [i for i in range(10)]

# series=pd.Series(arr)
# print(series)

# #labels
# other_series=pd.Series(arr, index=["e", "l", "s", "a", "m", "y", "l", "o", "v", "e"])
# print(other_series)

# #loc returns a column in a frame
# calories={
#     "day1": "230",
#     "day2": "635",
#     "day3": "723"
# }
# d_frame=pd.DataFrame(calories, index=["day1", "day2", "day3"])
# print(d_frame.loc())


import requests 
def download_csv(url):
    r = requests.get(url)
    with open('data.csv', 'wb') as f:
        f.write(r.content)

import os
import pandas as pd

if not os.path.exists('data.csv'):
    download_csv('https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv')


df = pd.read_csv('data.csv')
print(df)

# df= pd.read_csv("bands.csv")
# print(df.head())




