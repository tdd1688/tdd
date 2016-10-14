# coding:utf-8

from win32com import client
import os
import time
import SendKeys
from PIL import Image

class make_fw_barcode():
    def __init__(self):
        self.fw_path = '"C:\Program Files (x86)\Macromedia\Fireworks 8\Fireworks.exe"'


    def deal_color(self):
        img = Image.open('barcode\808003953626.png')

        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save("img2.png", "PNG")


    def make_kdnumber_png(self,barcode_png,barcode_jsf):
        print "in make_kdnumber_png step"
        if self.CheckProcExistByPN("Fireworks.exe"):
            print "Fireworks.exe is already exist"
        else:
            print "open Fireworks.exe "
            # os.system(self.fw_path)
            os.startfile(self.fw_path)
            print "open Fireworks done"
            time.sleep(15)


        os.system(barcode_png)
        time.sleep(10)
        SendKeys.SendKeys('+W')

        os.system(barcode_jsf)
        time.sleep(5)
        os.system('barcode_jsf\save.jsf')



    def CheckProcExistByPN(self,process_name):
      try:

        WMI = client.GetObject('winmgmts:')
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
      except Exception,e:
        print process_name + "error : ", e;
      if len(processCodeCov) > 0:
        print process_name + " exist";
        return True
      else:
        print process_name + " is not exist";
        return False




if __name__ == "__main__":
    # make_fw_barcode().make_kdnumber_png('barcode\808003953626.Png','barcode_jsf\code128C-12.jsf')
    make_fw_barcode().deal_color()
