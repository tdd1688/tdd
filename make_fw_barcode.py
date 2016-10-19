# coding:utf-8

from win32com import client
import os
import time
import SendKeys
import cv2

from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import random


class make_fw_barcode():
    def __init__(self):
        self.fw_path = '"C:\Program Files (x86)\Macromedia\Fireworks 8\Fireworks.exe"'

    def deal_color(self, barcode_png):
        print "in deal_color step"
        img = Image.open(barcode_png)

        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)

        img.save(barcode_png)

    def png_cut(self, barcode_png):
        print "in png_cut step"
        print barcode_png

        im = Image.open(barcode_png)
        print im.format, im.size, im.mode, im.info
        region = (0, 0, im.size[0], 150)

        # #裁切图片
        cropImg = im.crop(region)
        # #保存裁切后的图片
        # cropImg.save(r'barcode\test.png')
        cropImg.save(barcode_png)

        self.addnoise_setopacity()

        # image2 = cv2.imread(barcode_png)
        # noise_img = self.sp_noise(image2,0.05)
        # cv2.imwrite('noise.jpg', noise_img)

    def addnoise_setopacity(self, setopacity=80, noise_amount=15, gaussian_blur_radius=0.5):
        print "in addnoise_setopacity step"
        jsf_string = 'fw.getDocumentDOM().setOpacity({$setopacity});' \
                     'fw.getDocumentDOM().applyEffects(' \
                     '{ category:"UNUSED", effects:[ { EffectIsVisible:true, EffectMoaID:"{e4c0f4bc-c0a3-4cb3-b3513822027e4d9f}", MB_filter_preview_tile_size:"-1 -1", add_noise_amount:{$noise_amount}, add_noise_use_color:false, category:"\u6742\u70B9", name:"\u65B0\u589E\u6742\u70B9\u2026" }, ' \
                     '{ EffectIsVisible:true, EffectMoaID:"{d04ef8c0-71b3-11d1-8c8200a024cdc039}", MB_filter_preview_tile_size:"-1 -1", category:"\u6A21\u7CCA", gaussian_blur_radius:{$gaussian_blur_radius}, name:"\u9AD8\u65AF\u6A21\u7CCA..." } ], name:"UNUSED" });'

        data = jsf_string.replace('{$setopacity}', str(setopacity)).replace('{$noise_amount}',
                                                                            str(noise_amount)).replace(
            '{$gaussian_blur_radius}', str(gaussian_blur_radius))

        file = open(r'barcode_jsf\addnoise_setopacity_tmp.jsf', 'w')
        file.write(data)
        file.close()

        os.system(self.orginal_kd_barcode)
        time.sleep(10)
        SendKeys.SendKeys('+W')

        os.system(r'barcode_jsf\addnoise_setopacity_tmp.jsf')
        time.sleep(5)
        os.system('barcode_jsf\save.jsf')

    # add noise
    def sp_noise(self, image, prob):
        output = np.zeros(image.shape, np.uint8)
        thres = 1 - prob
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rdn = random.random()
                if rdn < prob:
                    output[i][j] = 0
                elif rdn > thres:
                    output[i][j] = 255
                else:
                    output[i][j] = image[i][j]
        return output

    def make_kdnumber_png(self, barcode_png):
        print "in make_kdnumber_png step"
        self.orginal_kd_barcode = barcode_png
        self.deal_color(barcode_png)
        self.png_cut(barcode_png)

    # def make_kdnumber_png(self,barcode_png,barcode_jsf):
    #     self.orginal_kd_barcode = barcode_png
    #     print "in make_kdnumber_png step"
    #     if self.CheckProcExistByPN("Fireworks.exe"):
    #         print "Fireworks.exe is already exist"
    #     else:
    #         print "open Fireworks.exe "
    #         # os.system(self.fw_path)
    #         os.startfile(self.fw_path)
    #         print "open Fireworks done"
    #         time.sleep(15)
    #
    #
    #     os.system(self.orginal_kd_barcode)
    #     time.sleep(10)
    #     SendKeys.SendKeys('+W')
    #
    #     os.system(barcode_jsf)
    #     time.sleep(5)
    #     os.system('barcode_jsf\save.jsf')



    def CheckProcExistByPN(self, process_name):
        print "in CheckProcExistByPN step"
        try:

            WMI = client.GetObject('winmgmts:')
            processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
        except Exception, e:
            print process_name + "error : ", e

        if len(processCodeCov) > 0:
            print process_name + " exist";
            return True
        else:
            print process_name + " is not exist"
            return False


if __name__ == "__main__":
    make_fw_barcode().make_kdnumber_png(r'barcode\518132270206.Png')

