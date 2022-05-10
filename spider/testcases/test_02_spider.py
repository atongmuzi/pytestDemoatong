import re
from common.spider import spider


# 定义一个爬虫类
class TestMovieSpider:
    def test_movie_new_round(self):
        url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        for i in range(1, 4):
            i += 1
            # 拼接url
            url = url.format(i)
            html = spider.get_html(url)
            # 打印匹配数据,创建正则表达式对象
            patton = re.compile(r'<a href="(.*?)".*?>(.*?)</a>.*?◎译 名 (.*?)◎片 名', re.S)
            re_list = patton.findall(html)
            # 定义路径
            csv_name = 'result.csv'
            for r_info in re_list:
                link = r_info[0]
                movie_name = r_info[1]
                movie_rename = r_info[2]
                print("link:{},movie_name:{},movie_rename:{}".format(link, movie_name, movie_rename))
                spider.save_csv(csv_name, [link, movie_name, movie_rename], 'a')
            # 定义路径
            filename = 'new_movie.html'
            spider.save_html(filename, html, 'a')