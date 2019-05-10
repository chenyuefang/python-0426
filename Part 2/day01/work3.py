import requests
from lxml import etree
import re


def parse(url):
    # 得到HMTL文档
    html = requests.get(url)

    # 解析文档
    # 获取豆瓣top250中页面的标题
    selector = etree.HTML(html.text)

    all_movies = []

    movies_list = selector.xpath("//ol[@class='grid_view']/li")
    for movie_selector in movies_list:
        name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]  # 名称
        star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]  # 评分
        nums = movie_selector.xpath(".//div[@class='star']/span[last()]/text()")[0]  # 人数
        nums = re.sub("\D", "", nums)  # 正则表达式
        director_and_act = movie_selector.xpath(".//div[@class='bd']/p[1]/text()")[0].strip("\n").strip(" ")
        director = re.findall("导演: (.*?) ", director_and_act)[0]  # "导演 (.*?) : 截取开头是导演+空格，到第一个空格之间的内容
        act = re.findall("主演: (.*?) ", director_and_act)
        if not act:
            act = ["未知"]

        url = movie_selector.xpath(".//div[@class='hd']/a/@href")[0]
        one_movie = [name, star, nums, director, url]

        all_movies.append(one_movie)

    print(all_movies)

    for movie in all_movies:
        one_str = movie[0] + "," + movie[1] + "," + movie[2] + "," + movie[3] +movie[4]+ "\n"
        with open("movies3.txt", "a", encoding="utf-8") as f:
            f.write(one_str)

    next_url = selector.xpath("//span[@class='next']/a/@href")  # 爬取后页内容
    if next_url:  # 判断
        next_url = "https://movie.douban.com/top250" + next_url[0]
        parse(next_url)  # 重新调用 parse(url):  执行文档的爬取


if __name__ == "__main__":
    parse("https://movie.douban.com/top250")
