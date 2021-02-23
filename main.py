import transform_data as td
nyt_url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
jh_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1613431998811r0.7768460732645635"

data = td.transform_data(nyt_url,jh_url)
print(data)