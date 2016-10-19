# coding:utf-8

from get_ddinfo import *
from make_barcode import *
from make_fw_barcode import *
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os

class run():

    def __init__(self):
        pass

    def delete_pngs(self,kdnumber):
        self.barcode_png = 'barcode\\' + kdnumber + '.png'
        print self.barcode_png
        if os.path.exists(self.barcode_png):
            os.remove(self.barcode_png)


if __name__ == "__main__":
    ddinfo_dict = get_ddinfo().get_one_from_ddlist()
    kdnumber = ddinfo_dict['KDNumber']
    kdcompany = str(ddinfo_dict['KDCompany']).encode('utf-8')
    print kdcompany,kdnumber,len(kdnumber)
    barcode_png,barcode_jsf = make_barcode().create_bar_code(kdcompany, kdnumber, len(kdnumber))
    make_fw_barcode().make_kdnumber_png(barcode_png)



    # run().delete_pngs(kdnumber)