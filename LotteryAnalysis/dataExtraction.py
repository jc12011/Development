from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from bs4.element import Tag
from datetime import datetime

# Set mode: "all" for one file, "yearly" for one file per year
mode = "all"  # or "yearly"

filePath = './files/'
os.makedirs(filePath, exist_ok=True)

current_year = datetime.now().year

def fetch_year_data(year):
    url = f'https://www.nfd.com.tw/house/year/{year}.htm'
    try:
        resp = requests.get(url, timeout=10)
        resp.encoding = 'big5'
        soup = BeautifulSoup(resp.text, "html.parser")
        table = soup.find('table', {'border': '1'})
        if not table or not isinstance(table, Tag):
            print(f'No table found for year {year}')
            return None, None
        rows = table.find_all('tr')
        if not rows:
            print(f'No data for year {year}')
            return None, None
        title = [td.text.strip() for td in rows[0].find_all('td')]
        data = [[td.text.strip() for td in row.find_all('td')] for row in rows[1:]]
        if not data or not title:
            print(f'No data for year {year}')
            return None, None
        return title, data
    except Exception as e:
        print(f'Error fetching year {year}: {e}')
        return None, None

all_data = []
all_columns = None

for year in range(1976, current_year + 1):
    print(f'Processing year: {year}')
    title, data = fetch_year_data(year)
    if title and data:
        if mode == "yearly":
            df = pd.DataFrame(data, columns=title)
            df.to_csv(os.path.join(filePath, f'{year}.csv'), index=False)
            print(f'Saved: {year}.csv')
        elif mode == "all":
            for row in data:
                #all_data.append([year] + row) #the year is already in the title
                all_data.append(row) 
            if all_columns is None:
                #all_columns = ["Year"] + title #the year is already in the title
                all_columns = title
    # else: message already printed in fetch_year_data

if mode == "all" and all_data and all_columns:
    df_all = pd.DataFrame(all_data, columns=all_columns)
    df_all.to_csv(os.path.join(filePath, 'all_years.csv'), index=False)
    print('Saved: all_years.csv')
