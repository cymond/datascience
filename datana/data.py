from urllib.request import urlretrieve
import os
import pandas as pd

Freemont_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD&bom=true&format=true&delimiter=%3B"
filename = "freemont.csv"
    
def retrieve_freemont_data(filename=filename, url=Freemont_URL, force_download = False):
    import pandas as pd
    if force_download or not os.path.exists(filename):
        print("Printing file...")
        urlretrieve(url, filename)

    data = pd.read_csv(filename, delimiter=';', index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
