import re
from common.spider import spider
import pytest


# 定义一个爬虫类
class TestMovieSpider:
    @pytest.mark.usefixtures("movie_csv_header_write")
    def test_movie_new_round(self):
        for i in range(1, 4):
            url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
            print(url)
            html = spider.get_html(url)
            # 打印匹配数据,创建正则表达式对象
            patton = re.compile(r'<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>.*?日期：(.*?)</font>.*?◎译 名 (.*?)◎片 名 '
                                r'(.*?)◎年 代 (.*?)◎产 地 (.*?)◎类 别 (.*?)◎语 言 ', re.S)
            re_list = patton.findall(html)
            # 定义路径
            csv_name = 'result.csv'
            for r_info in re_list:
                move_link = 'https://www.dytt8.net{}'.format(r_info[0])
                movie_name = r_info[1]
                movie_date = r_info[2]
                movie_rename = r_info[3]
                movie_title = r_info[4]
                movie_age = r_info[5]
                movie_place = r_info[6]
                movie_category = r_info[7]
                spider.save_csv(csv_name, [movie_date, movie_name, move_link, movie_rename, movie_title,
                                           movie_age, movie_place, movie_category], 'a')
            # 定义路径
            filename = 'new_movie.html'
            spider.save_html(filename, html, 'a')
            i += 1
