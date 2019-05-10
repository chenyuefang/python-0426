import requests
from lxml import etree

# 得到HMTL文档
html = requests.get("https://movie.douban.com/top250")

# 解析文档
# 获取豆瓣top250中页面的标题
selector = etree.HTML(html.text)
title = selector.xpath("/html/head/title/text()")
name = selector.xpath("//div[@class='hd']/a/span[1]/text()")
print(name)
