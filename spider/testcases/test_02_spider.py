import re
from common.spider import spider
import pytest
from spider.testcases.movie_test.new_movie_serch import one_level_serch


class TestMovieSpider:
    @pytest.mark.usefixtures("movie_csv_header_write")
    def test_movie_new_round(self):
        for i in range(1, 2):
            url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
            one_level_serch(url)
            i += 1
