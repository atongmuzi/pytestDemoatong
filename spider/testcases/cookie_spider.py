import requests
from lxml import etree
from common.spider import spider


class RenrenLogin():
    def __init__(self):
        # 个人主页的url地址
        self.url = 'https://www.jjwxc.net/fenzhan/yq/'
        self.headers = {
            # 将拷贝的cookie值放在此处
            'Cookie': 'timeOffset_o=-970; UM_distinctid=17d376a513e585-01e4ac2b97fb1-1c356857-13c680-17d376a513f839; '
                      '__yjs_duid=1_d369477570198cdf74cdd58277a0019f1641891127068; testcookie=yes; '
                      'smidV2=20210217180315da8efc623d075e08eb794e764ab5053200c2213c6a6c33400; '
                      'CNZZDATA30075907=cnzz_eid%3D1532331810-1634022289-https%253A%252F%252Fwww.baidu.com%252F'
                      '%26ntime%3D1649927481; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1652430131; '
                      'timeOffset_o=-230.10009765625; '
                      'token=Mzc3MTk0MzV8N2MzNzE4ZTYyZGYyNGJjYzhiY2Q3Yjk0ZDgyZjAxNDB8fHx8MjU5MjAwMHwxfHx85pmL5rGf55So5oi3fDF8bW9iaWxlfDE%3D; JJSESS=%7B%22clicktype%22%3A%22%22%2C%22sidkey%22%3A%22GnQKXrUmzwqDe0jsVEyF4TOaciMhdt5o12%22%2C%22returnUrl%22%3A%22http%3A//www.jjwxc.net/onebook.php%3Fnovelid%3D6217458%22%7D; JJEVER=%7B%22nicknameAndsign%22%3A%222%257E%2529%2524%25E9%2598%25BF%25E7%25AB%25A5%22%2C%22foreverreader%22%3A%2237719435%22%2C%22desid%22%3A%229QSv5CRuLAbTRyzOIs/mgOoL3w4R3Xey%22%2C%22sms_total%22%3A%220%22%2C%22lastCheckLoginTimePc%22%3A1652441036%2C%22fenzhan%22%3A%22yq%22%7D; Hm_lpvt_bc3b748c21fe5cf393d26c12b2c38d99=1652687969',
            # 注意，useragent不能改变，否则cookie失效
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/97.0.4692.71 Safari/537.36 '
        }

    def get_html(self):
        html = spider.get_request_html(self.url, 'gb18030', self.headers)
        self.parse_html(html)

    def parse_html(self, html):
        parse_html = etree.HTML(html)
        r_school = parse_html.xpath('//*[@id="menu3"]/li/text()')
        print(r_school)


if __name__ == '__main__':
    test = RenrenLogin()
    test.get_html()
