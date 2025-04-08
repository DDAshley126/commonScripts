### EasyMoneyCrawler
本文件夹爬取的是东方财富网站的数据，包括实时股票数据、期货数据、黄金数据、外汇数据等。请注意，部分数据在工作日15时30分后停止更新。

#### 爬取内容
```
/EasyMoneyCrawler
├── forexCrwaler/ # 外汇爬虫
│ └── forex.py
|
├── stockCrwaler/ # 股价爬虫
| ├── sh_stock.py
│ └── sz_stock.py
│
├── spotGoldPriceCrawler/ # 黄金爬虫
│ └── spotgold_price.py
│
├── golbalIndexCrawler/ # 全球指数爬虫
│ └── global_index.py
|
└── README.md
```

#### 注意事项
1.请遵守目标网站的robots.txt协议

2.合理设置爬取间隔，避免对目标网站造成负担

3.请勿用于非法用途，本项目仅用于交流学习与日常备份