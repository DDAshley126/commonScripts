from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
import requests


def main():
    url = 'https://www.sge.com.cn/sjzx/yshqbg'
    df = pd.DataFrame(columns=['代码', '最新价', '最高价', '最低价', '今开盘', '更新时间'])
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html')
    table = soup.find('table')
    now = datetime.datetime.now().replace(microsecond=0)
    for row in table.find_all('tr')[1:]:
        result = [cell.text for cell in row.find_all('td')]
        result.append(now)
        df.loc[len(df)] = result
    return df