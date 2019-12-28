# 图片二值化
import os
from PIL import Image


def file_full_names(dir):
    lst = []
    for root, sub_dirs, filenames in os.walk(dir):
        for fname in filenames:
            s = os.path.join(root, fname)
            lst.append(s)
    return lst


def filter_filename(lst, filter=None):
    if filter is None:
        filter = ['.jpg', '.JPG']
    res = []
    for fname in lst:
        if fname[-4:] in filter:
            res.append(fname)
    return res


def modified_filename(filename, m='_modified'):
    return filename[:-4] + m + filename[-4:]


if __name__ == '__main__':
    fullnames = file_full_names(r'D:\学习\计算智能历年试题\2011')
    fullnames = filter_filename(fullnames)
    for img_path in fullnames:
        # img_path = r"D:\学习\计算智能历年试题\2018\IMG_20190113_092457.jpg"
        img = Image.open(img_path)
        # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
        img = img.convert('L')
        # Img.save("test1.jpg")
        # 自定义灰度界限，<这个值为黑色，>=这个值为白色
        threshold = 85
        table = [0 if i < threshold else 1 for i in range(256)]
        # for i in range(256):
        #     if i < threshold:
        #         table.append(0)
        #     else:
        #         table.append(1)
        # 图片二值化
        photo = img.point(table, '1')
        photo.save(modified_filename(img_path))
