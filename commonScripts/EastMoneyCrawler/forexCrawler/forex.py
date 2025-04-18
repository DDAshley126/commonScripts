import requests
import re
import pandas as pd


def forex_quotation(exchange_type) -> pd.DataFrame:
    """
    东方财富网-外汇市场
    :param exchange_type: 汇率种类
    :return: 汇率表
    """
    params = {
        'np': '1',
        'fltt': '1',
        'invt': '2',
        'fields': 'f12,f13,f14,f1,f2,f4,f3,f152,f17,f18,f15,f16',
        'fid': 'f3',
        'pz': '20',
        'po': '1',
        'dect': '1',
        'wbp2u': '|0|0|0|web'
    }
    match exchange_type:
        case 'all' | '所有汇率':
            params.update({'fs': 'm:119,m:120,m:133'})
        case 'basic' | '基本汇率':
            params.update({'fs': 'b:MK0300'})
        case 'cross' | '交叉汇率':
            params.update({'fs': 'b:MK0301'})

    null = 'null'
    page = 0
    forex = []
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
                    '最新价': i['f2']/100,
                    '涨跌幅(%)': i['f3']/100,
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
    return pd.DataFrame(forex)


def forex_bank_quotation(bank='招商银行') -> pd.DataFrame:
    """
    东方财富网-外汇市场-外汇牌价
    :param bank: 银行名
    :return: 外汇牌价
    """
    params = {
        'np': '1',
        'fltt': '1',
        'invt': '2',
        'fields': 'f12,f14,f3,f152,f4,f31,f1,f142,f32,f143,f124',
        'fid': 'f3',
        'pn': '1',
        'pz': '20',
        'po': '1',
        'dect': '1',
        'wbp2u': '|0|0|0|web'
    }
    match bank:
        case '工商银行':
            params.update({'fs': 'm:162+s:1'})
        case '农业银行':
            params.update({'fs': 'm:162+s:2'})
        case '中国银行':
            params.update({'fs': 'm:162+s:4'})
        case '建设银行':
            params.update({'fs': 'm:162+s:8'})
        case '交通银行':
            params.update({'fs': 'm:162+s:16'})
        case '招商银行':
            params.update({'fs': 'm:162+s:32'})

    url = f'https://push2.eastmoney.com/api/qt/clist/get'
    response = requests.get(url, params=params)
    data = response.text
    data = data.replace('(', '')
    data = data.replace(')', '')
    r = re.compile('.*"diff":(.*)}}')
    data = r.findall(data)[0]
    df = eval(data)
    data = pd.DataFrame([df[0]])
    for i in range(1, len(df)):
        data.loc[len(data)] = list(df[i].values())
    data.rename(
        columns={'f12': '代码', 'f14': '品种', 'f31': '现汇买入价', 'f32': '现汇卖出价', 'f142': '现钞买入价', 'f143': '现钞卖出价', 'f124': '更新时间'}, inplace=True)
    data.drop(columns=['f1', 'f3', 'f4', 'f152'], inplace=True)
    data['现汇买入价'] = pd.to_numeric(data['现汇买入价'], errors='coerce')/10000
    data['现汇卖出价'] = pd.to_numeric(data['现汇卖出价'], errors='coerce')/10000
    data['现钞买入价'] = pd.to_numeric(data['现钞买入价'], errors='coerce') / 10000
    data['现钞卖出价'] = pd.to_numeric(data['现钞卖出价'], errors='coerce') / 10000
    data['更新时间'] = pd.to_datetime(data['更新时间']+28800, unit='s')     # 时区
    data.fillna('-', inplace=True)
    return data


if __name__ == '__main__':
    forex_quotation_df = forex_quotation()
    print(forex_quotation)

    forex_bank_quotation_df = forex_bank_quotation()
    print(forex_bank_quotation_df)