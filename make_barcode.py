# coding:utf-8

class make_barcode():

    def __init__(self):
        self.barcode_define = {
            "圆通":[10,12,18],
            "申通":[12,13],
            "申通":[12,13],
            "申通":[12,13],
            "申通":[12,13],
            "申通":[12,13],
            "申通":[12,13],
            "申通":[12,13],
            "申通":[12,13],
            "申通":[12,13],
        }

        self.execode = {

        }

    def create_bar_code(self,kdcompany,kdnumber,dhlenth):
        print "in create_bar_code step"
        print locals()
        if not kdcompany in self.barcode_define.iterkeys():
            print kdcompany,"is not in self.barcode_define"
            return False

        if not dhlenth in self.barcode_define[kdcompany]:
            print dhlenth,"is not in",self.barcode_define[kdcompany]
            return False




if __name__ == "__main__":
    make_barcode().create_bar_code("圆通","808003953626",12)