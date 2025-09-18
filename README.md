# 🕷️ MySpiderLab

> 个人 Python 爬虫学习仓库 —— 记录学习过程、示例代码与工具集合。

---

## 📌 仓库介绍
这个仓库主要记录我学习 Python 爬虫的过程，包含：
- 各种网页请求方法（`requests`、`httpx` 等）
- 常见的网页解析方式（`BeautifulSoup`、`lxml`、`XPath`、`re`）
- 模拟浏览器（`Selenium`、`Playwright`）
- 反爬机制与应对（Headers、代理池、验证码思路）
- 数据存储（CSV、JSON、数据库）

目标是：**边学边写，逐步积累一个自己的爬虫学习笔记库** 📝。

---

## 📂 目录结构

```
MySpiderLab/
├── basics/ # 基础语法 & 简单示例
│ ├── requests_demo.py
│ └── parse_html.py
├── parsing/ # HTML/XML 解析练习
│ ├── bs4_example.py
│ ├── xpath_demo.py
│ └── regex_demo.py
├── advanced/ # 高级爬虫（代理、反爬、异步）
│ ├── proxy_pool.py
│ ├── async_crawler.py
│ └── anti_scraping_notes.md
├── selenium/ # 浏览器模拟
│ ├── selenium_demo.py
│ └── playwright_demo.py
├── storage/ # 数据存储
│ ├── save_csv.py
│ ├── save_json.py
│ └── save_mysql.py
└── README.md
```

## 🚀 使用方法

### 1. 克隆仓库
```bash
git clone https://github.com/hxd77/MySpiderLab.git
cd MySpiderLab
```

### 2. 创建虚拟环境 & 安装依赖

```
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. 运行示例

```
python basics/requests_demo.py
```

## 🛠️ 依赖说明

常用依赖库：

- `requests` —— 发送 HTTP 请求
- `httpx` —— 异步 HTTP 客户端
- `beautifulsoup4` —— HTML 解析
- `lxml` —— XPath/HTML/XML 解析
- `selenium` —— 浏览器模拟
- `playwright` —— 现代浏览器自动化
- `pandas` —— 数据存储与处理

安装：

```
pip install requests beautifulsoup4 lxml selenium playwright pandas
```

## 📝 学习目标

-  学会使用 `requests` 获取网页
-  熟悉 `BeautifulSoup` 和 `XPath` 的解析方法
-  理解反爬虫机制并尝试突破
-  学习多线程、多进程和异步爬虫
-  学习 `Selenium` / `Playwright` 的用法
-  学会数据存储（CSV、JSON、数据库）

## 📒 学习笔记

这里记录一些心得与踩坑经验：

- **Headers 设置**：很多网站需要伪装浏览器 UA，否则会 403。
- **反爬策略**：遇到验证码、JS 渲染页面时，需要用 Selenium/Playwright。
- **数据存储**：小规模用 CSV/JSON，大规模最好上数据库。

------

## 📜 License

本仓库仅用于学习与研究，请勿将示例代码用于任何非法用途。
 MIT License © 2025 by hxd77

