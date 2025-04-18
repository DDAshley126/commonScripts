import requests
import pandas as pd


def stock_us_east() -> pd.DataFrame:
    """
    东方财富网-行情中心-美股市场-全部美股
    :return: 行情表
    """
    params = {
        'np': '1',
        'fltt': '1',
        'invt': '2',
        'fs': 'm:105,m:106,m:107',
        'fields': 'f12,f13,f14,f1,f2,f4,f3,f152,f17,f28,f15,f16,f18,f20,f115',
        'fid': 'f3',
        'pz': '20',
        'po': '1',
        'dect': '1',
        'wep2u': '|0|0|0|web'
    }

    null = 'null'
    page = 0
    result = []
    while True:
        page += 1
        params.update({'pn': page})
        print(f'正在爬取第{page}页')
        url = f'https://push2.eastmoney.com/api/qt/clist/get'
        response = requests.get(url, params=params)
        data = response.text
        df = eval(data)
        if df['data'] != 'null':
            df = df['data']['diff']
            for i in df:
                dict = {
                    '最新价（美元）': i['f2'],
                    '涨跌幅(%)': i['f3'],
                    '涨跌额': i['f4'],
                    '代码': i['f12'],
                    '品种': i['f14'],
                    '最高价': i['f15'],
                    '最低价': i['f16'],
                    '开盘价': i['f17'],
                    '昨收价': i['f28'],
                    '总市值（美元）': i['f20'],
                    '市盈率': i['f115'],
                }
                result.append(dict)
        else:
            break
    data = pd.DataFrame(result)
    data['最新价（美元）'] = pd.to_numeric(data['最新价（美元）'], errors='coerce')/1000
    data['涨跌幅(%)'] = pd.to_numeric(data['涨跌幅(%)'], errors='coerce')/100
    data['涨跌额'] = pd.to_numeric(data['涨跌额'], errors='coerce')/1000
    data['最高价'] = pd.to_numeric(data['最高价'], errors='coerce')/1000
    data['最低价'] = pd.to_numeric(data['最低价'], errors='coerce')/1000
    data['开盘价'] = pd.to_numeric(data['开盘价'], errors='coerce')/1000
    data['昨收价'] = pd.to_numeric(data['昨收价'], errors='coerce')/1000
    data['市盈率'] = pd.to_numeric(data['市盈率'], errors='coerce')/100
    return data


def stock_uk_east():
    """
    东方财富网-行情中心-英股市场-全部英股
    :return: 行情表
    """
    params = {
        'np': '1',
        'fltt': '1',
        'invt': '2',
        'fs': 'm:155+t:1,m:155+t:2,m:155+t:3,m:156+t:1,m:156+t:2,m:156+t:5,m:156+t:6,m:156+t:7,m:156+t:8',
        'fields': 'f12,f13,f14,f1,f2,f4,f3,f152,f17,f28,f15,f16,f18,f20,f115',
        'fid': 'f3',
        'pz': '20',
        'po': '1',
        'dect': '1',
        'wep2u': '|0|0|0|web'
    }

    null = 'null'
    page = 0
    result = []
    while True:
        page += 1
        params.update({'pn': page})
        print(f'正在爬取第{page}页')
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
                    '开盘价': i['f17'],
                    '昨收价': i['f28'],
                    '总市值': i['f20'],
                    '市盈率': i['f115'],
                }
                result.append(dict)
        else:
            break
    data = pd.DataFrame(result)
    data['最新价'] = pd.to_numeric(data['最新价'], errors='coerce')/1000
    data['涨跌幅(%)'] = pd.to_numeric(data['涨跌幅(%)'], errors='coerce')/100
    data['涨跌额'] = pd.to_numeric(data['涨跌额'], errors='coerce')/1000
    data['最高价'] = pd.to_numeric(data['最高价'], errors='coerce')/1000
    data['最低价'] = pd.to_numeric(data['最低价'], errors='coerce')/1000
    data['开盘价'] = pd.to_numeric(data['开盘价'], errors='coerce')/1000
    data['昨收价'] = pd.to_numeric(data['昨收价'], errors='coerce')/1000
    data['市盈率'] = pd.to_numeric(data['市盈率'], errors='coerce')/100
    return data


def stock_hk_east() -> pd.DataFrame:
    """
    东方财富网-行情中心-港股市场-全部港股
    :return: 行情表
    """
    params = {
        'np': '1',
        'fltt': '1',
        'invt': '2',
        'fs': 'm:128+t:3,m:128+t:4,m:128+t:1,m:128+t:2',
        'fields': 'f12,f13,f14,f19,f1,f2,f4,f3,f152,f17,f18,f15,f16,f5,f6',
        'fid': 'f3',
        'pz': '20',
        'po': '1',
        'dect': '1',
        'wep2u': '|0|0|0|web'
    }

    null = 'null'
    page = 0
    result = []
    while True:
        page += 1
        params.update({'pn': page})
        print(f'正在爬取第{page}页')
        url = f'https://push2.eastmoney.com/api/qt/clist/get'
        response = requests.get(url, params=params)
        data = response.text
        df = eval(data)
        print(df)
        if df['data'] != 'null':
            df = df['data']['diff']
            for i in df:
                dict = {
                    '最新价': i['f2'],
                    '涨跌幅(%)': i['f3'],
                    '涨跌额': i['f4'],
                    '成交量（股）': i['f5'],
                    '成交额': i['f6'],
                    '代码': i['f12'],
                    '品种': i['f14'],
                    '最高价': i['f15'],
                    '最低价': i['f16'],
                    '开盘价': i['f17'],
                    '昨收价': i['f18']
                }
                result.append(dict)
        else:
            break
    data = pd.DataFrame(result)
    data['最新价'] = pd.to_numeric(data['最新价'], errors='coerce')/1000
    data['涨跌幅(%)'] = pd.to_numeric(data['涨跌幅(%)'], errors='coerce')/100
    data['涨跌额'] = pd.to_numeric(data['涨跌额'], errors='coerce')/1000
    data['最高价'] = pd.to_numeric(data['最高价'], errors='coerce')/1000
    data['最低价'] = pd.to_numeric(data['最低价'], errors='coerce')/1000
    data['开盘价'] = pd.to_numeric(data['开盘价'], errors='coerce')/1000
    data['昨收价'] = pd.to_numeric(data['昨收价'], errors='coerce')/1000
    return data


if __name__ == '__main__':
    stock_us_east_df = stock_us_east()
    print(stock_us_east)

    stock_uk_east_df = stock_uk_east()
    print(stock_uk_east)

    stock_hk_east_df = stock_hk_east()
    print(stock_hk_east)