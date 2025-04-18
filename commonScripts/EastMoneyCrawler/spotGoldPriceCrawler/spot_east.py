import datetime
import time
import pandas as pd
import requests
import re


def gold_quotes_east(category: str = '上海黄金现货') -> pd.DataFrame:
    """
    东方财富网-黄金市场（部分时间段不更新）
    :param category: 种类，上海黄金现货、上海黄金期货、国际贵金属现货、国际贵金属期货
    :return: 黄金行情表
    """
    params = {
        'np': '1',
        'fltt': '1',
        'invt': '2',
        'fields': 'f12,f13,f14,f1,f2,f4,f3,f152,f17,f28,f15,f16,f124',
        'fid': 'f3',
        'pn': '1',
        'pz': '20',
        'po': '1',
        'dect': '1',
        'wep2u': '|0|0|0|web'
    }
    match category:
        case '上海黄金现货':
            params.update({'fs': 'm:118'})
        case '上海黄金期货':
            params.update({'fs': 'm:113+t:5'})
        case '国际贵金属现货':
            params.update({'fs': 'm:122,m:123'})
        case '国际贵金属期货':
            params.update({'fs': 'i:111.JAGC,i:101.QI00Y,i:111.JPAC,i:101.HG00Y,i:111.JAUC,i:111.JPLC,i:102.PL00Y,i:101.QO00Y,i:101.MGC00Y,i:101.GC00Y,i:101.SI00Y,i:102.PA00Y'})
        case _:
            raise ValueError('invalid error value specified')
    null = 'null'
    page = 0
    result = []
    while True:
        page += 1
        params.update({'pn': page})
        url = f'https://push2.eastmoney.com/api/qt/clist/get'
        response = requests.get(url, params=params)
        data = response.text
        df = eval(data)
        if df['data'] != 'null':
            df = df['data']['diff']
            for i in df:
                dict = {
                    '最新价': i['f2'],
                    '涨跌幅(%)': i['f3'],
                    '涨跌额': i['f4'],
                    '代码': i['f12'],
                    '品种': i['f14'],
                    '最高价': i['f15'],
                    '最低价': i['f16'],
                    '今开': i['f17'],
                    '昨结': i['f28'],
                    '更新时间': i['f124'],
                }
                result.append(dict)
        else:
            break
    data = pd.DataFrame(result)
    data['最新价'] = pd.to_numeric(data['最新价'], errors='coerce')/100
    data['涨跌幅(%)'] = pd.to_numeric(data['涨跌幅(%)'], errors='coerce')/100
    data['涨跌额'] = pd.to_numeric(data['涨跌额'], errors='coerce')/100
    data['最高价'] = pd.to_numeric(data['最高价'], errors='coerce')/100
    data['最低价'] = pd.to_numeric(data['最低价'], errors='coerce')/100
    data['今开'] = pd.to_numeric(data['今开'], errors='coerce')/100
    data['昨结'] = pd.to_numeric(data['昨结'], errors='coerce')/100
    data['更新时间'] = pd.to_datetime(data['更新时间']+28800, unit='s')
    data.fillna('-', inplace=True)
    return data



if __name__ == '__main__':
    gold_quotes_east_df = gold_quotes_east()
    print(gold_quotes_east_df)