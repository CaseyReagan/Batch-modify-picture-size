import os
from PIL import Image


filename = os.listdir("./origin")   ##放原始图片的文件夹路径
base_dir = r"./origin/"    ## 放原始图片的文件夹路径
new_dir = r"./changed/"    ## 放新图片的文件路径

for img in filename:
    image = Image.open(base_dir + img)
    size_m, size_n = image.size
    size_m = int(size_m / 2)
    size_n = int(size_n / 2)
    image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
 #   image_size = image.resize((768, 1280), Image.NEAREST)   ## 最关键的函数在这里，你需要的时候只需要修改这一行resize后面的数字，注释掉前三行，使用这一行就可以了
    image_size.save(new_dir + img)
