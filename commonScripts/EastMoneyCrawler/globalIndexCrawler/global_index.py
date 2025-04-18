import time
import requests
import re
import pandas as pd
import datetime

def market_index(area: str = 'Asia'):
    params = {
        'np': '1',
        'fltt': '1',
        'invt': '2',
        'fields': 'f12,f13,f14,f292,f1,f2,f4,f3,f152,f17,f18,f15,f16,f7,f124',
        'fid': 'f3',
        'pn': '1',
        'pz': '20',
        'po': '1',
        'dect': '1',
        'wep2u': '|0|0|0|web'
    }
    match area:
        case '亚洲' | 'Asia' | '亚洲指数': 
            params.update({'fs': 'i:1.000001,i:0.399001,i:0.399005,i:0.399006,i:1.000300,i:100.HSI,i:100.HSCEI,i:124.HSCCI,i:100.TWII,i:100.N225,i:100.KOSPI200,i:100.KS11,i:100.STI,i:100.SENSEX,i:100.KLSE,i:100.SET,i:100.PSI,i:100.KSE100,i:100.VNINDEX,i:100.JKSE,i:100.CSEALL'})    
        case '欧洲' | 'Europe' | '欧洲指数':
            params.update({'fs': 'i:100.SX5E,i:100.FTSE,i:100.MCX,i:100.AXX,i:100.FCHI,i:100.GDAXI,i:100.RTS,i:100.IBEX,i:100.PSI20,i:100.OMXC20,i:100.BFX,i:100.AEX,i:100.WIG,i:100.OMXSPI,i:100.SSMI,i:100.HEX,i:100.OSEBX,i:100.ATX,i:100.MIB,i:100.ASE,i:100.ICEXI,i:100.PX,i:100.ISEQ'})
        case '美洲' | 'America' | '美洲指数':
            params.update({'fs': 'i:100.DJIA,i:100.SPX,i:100.NDX,i:100.TSX,i:100.BVSP,i:100.MXX'})
        case '澳洲' | 'Australia' | '澳洲指数':
            params.update({'fs': 'i:100.AS51,i:100.AORD,i:100.NZ50'})
        case '其他' | 'other' | '其他指数':
            params.update({'fs': 'i:100.UDI,i:100.BDI,i:100.CRB'})

    url = 'https://push2.eastmoney.com/api/qt/clist/get'
    response = requests.get(url, params=params)
    data = response.text
    df = eval(data)
    df = df['data']['diff']
    result = []
    for i in df:
        dict = {
            '最新价': i['f2'],
            '涨跌幅(%)': i['f3'],
            '涨跌额': i['f4'],
            '振幅(%)': i['f7'],
            '代码': i['f12'],
            '品种': i['f14'],
            '最高价': i['f15'],
            '最低价': i['f16'],
            '今开': i['f17'],
            '昨收价': i['f18'],
            '最新行情时间': i['f124'],
        }
        result.append(dict)
    data = pd.DataFrame(result)
    data['最新价'] = pd.to_numeric(data['最新价'], errors='coerce')/100
    data['涨跌幅(%)'] = pd.to_numeric(data['涨跌幅(%)'], errors='coerce')/100
    data['涨跌额'] = pd.to_numeric(data['涨跌额'], errors='coerce')/100
    data['振幅(%)'] = pd.to_numeric(data['振幅(%)'], errors='coerce')/100
    data['最高价'] = pd.to_numeric(data['最高价'], errors='coerce')/100
    data['最低价'] = pd.to_numeric(data['最低价'], errors='coerce')/100
    data['今开'] = pd.to_numeric(data['今开'], errors='coerce')/100
    data['昨收价'] = pd.to_numeric(data['昨收价'], errors='coerce')/100
    data['最新行情时间'] = pd.to_datetime(data['最新行情时间']+28800, unit='s')
    data.fillna('-', inplace=True)
    return data

if __name__ == '__main__':
    market_index_df = market_index()
    print(market_index_df)