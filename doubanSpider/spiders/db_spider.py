import re

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader

from doubanSpider.items import MovieItem
import scrapy


class db_spider(scrapy.Spider):
    name="douban"
    alowed_domains=['http://movie.douban.com/']
    start_urls=['https://movie.douban.com/subject/26266893/',
                'https://movie.douban.com/subject/1652587/',
                'https://movie.douban.com/subject/24773958/',
                'https://movie.douban.com/subject/24773958/'
                ]
            
    def parse(self,response):
        movie=MovieItem()
        movie['m_co_l']=response.xpath('//a[@class="nbgnbg"]/img/@src').get()
        movie['m_nam']=response.xpath('/html/body/div[3]/div[1]/h1/span[1]/text()').get()
        movie['m_cat']=response.xpath('//span[@property="v:genre"]/text()').getall()
        list=response.xpath('//div[@id="info"]//text()').re(r'[\u4e00-\u9fa5a-zA-Z\(\)0-9\-·/]+')
            #导演-乔·庄斯顿-编剧-克里斯托弗·马库斯-斯蒂芬·麦克菲利-乔·西蒙-杰克·科比-主演-克里斯·埃文斯
            # -海莉·阿特维尔-塞巴斯蒂安·斯坦-汤米·李·琼斯-雨果·维文-多米尼克·库珀-理查德·阿米蒂奇-斯坦利·
            # 图齐-塞缪尔·杰克逊-托比·琼斯-尼尔·麦克唐纳-德里克·卢克-肯尼斯·崔-约翰·约瑟夫·菲尔德-类型-动作
            # -科幻-冒险-制片国家-地区-美国-语言-英语-挪威语-法语-上映日期-2011-09-09(中国大陆)-2011-07-
            # 19(加州首映)-2011-07-22(美国)-片长-124分钟(美国)-又名-复仇者先锋-链接-0458339
        str='-'
        str=str.join(list)
        movie['m_area']=re.search('地区-(.*)-语言',str).group(1)
        movie['m_area']=movie['m_area'].split('-/-',-1)
        movie['m_lan']=re.search('语言-(.*)-上映',str).group(1).split("-/-",-1)
        els_list=re.search('又名-(.*)-IMDb链接',str).group(1).split("/",-1)
        for index in range(len(els_list)):
            els_list[index]=re.sub('-',"",els_list[index])
        movie['m_elsename']=els_list
        list1=response.xpath('//span[@property="v:initialReleaseDate"]/text()').re(r'\((.*)\)')
        list2=response.xpath('//span[@property="v:initialReleaseDate"]/text()').re(r'\d{4}-\d{2}-\d{2}')
        movie['m_relea_tim_reg']=dict(zip(list1,list2))
        movie['m_len']=response.xpath('//span[@property="v:runtime"]/text()').re(r'\d+')
        movie['m_IMDb_l']=response.xpath('//span[contains(., "IMDb链接:")]/following-sibling::a[1]/@href').get()
        movie['m_tag']=response.xpath('//div[@class="tags-body"]/a/text()').getall()
        if response.xpath('//span[@class="all hidden"]').get() is not None:
            list=response.xpath('//span[@class="all hidden"]/text()').re(r'[\w()、，：:]+')
            str='-'
            movie['m_sum']=str.join(list)
        else:
            list=response.xpath('//span[@property="v:summary"]/text()').re(r'[\w()、，：:]+')
            str='-'
            movie['m_sum']=str.join(list)
        #list=response.xpath('//div[@ id="link-report"/text()').re(r'[\u4e00-\u9fa50-9a-zA-Z\(\)/,]+')
        #str=' '
        #movie['m_sum']=str.join(list)
        yield movie

        for index in range(len(list2)):
            list2[index]=re.sub('-',"",list2[index])
...     
'''
process=CrawlerProcess()
process.crawl(db_spider)
process.start()
'''