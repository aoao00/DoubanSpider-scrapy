# DoubanSpider-scrapy
This is a Spider based on scrapy to crawl the information about all the movies on DouBan.

# 安装/Installation

本爬虫使用的是Scrapy爬虫框架，[文档](https://docs.scrapy.org/en/latest/index.html)。

```bash
pip install scrapy
git clone https://github.com/aoao00/DoubanSpider-scrapy.git
cd DoubanSpider-scrapy/doubanSpider
scrapy crawl douban
```

这个时候爬虫已经在运行了。

# 配置/Settings

爬取的数据会存储在`DoubanSpider-scrapy/doubanSpider/item.jl`中，如需存储数据到MongoDb，请打开`DoubanSpider-scrapy/doubanSpider/`中的settings.py。

```python
MONGO_URI='mongodb://127.0.0.1:27017' #修改为自己的mongodb数据库端口
MONGO_DATABASE='DOUBAN'
```

