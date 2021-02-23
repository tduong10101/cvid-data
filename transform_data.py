import requests
import pandas as pd
from io import StringIO

def get_data_from_url(url):
    result=requests.get(url).text
    result = StringIO(result)
    result_pd = pd.pandas.read_csv(result, parse_dates={'date_obj':[0]})
    return result_pd

def transform_data(nyt_url,jh_url):
    # get data from url1 data dump
    nyt_data = get_data_from_url(nyt_url)

    # get data from url2 data dump
    jh_data = get_data_from_url(jh_url)
    jh_data = jh_data[jh_data['Country/Region']=='US']
    for col in jh_data.columns:
        jh_data.rename(columns = {col:col.lower()}, inplace = True) 

    merged_data = pd.merge(nyt_data, jh_data, on='date_obj')

    return merged_data