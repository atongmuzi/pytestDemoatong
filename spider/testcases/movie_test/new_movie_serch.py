from common.spider import spider
from common.mysql_operate import db


def one_level_serch(url):
    print(url)
    html = spider.get_html(url)
    # 打印匹配数据,创建正则表达式对象
    re_list = spider.patton_result(
        r'<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>.*?日期：(.*?)</font>.*?◎译 名 (.*?)◎片 名 '
        r'(.*?)◎年 代 (.*?)◎产 地 (.*?)◎类 别 (.*?)◎语 言 ', html)
    # 定义路径
    csv_name = 'movie_test/result/result.csv'
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
        # 解析二级页面
        two_level_parse(move_link)


def two_level_parse(url):
    html = spider.get_html(url)
    # 打印匹配数据,创建正则表达式对象
    re_list = spider.patton_result(r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1>', html)
    # 插入数据库
    sql = "insert into movie_info(movie_name) values('%s')" % (re_list[0])
    # sql = "insert into movie_info(movie_name, movie_download) values('%s','%s')" % (re_list[0], re_list[1])
    db.execute_db(sql)
