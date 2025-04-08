import time
import requests
import re
import pandas as pd
import datetime

def get_index_data(area):
    now = time.time()
    match area:
        case '亚洲' | 'Asia' | '亚洲指数': 
            url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37109280084931775681_{now}&fs=i%3A1.000001%2Ci%3A0.399001%2Ci%3A0.399005%2Ci%3A0.399006%2Ci%3A1.000300%2Ci%3A100.HSI%2Ci%3A100.HSCEI%2Ci%3A124.HSCCI%2Ci%3A100.TWII%2Ci%3A100.N225%2Ci%3A100.KOSPI200%2Ci%3A100.KS11%2Ci%3A100.STI%2Ci%3A100.SENSEX%2Ci%3A100.KLSE%2Ci%3A100.SET%2Ci%3A100.PSI%2Ci%3A100.KSE100%2Ci%3A100.VNINDEX%2Ci%3A100.JKSE%2Ci%3A100.CSEALL&fields=f12%2Cf13%2Cf14%2Cf292%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16%2Cf7%2Cf124&fid=f3&pn=1&pz=30&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb'
        case '欧洲' | 'Europe' | '欧洲指数':
            url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37109280084931775681_{now}&fs=i%3A100.SX5E%2Ci%3A100.FTSE%2Ci%3A100.MCX%2Ci%3A100.AXX%2Ci%3A100.FCHI%2Ci%3A100.GDAXI%2Ci%3A100.RTS%2Ci%3A100.IBEX%2Ci%3A100.PSI20%2Ci%3A100.OMXC20%2Ci%3A100.BFX%2Ci%3A100.AEX%2Ci%3A100.WIG%2Ci%3A100.OMXSPI%2Ci%3A100.SSMI%2Ci%3A100.HEX%2Ci%3A100.OSEBX%2Ci%3A100.ATX%2Ci%3A100.MIB%2Ci%3A100.ASE%2Ci%3A100.ICEXI%2Ci%3A100.PX%2Ci%3A100.ISEQ&fields=f12%2Cf13%2Cf14%2Cf292%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16%2Cf7%2Cf124&fid=f3&pn=1&pz=30&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb'
        case '美洲' | 'America' | '美洲指数':
            url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37109280084931775681_{now}&fs=i%3A100.DJIA%2Ci%3A100.SPX%2Ci%3A100.NDX%2Ci%3A100.TSX%2Ci%3A100.BVSP%2Ci%3A100.MXX&fields=f12%2Cf13%2Cf14%2Cf292%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16%2Cf7%2Cf124&fid=f3&pn=1&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb'
        case '澳洲' | 'Australia' | '澳洲指数':
            url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37109280084931775681_1744079388853&fs=i%3A100.AS51%2Ci%3A100.AORD%2Ci%3A100.NZ50&fields=f12%2Cf13%2Cf14%2Cf292%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16%2Cf7%2Cf124&fid=f3&pn=1&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb'
        case '其他' | 'other' | '其他指数':
            url = f'https://push2.eastmoney.com/api/qt/clist/get?np=1&fltt=1&invt=2&cb=jQuery37109280084931775681_1744079388855&fs=i%3A100.UDI%2Ci%3A100.BDI%2Ci%3A100.CRB&fields=f12%2Cf13%2Cf14%2Cf292%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf17%2Cf18%2Cf15%2Cf16%2Cf7%2Cf124&fid=f3&pn=1&pz=20&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb'
    
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
    data.rename(columns={'f2': '最新价', 'f3': '涨跌幅', 'f4': '涨跌额', 'f7': '振幅', 'f12': '代码', 'f14': '名称', 'f15': '最高价',
                        'f16': '最低价', 'f17': '开盘价', 'f18': '昨收价', 'f28': '昨结', 'f124': '最新行情时间'}, inplace=True)
    data.drop(columns=['f1', 'f13', 'f152', 'f292'], inplace=True)
    data['最新价'] = data['最新价'].apply(lambda x: round(int(x) / 100, 4) if x != '-' else x)
    data['涨跌幅'] = data['涨跌幅'].apply(lambda x: str(round(int(x) / 100, 2)) + '%' if x != '-' else x)
    data['涨跌额'] = data['涨跌额'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['振幅'] = data['振幅'].apply(lambda x: str(round(int(x) / 100, 2)) + '%' if x != '-' else x)
    data['最高价'] = data['最高价'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['最低价'] = data['最低价'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['开盘价'] = data['开盘价'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['昨收价'] = data['昨收价'].apply(lambda x: round(int(x) / 100, 2) if x != '-' else x)
    data['最新行情时间'] = data['最新行情时间'].apply(lambda x: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    return data

def main():
    df = get_index_data('Asia')
    df = data_process(df)
    return df