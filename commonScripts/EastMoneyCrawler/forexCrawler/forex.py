import requests
import re
import time
import pandas as pd


def get_forex_data(exchange_type):
    now = time.time()
    match exchange_type:
        case 'all' | '所有汇率':
            fs = 'm%3A119%2Cm%3A120%2Cm%3A133'
        case 'basic' | '基本汇率':
            fs = 'b%3AMK0300'
        case 'cross' | '交叉汇率':
            fs = 'b%3AMK0301'

    null = 'null'
    page = 0
    forex = []
    while True:
        page += 1
        print(f'正在爬取第{page}页')
        url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37104721282746568578_{now}&fs={fs}&fields=f12%2Cf13%2Cf14%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16&fid=f3&pn={page}&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb'
        response = requests.get(url)
        data = response.text
        r = re.compile('.*\((.*)\).*')
        data = r.findall(data)[0]
        df = eval(data)
        return data
        if df['data'] != 'null':
            df = df['data']['diff']
            for i in df:
                dict = {
                    '最新价': i['f2']/100,
                    '涨跌幅': str(i['f3']/100) + '%',
                    '涨跌额': i['f4']/100,
                    '代码': i['f12'],
                    '品种': i['f14'],
                    '最高价': i['f15']/100,
                    '最低价': i['f16']/100,
                    '今开': i['f17']/100,
                }
                forex.append(dict)
        else: 
            break
    return data
