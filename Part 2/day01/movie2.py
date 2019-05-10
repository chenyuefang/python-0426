import requests
from lxml import etree

html = requests.get("https://movie.douban.com/top250")

selector = etree.HTML(html.text)

all_moive = []

movies_list = selector.xpath("//ol[@class='grid_view']/li")  # @属性名  @href
for movie_selector in movies_list:
    name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]  # 名称
    director = movie_selector.xpath(".//div[@class='bd']/p/text()")[0]  # 导演
    star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]  # 评分
    nums = movie_selector.xpath(".//div[@class='star']/span[last()]/text()")[0] # 人数
    nums = nums.split("人评价")[0]
    comment = movie_selector.xpath(".//div[@class='bd']/p[@class='quote']/span[@class='inq']/text()")[0]  # 评语
    url = movie_selector.xpath(".//div[@class='hd']/a/@href")[0]
    one_movie = [name, director, star, nums, comment, url]

    all_moive.append(one_movie)

print(all_moive)

for movie in all_moive:
    one_str = movie[0] + " ," + movie[1] + "," + movie[2] + "," + movie[3] + "," + movie[4] + "," + movie[5] + "\n"
    with open("movie2.txt", "a", encoding="utf-8") as f:
        f.write(one_str)
