import requests
import re
from decimal import Decimal


def get_exchange_data():
    headers = {
        'Referer': 'https://vip.stock.finance.sina.com.cn/'
    }
    url = f'https://hq.sinajs.cn/rn=wkc1a&list=fx_scnymdl,fx_scnymga,fx_scnymkd,fx_scnymmk,fx_scnymnt,fx_scnymop,fx_scnymro,fx_scnymru,fx_scnymsd,fx_scnymur,fx_scnymvr,fx_scnymwk,fx_scnymxn,fx_scnymxv,fx_scnymxx,fx_scnymyr,fx_scnymyx,fx_scnymzn,fx_scnynad,fx_scnyngn,fx_scnynio,fx_scnynok,fx_scnynox,fx_scnynpr,fx_scnynzd,fx_scnyomr,fx_scnypab,fx_scnypen,fx_scnypgk,fx_scnyphp,fx_scnypkr,fx_scnypkx,fx_scnypln,fx_scnyplx,fx_scnypyg,fx_scnyqar,fx_scnyron,fx_scnyrox,fx_scnyrsd,fx_scnyrub,fx_scnyrux,fx_scnyrwf,fx_scnysar,fx_scnysbd,fx_scnyscr,fx_scnysdg,fx_scnysek,fx_scnysgd,fx_scnyshp,fx_scnysle,fx_scnysll,fx_scnysos,fx_scnysrd,fx_scnyssp,fx_scnystd,fx_scnystn,fx_scnysvc,fx_scnysyp,fx_scnyszl,fx_scnythb,fx_scnythx,fx_scnytjs,fx_scnytmt,fx_scnytnd,fx_scnytop,fx_scnytry,fx_scnyttd,fx_scnytwd,fx_scnytzs,fx_scnyuah,fx_scnyugx,fx_scnyusd,fx_scnyuyu,fx_scnyuzs,fx_scnyvef,fx_scnyves,fx_scnyvnd,fx_scnyvuv,fx_scnywst,fx_scnyxaf,fx_scnyxcd,fx_scnyxcg,fx_scnyxcu,fx_scnyxdr,fx_scnyxof,fx_scnyxpf,fx_scnyyer,fx_scnyzac,fx_scnyzar,fx_scnyzmw,fx_scnyzwl'
    response = requests.get(url, headers=headers)
    result = response.text
    r = re.compile('.*var hq_str_fx_scny.*="(.*)";')
    data = r.findall(result)
    forex = []
    for i in data:
        list = i.split(',')
        dict = {
            '更新时间': list[0], # 更新时间为北京时间
            '最新价': list[2],
            '最高价': list[3],
            '振幅': list[4],
            '开盘价': list[5],
            '更新时间': list[0],
            '最高价': list[6],
            '最低价': list[7],
            '名称': list[9],
            '涨跌幅': str(Decimal(list[12])*100) + '%' if len(list[12]) != 0 else '-',
            '更新日期': list[-1],
        }
        forex.append(dict)
    return forex