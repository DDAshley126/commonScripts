import requests
import re
import time
import pandas as pd
import datetime
import random


def get_forex_data():
    now = timetime()
    url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37109255212463222533_{now}&fs=b%3AMK0300&fields=f12%2Cf13%2Cf14%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16&fid=f3&pn=1&pz=100&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb&_={now}'
    response = requests.get(url)
    data = response.text
    r = re.compile('.*\((.*)\).*')
    data = r.findall(data)[0]
    data = eval(data)
    return data


def data_process(df):
    data = pd.DataFrame([df['data']['diff'][0]])
    for i in range(1, len(df['data']['diff'])):
        data.loc[len(data)] = list(df['data']['diff'][i].values())
    data.rename(columns={'f2': '最新价', 'f3': '涨跌幅', 'f4': '涨跌额', 'f12': '代码', 'f14': '品种', 'f15': '最高',
                            'f16': '最低', 'f17': '今开'}, inplace=True)
    data.drop(columns=['f1', 'f13', 'f152'], inplace=True)
    data['最新价'] = data['最新价'].apply(lambda x: round(int(x) / 10000, 4) if x != '-' else x)
    data['涨跌幅'] = data['涨跌幅'].apply(lambda x: str(round(int(x) / 10000, 2)) + '%' if x != '-' else x)
    data['涨跌额'] = data['涨跌额'].apply(lambda x: round(int(x) / 10000, 2) if x != '-' else x)
    data['最高'] = data['最高'].apply(lambda x: round(int(x) / 10000, 2) if x != '-' else x)
    data['最低'] = data['最低'].apply(lambda x: round(int(x) / 10000, 2) if x != '-' else x)
    data['今开'] = data['今开'].apply(lambda x: round(int(x) / 10000, 2) if x != '-' else x)
    data['更新时间'] = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    return data


def main():
    df = get_forex_data()
    df = data_process(df)