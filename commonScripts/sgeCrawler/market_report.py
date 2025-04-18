import requests
import re
import io
from bs4 import BeautifulSoup
import time


def weekly_report(path):
    """
    行情周报
    :path: 想要保存这些文件的路径
    :return: 0
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    href = []
    r = re.compile('.*href="(.*)" target.*')
    for page in range(1, 82):
        url = f'https://www.sge.com.cn/sjzx/hqzb?p={page}'
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html')
        download_href = soup.find_all(attrs={'class': 'txt fl', 'target': '_blank'})
        for i in download_href:
            href.append(r.findall(str(i))[0])

    # 2021年以前的路径是相对路径，要全部换成绝对路径
    for i in range(len(href)):
        if 'https://www.sge.com.cn' in href[i]:
            pass
        else:
            href[i] = 'https://www.sge.com.cn' + href[i][1:]
            
        response = requests.get(href[i], headers=headers)
        pdf_content = io.BytesIO(response.content)
        with open(path + u'/行情周报{}.pdf'.format(href[i][35:41] + href[i][42:44]), 'wb') as file:  
            file.write(pdf_content.read())
        time.sleep(5)
    return 0


def monthly_report(path):
    """
    行情月报
    :path: 想要保存这些文件的路径
    :return: 0
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    href = []
    r = re.compile('.*href="(.*)" target.*')
    for page in range(1, 26):
        url = f'https://www.sge.com.cn/sjzx/hqyb?p={page}'
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html')
        download_href = soup.find_all(attrs={'class': 'txt fl', 'target': '_blank'})
        for i in download_href:
            href.append(r.findall(str(i))[0])

    # 2021年以前的路径是相对路径，要全部换成绝对路径
    for i in range(len(href)):
        if 'https://www.sge.com.cn' in href[i]:
            pass
        else:
            href[i] = 'https://www.sge.com.cn' + href[i][1:]
            
        response = requests.get(href[i], headers=headers)
        pdf_content = io.BytesIO(response.content)
        with open(path + u'/行情月报{}.pdf'.format(href[i][35:41] + href[i][42:44]), 'wb') as file:  
            file.write(pdf_content.read())
        time.sleep(5)
    return 0


if __name__ == '__main__':
    weekly_report('/')
    monthly_report('/')