# coding:utf-8

class error_handler():

    def __init__(self):
        self.error_info = {
            "":"",

        }

    def set_error(self,error_desc):
        print self.error_info[error_desc]


