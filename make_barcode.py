# coding:utf-8

import os


class make_barcode():
    def __init__(self):
        self.barcode_define = {
            "圆通": [10, 12, 18],
            "申通": [12, 13],
            "申通": [12, 13],
            "申通": [12, 13],
            "申通": [12, 13],
            "申通": [12, 13],
            "申通": [12, 13],
            "申通": [12, 13],
            "申通": [12, 13],
            "申通": [12, 13],
        }

        self.execode = {
            "全峰-12": "128C",
            "天天-12": "128C",
            "顺丰-12": "128C",
            "韵达-13": "128A",
            "申通-12": "128C",
            "中通-10": "39",
            "圆通-10": "128B",
            "圆通-12": "128C",
            "汇通-14": "128C",
            "邮政平邮-13": "128A",
            "邮政小包-13": "128A",
            "EMS-13": "39",
            "EMS经济-13": "128A",
            "EMS标准-13": "128A",
            "龙邦-12": "128C",
            "龙邦物流-12": "128C",
            "增益-12": "128C",
            "速尔-12": "128C",
            "优速-12": "128C",
            "汇强-12": "128C",
            "国通-10": "128C",
            "运通速运-10": "128C",
            "长发-16": "128C",
            "快捷-12": "128C",
            "凡宇-12": "128C",
            "宅急送-10": "128A",
            "佳吉物流-10": None,
            "急便送-15": "128C",
            "天益-10": "128C",
            "金鑫物流-14": "128C",
            "城市100-13": "128B",
            "能达-12": "128C",
            "飞康达-12": "39",

        }

    def create_bar_code(self, kdcompany, kdnumber, dhlength):
        print "in create_bar_code step"
        print locals()
        if not kdcompany in self.barcode_define.iterkeys():
            print kdcompany, "is not in self.barcode_define"
            return False

        if not dhlength in self.barcode_define[kdcompany]:
            print dhlength, "is not in", self.barcode_define[kdcompany]
            return False

        try:
            barcode_exe = self.execode[str(kdcompany) + "-" + str(dhlength)] + ".exe"
        except Exception, e:
            print e
            print "kdcompany, kdnumber, dhlength, is not match with barcode exe !"
            return False

        cmd = "barcode\\" + barcode_exe + " " + kdnumber
        print cmd
        os.system(cmd)

        barcode_png = "barcode\\" + str(kdnumber)+".png"
        return barcode_png


if __name__ == "__main__":
    make_barcode().create_bar_code("圆通", "808003953626", 12)
