#-*- coding:utf-8 -*


import os
from PIL import Image
from captcha_ml import image_training
import configparser
from captcha_ml.config import *


#全局变量
# config = configparser.ConfigParser()
# config.read("./config.ini")
# train_data_path = config.get("global", "train_data_path") #训练集存放路径
# image_character_num = int(config.get("global", "image_character_num")) #识别的验证码个数
# image_width = int(config.get("global", "image_width")) #标准化的图像宽度（像素）
# image_height = int(config.get("global", "image_height")) #标准化的图像高度（像素）



def read_train_data():
    """
    读取训练集文件夹下的单字母/数字图像文件
    :return:image_array, image_label:图像list、图像label list
    """
    image_array = []
    image_label = []
    for label in os.listdir(train_data_path):#获取目录下的所有文件
        label_path = train_data_path + '/' + label
        for image_path in os.listdir(label_path):
            image = Image.open(label_path + '/' + image_path)
            image_array.append(image)
            image_label.append(label)
    return image_array, image_label



#feature generated
def feature_transfer(image):
    """
    生成特征矩阵
    计算每副图像的行和、列和，共image_width + image_height个特征
    :param image:图像list
    :return:
    """
    image = image.resize((image_width, image_height)) #标准化图像格式

    feature = []#计算特征
    for x in range(image_width):#计算行特征
        feature_width = 0
        for y in range(image_height):
            if image.getpixel((x, y)) == 0:
                feature_width += 1
        feature.append(feature_width)

    for y in range(image_height): #计算列特征
        feature_height = 0
        for x in range(image_width):
            if image.getpixel((x, y)) == 0:
                feature_height += 1
        feature.append(feature_height)
    # print('feature length :',len(feature))
    return feature


def main():
    image_array, image_label = read_train_data()
    image_feature = []
    for num, image in enumerate(image_array):
        feature = feature_transfer(image)
        # print('label: ',image_label[num])
        # print(feature)
        image_feature.append(feature)
    return image_feature, image_label


if __name__ == '__main__':
    main()
