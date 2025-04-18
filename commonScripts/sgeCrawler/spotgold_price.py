from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
import requests


def spot_quotes_sge() -> pd.DataFrame:
    """
    上海黄金交易所-延时行情
    :return: 延时行情（开盘后实时更新）
    :rtype: pd.DataFrame
    """
    url = 'https://www.sge.com.cn/sjzx/yshqbg'
    df = pd.DataFrame(columns=['代码', '最新价', '最高价', '最低价', '今开盘'])
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html')
    table = soup.find('table')
    for row in table.find_all('tr')[1:]:
        result = [cell.text for cell in row.find_all('td')]
        df.loc[len(df)] = result
    return df


if __name__ == '__main__':
    spot_quotes_sge = spot_quotes_sge()
    print(spot_quotes_sge)