# coding:utf-8



import Image

img = Image.open(r'barcode\518132270206.Png')
region = (100,200,400,500)

#裁切图片
cropImg = img.crop(region)

#保存裁切后的图片
cropImg.save(r'barcode\test.Png')