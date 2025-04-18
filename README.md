# commonScripts
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

#### 介绍
本仓库收集日常工作常用脚本，包括办公自动化、数据看板、pdf编辑、爬取数据等。

#### 文件结构
```
/commonScripts
├── DesktopNotification/ # 电脑桌面通知
│ └── desktop_notice.py
│
├── EastMoneyCrawler/ # 东财爬虫
│ ├── forexCrawler
│ ├── spotGoldPriceCrawler
│ └── stockCrawler
|
├── amapAPI/ # 高德api获取地址信息
│ └── address_info.py
│
├── emailSend/ # 邮件发送
│ └── email_send.py
│
├── sgeCrawler/ # 上交所爬虫
│ └── spotgold_price.py
│
├── sinaCrawler/ # 新浪财经
│ └── forexCrawler
│
└── README.md
```

#### 注意事项
部分脚本采用了match...case...语法，该语法为Python3.10版本引入的新语法，故推荐使用3.10以上版本。