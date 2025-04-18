import requests


def run(address):
    url = f'https://restapi.amap.com/v3/geocode/geo?address={address}&key={Your Key}'
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    dict = run('你想要查询的地址')
    print(dict)
