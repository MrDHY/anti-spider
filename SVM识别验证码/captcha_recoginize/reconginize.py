import os
import re
import warnings
import numpy as np
from PIL import Image
from collections import Counter
from sklearn.externals import joblib
from captcha_recoginize.config import *


class reconginize:
    def __init__(self):
        warnings.filterwarnings('ignore')
        self.svc_linear_2 = joblib.load(model_path_2)
        self.svc_linear_3 = joblib.load(model_path_3)
        self.svc_linear_4 = joblib.load(model_path_4)
        self.svc_linear_5 = joblib.load(model_path_5)
        self.svc_linear_6 = joblib.load(model_path_6)
        self.svc_linear_7 = joblib.load(model_path_7)
        self.svc_linear_8 = joblib.load(model_path_8)
        self.svc_linear_9 = joblib.load(model_path_9)
        self.svc_linear_a = joblib.load(model_path_a)
        self.svc_linear_b = joblib.load(model_path_b)
        self.svc_linear_c = joblib.load(model_path_c)
        self.svc_linear_d = joblib.load(model_path_d)
        self.svc_linear_e = joblib.load(model_path_e)
        self.svc_linear_f = joblib.load(model_path_f)
        self.svc_linear_h = joblib.load(model_path_h)
        self.svc_linear_k = joblib.load(model_path_k)
        self.svc_linear_m = joblib.load(model_path_m)
        self.svc_linear_n = joblib.load(model_path_n)
        self.svc_linear_r = joblib.load(model_path_r)
        self.svc_linear_x = joblib.load(model_path_x)

    @staticmethod
    def get_img(image_path):
        image = Image.open(image_path)
        return image

    def pix(self, im, w, h, n):
        if not os.path.exists(denoising_path):
            os.mkdir(denoising_path)
        data = im
        # 图片的长宽
        w = w
        h = h
        for x in range(w):
            if x == 0:  # 去除左边界的噪点
                right = x + 1
                for y in range(0, h):
                    if y == 0:
                        down = y + 1
                        right_color = data.getpixel((right, y))
                        down_color = data.getpixel((x, down))
                        right_down_color = data.getpixel((right, down))
                        item_list = [right_color, down_color, right_down_color]
                        count = self.count_black(item_list)
                        if count <= max_black_count:
                            data.putpixel((x, y), 255)
                    elif y == h - 1:
                        up = y - 1
                        up_color = data.getpixel((x, up))
                        right_color = data.getpixel((right, y))
                        right_up_color = data.getpixel((right, up))
                        item_list = [up_color, right_color, right_up_color]
                        count = self.count_black(item_list)
                        if count <= max_black_count:
                            data.putpixel((x, y), 255)
                    else:
                        up = y - 1
                        down = y + 1
                        up_color = data.getpixel((x, up))
                        down_color = data.getpixel((x, down))
                        right_color = data.getpixel((right, y))
                        right_up_color = data.getpixel((right, up))
                        right_down_color = data.getpixel((right, down))
                        item_list = [up_color, right_color, right_up_color, down_color, right_down_color]
                        count = self.count_black(item_list)
                        if count <= max_black_count:
                            data.putpixel((x, y), 255)
            if x == w - 1:  # 去除右边界的噪点
                left = x - 1
                for y in range(0, h):
                    if y == 0:
                        down = 1
                        left_color = data.getpixel((left, y))
                        left_down_color = data.getpixel((left, down))
                        down_color = data.getpixel((x, down))
                        if data.getpixel((x, y)) == 0:
                            item_list = [left_color, left_down_color, down_color]
                            count = self.count_black(item_list)
                            if count <= max_black_count:
                                data.putpixel((x, y), 255)
                    elif y == h - 1:
                        if data.getpixel((x, y)) == 0:
                            up = y - 1
                            up_color = data.getpixel((x, up))
                            left_color = data.getpixel((left, y))
                            left_up_color = data.getpixel((left, up))
                            if data.getpixel((x, y)) == 0:
                                item_list = [left_color, left_up_color, up_color]
                                count = self.count_black(item_list)
                                if count <= max_black_count:
                                    data.putpixel((x, y), 255)
                    else:
                        if data.getpixel((x, y)) == 0:
                            up = y - 1
                            down = y + 1
                            up_color = data.getpixel((x, up))
                            down_color = data.getpixel((x, down))
                            left_color = data.getpixel((left, y))
                            left_down_color = data.getpixel((left, down))
                            left_up_color = data.getpixel((left, up))
                            item_list = [up_color, down_color, left_color, left_down_color, left_up_color]
                            count = self.count_black(item_list)
                            if count <= max_black_count:
                                data.putpixel((x, y), 255)
            if 0 < x < w - 1:
                # 获取目标像素点左右位置
                left = x - 1
                right = x + 1
                for y in range(h):
                    if y == 0:  # 去除上边界的噪点
                        down = y + 1
                        down_color = data.getpixel((x, down))
                        left_color = data.getpixel((left, y))
                        left_down_color = data.getpixel((left, down))
                        right_color = data.getpixel((right, y))
                        right_down_color = data.getpixel((right, down))
                        item_list = [right_color, down_color, left_color, left_down_color, right_down_color]
                        count = self.count_black(item_list)
                        print(n, count)
                        if count <= max_black_count:
                            data.putpixel((x, y), 255)
                    elif y == h - 1:  # 去除下边界的噪点
                        if data.getpixel((x, y)) == 0:
                            try:
                                up = y - 1
                                up_color = data.getpixel((x, up))
                                left_color = data.getpixel((left, y))
                                left_up_color = data.getpixel((left, up))
                                right_color = data.getpixel((right, y))
                                right_up_color = data.getpixel((right, up))
                                item_list = [up_color, right_up_color, left_color, right_color, left_up_color]
                                count = self.count_black(item_list)
                                if count <= max_black_count:
                                    data.putpixel((x, y), 255)
                            except Exception as e:
                                pass
                    else:
                        if data.getpixel((x, y)) == 0:  # 去除中心区域的噪点
                            # 获取目标像素点上下位置
                            up = y - 1
                            down = y + 1
                            try:
                                up_color = data.getpixel((x, up))
                                down_color = data.getpixel((x, down))
                                left_color = data.getpixel((left, y))
                                left_down_color = data.getpixel((left, down))
                                left_up_color = data.getpixel((left, up))
                                right_color = data.getpixel((right, y))
                                right_up_color = data.getpixel((right, up))
                                right_down_color = data.getpixel((right, down))
                                item_list = [up_color, down_color, left_color, left_down_color, left_up_color,
                                             right_color,
                                             right_up_color, right_down_color]
                                count = self.count_black(item_list)
                                if count <= max_black_count:
                                    data.putpixel((x, y), 255)
                            except Exception:
                                pass
                            else:
                                pass
        file_name = n.split('/')[2]
        data.save("{0}/{1}".format(denoising_path, file_name), "png")  # 保存图片

    @staticmethod
    def count_black(item_list):
        count_dict = Counter(item_list)
        count = count_dict[0]
        return count

    @staticmethod
    def convert_image(image, n):
        if not os.path.exists(black_white_path):
            os.mkdir(black_white_path)
        image = image.convert('L')  # 灰度
        image2 = Image.new('L', image.size, 255)
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixel = image.getpixel((x, y))
                if pixel < gray_value:  # 灰度低于134 设置为 0
                    image2.putpixel((x, y), 0)
        image2.save('{0}/{1}'.format(black_white_path, n))  # 将灰度图存储下来看效果
        return image2

    @staticmethod
    def cut_img(file_path):
        name = re.findall('\d+', file_path)[0]
        if not os.path.exists(name):
            os.mkdir(name)
        img = Image.open(file_path)
        w = image_w  # 设置切割图片的宽度
        h = image_h  # 设置切割图片的高度
        region = img.crop((offset_x, offset_y, offset_x + w, offset_y + h))
        region1 = img.crop((offset_x + w, offset_y, 2 * w + offset_x, offset_y + h))
        region2 = img.crop((2 * w + offset_x, offset_y, 3 * w + offset_x, offset_y + h))
        region3 = img.crop((3 * w + offset_x, offset_y, 4 * w + offset_x, offset_y + h))
        region.save('./{0}/{1}_1st.png'.format(name, name))
        region1.save('./{0}/{1}_2st.png'.format(name, name))
        region2.save('./{0}/{1}_3st.png'.format(name, name))
        region3.save('./{0}/{1}_4st.png'.format(name, name))

    @staticmethod
    def together_path(dir_list):  # 遍历一个文件夹的所有函数
        all_file_path = []
        for dir_name in dir_list:
            file_list = os.listdir('./{0}'.format(dir_name))
            for j in file_list:
                file_path = '{0}/{1}'.format(i, j)
                all_file_path.append(file_path)
        return all_file_path

    @staticmethod
    def maxtric_data(file_path):
        img = Image.open(file_path)
        data = img.getdata()
        data = np.matrix(data) / 255
        data1 = data.tolist()
        data2 = []
        for maxtric in data1:
            data2.extend(maxtric)
        return [data2]

    def get_content(self, a):
        result_list = [
            self.svc_linear_3.predict(a).tolist()[0],
            self.svc_linear_6.predict(a).tolist()[0],
            self.svc_linear_a.predict(a).tolist()[0],
            self.svc_linear_h.predict(a).tolist()[0],
            self.svc_linear_n.predict(a).tolist()[0],
            self.svc_linear_e.predict(a).tolist()[0],
            self.svc_linear_5.predict(a).tolist()[0],
            self.svc_linear_k.predict(a).tolist()[0],
            self.svc_linear_x.predict(a).tolist()[0],
            self.svc_linear_b.predict(a).tolist()[0],
            self.svc_linear_8.predict(a).tolist()[0],
            self.svc_linear_m.predict(a).tolist()[0],
            self.svc_linear_7.predict(a).tolist()[0],
            self.svc_linear_d.predict(a).tolist()[0],
            self.svc_linear_9.predict(a).tolist()[0],
            self.svc_linear_4.predict(a).tolist()[0],
            self.svc_linear_c.predict(a).tolist()[0],
            self.svc_linear_r.predict(a).tolist()[0],
            self.svc_linear_f.predict(a).tolist()[0],
            self.svc_linear_2.predict(a).tolist()[0]
        ]
        result = list(set(result_list))
        for item in result:
            if item != '0':
                return item
        return '0'

    def reconginize_single_img(self, cuted_img_path):
        maxtric_img = self.maxtric_data(cuted_img_path)
        data_content = self.get_content(maxtric_img)
        return data_content

    def reconginize_all_img(self, file_name_2):
        img_file_list = self.together_path(file_name_2)
        img_text_list = []
        for file in img_file_list:
            img_text_list.append(self.reconginize_single_img(file))
        text = ''.join(img_text_list)
        return text

    def recision_rmdir(self, dirname):
        dirname = dirname.replace('\\', '/')
        if os.path.isdir(dirname):
            for p in os.listdir(dirname):
                self.recision_rmdir(os.path.join(dirname, p))
            if os.path.exists(dirname):
                os.rmdir(dirname)
        else:
            if os.path.exists(dir):
                os.remove(dirname)

    def recongnize_main(self, image_path):
        file_name_1 = image_path.split('/')[-1].replace('jpeg', 'png')
        image = self.get_img(image_path)
        self.convert_image(image, file_name_1)
        black_img_path = '{0}/{1}'.format(black_white_path, file_name_1)
        self.cut_img(black_img_path)
        file_name_2 = file_name_1.split('.')[0]
        text = self.reconginize_all_img(file_name_2)
        self.recision_rmdir(file_name_2)
        return text

if __name__ == '__main__':
    b = reconginize()
    for i in range(10):
        print(b.recongnize_main('{0}/{1}.jpeg'.format('images', i)))