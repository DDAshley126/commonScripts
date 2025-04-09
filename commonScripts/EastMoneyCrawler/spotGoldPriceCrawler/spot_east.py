import datetime
import time
import pandas as pd
import requests
import re


def spot_quotes_east() -> pd.DataFrame:
    """
    东方财富网-上海黄金现货行情（部分时间段不更新）
    """
    now = time.time()
    url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37109255212463222533_{now}&fs=m%3A118&fields=f12%2Cf13%2Cf14%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf28%2Cf15%2Cf16%2Cf124&fid=f3&pn=1&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb'
    response = requests.get(url)
    data = response.text
    r = re.compile('.*\((.*)\).*')
    data = r.findall(data)[0]
    data = eval(data)
    data = pd.DataFrame([data['data']['diff'][0]])
    for i in range(1, len(data['data']['diff'])):
        data.loc[len(data)] = list(data['data']['diff'][i].values())
    data.rename(columns={'f2': '最新价', 'f3': '涨跌幅', 'f4': '涨跌额', 'f12': '代码', 'f14': '品种', 'f15': '最高',
                         'f16': '最低', 'f17': '今开', 'f28': '昨结', 'f124': '更新时间'}, inplace=True)
    data.drop(columns=['f1', 'f13', 'f152'], inplace=True)
    data['最新价'] = data['最新价'].apply(lambda x: round(int(x) / 100, 4) if x != '-' else x)
    data['涨跌幅'] = data['涨跌幅'].apply(lambda x: str(round(int(x) / 100, 2)) + '%' if x != '-' else x)
    data['涨跌额'] = data['涨跌额'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['最高'] = data['最高'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['最低'] = data['最低'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['今开'] = data['今开'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['昨结'] = data['昨结'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['更新时间'] = data['更新时间'].apply(
        lambda x: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    return data


if __name__ == '__main__':
    spot_quotes_east_df = spot_quotes_east()
    print(spot_quotes_east_df)