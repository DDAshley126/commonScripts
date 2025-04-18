# 热点财经数据分析与信息推送系统

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

这是一个自动化的财经热点数据采集、分析和推送系统，能够实时获取股票、期货、黄金等热门数据，通过deepseek进行智能分析，生成数据报告并采用邮件推送。


## 模块架构
该系统主要由以下模块组成：

1、数据采集模块：获取实时热点数据

2、数据存储模块：获取的数据保存为json格式

3、异常监控模块：算法监控数据异常

4、数据可视化模块：生成图表

5、ai智能分析模块：调用deepseek api进行热门新闻总结和数据解读

6、报告生成模块：生成一份详细的数据报告/推动异常简报

7、推送模块：报告通过邮件发送/推送桌面通知

8、定时运行模块：设置任务定期自动运行



## 🚴 快速开始

### 环境要求
- Python 3.8+

### 安装步骤
1、克隆仓库
```commandline
git clone https://github.com/ddashley126/HotFinanceAnalysor.git
```
2、安装依赖
```commandline
pip install -r requirements.txt
```
3、配置环境变量

创建一个 `.env` 文件，包含以下内容：
```pycon
API_KEY = 'api_key'
API_URL = 'api_url'   # 如果不用deepseek就换成相应的url和api
EMAIL_
```

### 使用方法

运行主程序：
```bash
python main.py
```
