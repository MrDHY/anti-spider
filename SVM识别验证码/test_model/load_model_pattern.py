import os
import warnings
from PIL import Image
import numpy as np
from sklearn.externals import joblib
from test_model.config import *


def tes1t1_data(file_path):
    img = Image.open(file_path)
    data = img.getdata()
    data = np.matrix(data) / 255
    data1 = data.tolist()
    data2 = []
    for i in data1:
        data2.extend(i)
    return [data2]


def together_path(dir_list):           # 遍历一个文件夹的所有函数
    all_file_path = []
    for i in dir_list:
        file_list = os.listdir('./{0}'.format(i))
        for j in file_list:
            file_path = '{0}/{1}'.format(i, j)
            all_file_path.append(file_path)
    return all_file_path

def reconginize_img(img_path):
    warnings.filterwarnings("ignore")
    m = tes1t1_data(img_path)
    svc_3 = joblib.load(model_path_3)
    a = svc_3.predict(m)
    print(a)


if __name__ == '__main__':
    img_path_list = together_path(img_path)
    for file_path in img_path_list:
        reconginize_img(file_path)
