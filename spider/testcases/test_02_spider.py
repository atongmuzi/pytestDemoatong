import re
from common.spider import spider
from spider.testcases.novel.novel import lunyu_charper
import pytest
from spider.testcases.movie_test.new_movie_serch import one_level_serch
from spider.testcases.admin.admin_api import admin


class TestMovieSpider:
    @pytest.mark.usefixtures("movie_csv_header_write")
    def test_movie_new_round(self):
        for i in range(1, 2):
            url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
            one_level_serch(url)
            i += 1

    def test_novel_parse(self):
        url = 'http://www.jjwxc.net/onebook.php?novelid=4735894'
        lunyu_charper(url)

    def test_admin_modify(self):
        admin.modify_login_white_phone_api('13656199033')

