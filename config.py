#-*- coding:utf-8 -*


#原始路径
path = 'C:/Users/Administrator/PycharmProjects/NeuralNetwork/captcha_test'
#训练集原始验证码文件存放路径
captcha_path = path + '/captcha_soc/captcha'
#训练集验证码清理存放路径
captcha__clean_path = path + '/captcha_soc/captcha_clean'
#训练集存放路径
train_data_path = path + '/captcha_soc/training_data'
#模型存放路径
model_path = path + '/captcha_soc/model/model.model'
#测试集原始验证码文件存放路径
test_data_path = path + '/captcha_soc/test_data'
#测试结果存放路径
output_path = path + '/captcha_soc/result/result.txt'

#识别的验证码个数
image_character_num = 4

#图像粗处理的灰度阈值
threshold_grey = 100

#标准化的图像大小
image_width = 8
image_height = 26

