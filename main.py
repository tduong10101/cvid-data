import requests
import pandas as pd
from io import StringIO
nyt_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
jh_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1613431998811r0.7768460732645635"

def get_data_from_url(url):
    result=requests.get(url).text
    result = StringIO(result)
    result_pd = pd.pandas.read_csv(result, parse_dates={'date_obj':[0]})
    return result_pd

# get data from url1 data dump
nyt_data = get_data_from_url(nyt_url)

# get data from url2 data dump
jh_data = get_data_from_url(jh_url)
jh_data = jh_data[jh_data['Country/Region']=='US']
for col in jh_data.columns:
    jh_data.rename(columns = {col:col.lower()}, inplace = True) 

merged_data = pd.merge(nyt_data, jh_data, on='date_obj')

print(merged_data)