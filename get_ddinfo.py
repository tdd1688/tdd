# coding:utf-8

import requests
from random import choice
class get_ddinfo():

    def __init__(self):
        self.url = 'http://www.aokuu.net.cn/index.php/IH78fhgER04/Back/getdidan2'

    def get_one_from_ddlist(self):
        print "in get_dd_list step "

        rt = requests.get(self.url)
        rt_json = rt.json()
        print rt.status_code
        print 'total dd counts =',len(rt_json)
        for k in rt_json:
            print k

        self.select_one_dd = choice(rt_json)
        print "select_one_dd ==",self.select_one_dd
        return self.select_one_dd

    def get_dd_info(self):
        self.dd_info = self.select_one_dd
        return self.dd_info


if __name__ == "__main__":
    get_ddinfo().get_one_from_ddlist()

