import os
import re
import requests
from PIL import Image
from collections import Counter
from gen_train_image.config import *                               # 导入相关配置


def imagesget():
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    count = 0
    while True:
        img = requests.get(download_url).content                    # 从相关网址下载验证码
        with open('{0}/{1}.jpeg'.format(images_path, count), 'wb') as imgfile:
            imgfile.write(img)
        count += 1
        if count == download_count:
            break


def convert_image(image, n):
    if not os.path.exists(black_white_path):
        os.mkdir(black_white_path)
    image = image.convert('L')                                      # 灰度
    image2 = Image.new('L', image.size, 255)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = image.getpixel((x, y))
            if pixel < gray_value:                                   # 灰度低于134 设置为 0
                image2.putpixel((x, y), 0)
    image2.save('{0}/{1}'.format(black_white_path, n))               # 将灰度图存储下来看效果
    return image2


def cut_img(file_path):
    name = re.findall('\d+', file_path)[0]
    if not os.path.exists(name):
        os.mkdir(name)
    img = Image.open(file_path)
    w = image_w                                                     # 设置切割图片的宽度
    h = image_h                                                     # 设置切割图片的高度
    region = img.crop((offset_x, offset_y, offset_x + w, offset_y + h))
    region1 = img.crop((offset_x + w, offset_y, 2 * w + offset_x, offset_y + h))
    region2 = img.crop((2 * w + offset_x, offset_y, 3 * w + offset_x, offset_y + h))
    region3 = img.crop((3 * w + offset_x, offset_y, 4 * w + offset_x, offset_y + h))
    region.save('./{0}/{1}_1st.png'.format(name, name))
    region1.save('./{0}/{1}_2st.png'.format(name, name))
    region2.save('./{0}/{1}_3st.png'.format(name, name))
    region3.save('./{0}/{1}_4st.png'.format(name, name))


def pix(im, w, h, n):
    if not os.path.exists(denoising_path):
        os.mkdir(denoising_path)
    data = im
    # 图片的长宽
    w = w
    h = h
    for x in range(w):
        if x == 0:                                                     # 去除左边界的噪点
            right = x + 1
            for y in range(0, h):
                if y == 0:
                    down = y + 1
                    right_color = data.getpixel((right, y))
                    down_color = data.getpixel((x, down))
                    right_down_color = data.getpixel((right, down))
                    item_list = [right_color, down_color, right_down_color]
                    count = count_black(item_list)
                    if count <= max_black_count:
                        data.putpixel((x, y), 255)
                elif y == h - 1:
                    up = y - 1
                    up_color = data.getpixel((x, up))
                    right_color = data.getpixel((right, y))
                    right_up_color = data.getpixel((right, up))
                    item_list = [up_color, right_color, right_up_color]
                    count = count_black(item_list)
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
                    count = count_black(item_list)
                    if count <= max_black_count:
                        data.putpixel((x, y), 255)
        if x == w - 1:                                                    # 去除右边界的噪点
            left = x - 1
            for y in range(0, h):
                if y == 0:
                    down = 1
                    left_color = data.getpixel((left, y))
                    left_down_color = data.getpixel((left, down))
                    down_color = data.getpixel((x, down))
                    if data.getpixel((x, y)) == 0:
                        item_list = [left_color, left_down_color, down_color]
                        count = count_black(item_list)
                        if count <= max_black_count:
                            data.putpixel((x, y), 255)
                elif y == h-1:
                    if data.getpixel((x, y)) == 0:
                        up = y-1
                        up_color = data.getpixel((x, up))
                        left_color = data.getpixel((left, y))
                        left_up_color = data.getpixel((left, up))
                        if data.getpixel((x, y)) == 0:
                            item_list = [left_color, left_up_color, up_color]
                            count = count_black(item_list)
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
                        count = count_black(item_list)
                        if count <= max_black_count:
                            data.putpixel((x, y), 255)
        if 0 < x < w-1:
            # 获取目标像素点左右位置
            left = x - 1
            right = x + 1
            for y in range(h):
                if y == 0:                                               # 去除上边界的噪点
                    down = y + 1
                    down_color = data.getpixel((x, down))
                    left_color = data.getpixel((left, y))
                    left_down_color = data.getpixel((left, down))
                    right_color = data.getpixel((right, y))
                    right_down_color = data.getpixel((right, down))
                    item_list = [right_color, down_color, left_color, left_down_color, right_down_color]
                    count = count_black(item_list)
                    print(n, count)
                    if count <= max_black_count:
                        data.putpixel((x, y), 255)
                elif y == h-1:                                               # 去除下边界的噪点
                    if data.getpixel((x, y)) == 0:
                        try:
                            up = y - 1
                            up_color = data.getpixel((x, up))
                            left_color = data.getpixel((left, y))
                            left_up_color = data.getpixel((left, up))
                            right_color = data.getpixel((right, y))
                            right_up_color = data.getpixel((right, up))
                            item_list = [up_color, right_up_color, left_color, right_color, left_up_color]
                            count = count_black(item_list)
                            if count <= max_black_count:
                                data.putpixel((x, y), 255)
                        except Exception as e:
                            pass
                else:
                    if data.getpixel((x, y)) == 0:                            # 去除中心区域的噪点
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
                            item_list = [up_color, down_color, left_color, left_down_color, left_up_color, right_color,
                                         right_up_color, right_down_color]
                            count = count_black(item_list)
                            if count <= max_black_count:
                                data.putpixel((x, y), 255)
                        except Exception:
                            pass
                        else:
                            pass
    file_name = n.split('/')[2]
    data.save("{0}/{1}".format(denoising_path, file_name), "png")   # 保存图片


def count_black(item_list):
    count_dict = Counter(item_list)
    count = count_dict[0]
    return count


def buildvector(image):
    result = {}
    count = 0
    for i in image.getdata():
        result[count] = i
        count += 1
    return result


def ergodic(file_name):
    file_list = os.listdir(file_name)
    return file_list


def together_path(i):
    all_file_path = []
    for i in range(i):
        file_list = os.listdir('./{0}'.format(i))
        for j in file_list:
            file_path = './{0}/{1}'.format(i, j)
            all_file_path.append(file_path)
    return all_file_path


def main():

    imagesget()
    file_list = ergodic(images_path)
    print(file_list)
    for file in file_list:
        img = Image.open('{0}/{1}'.format(images_path, file))
        file = file.replace('jpeg', 'png')
        convert_image(img, file)

    file_list1 = ergodic(black_white_path)
    print(file_list1)                                       # 打印相关路径
    for file in file_list1:
        cut_img('{0}/{1}'.format(black_white_path, file))

    file_path = together_path(download_count)
    for i in file_path:
        img = Image.open(i)
        pix(img, image_w, image_h, i)


if __name__ == '__main__':
    main()
