# 使用SVM破解验证码

### 破解验证码的思维导图:
![image](http://upload-images.jianshu.io/upload_images/9552963-a4b04048bd50f9f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

### 模块解释
```
gen_train_img文件夹是用来生成训练数据集的
```

```
train_and_get_model文件夹是用来训练和生成验证码需要的模型的，此过程全部在jupyter中进行
```
```
test_model是用来测试模型的正确度
```
```
captcha_recongnize是用来识别验证码的
```
### 这四个模块的运行方式
```
gen_train_image可直接运行python last_img.py,相关的配置参数，已经在config里说明，可以修改
```
```
train_and_get_model可打开:支持向量机验证码.ipynb，这个文件，该文件的打开需要安装anaconda[，](https://www.anaconda.com/download/),anaconda自带jyputer notebook
打开文件后可查看相关信息，代码中都有注释。
```
```
test_model打开load_model_pattern.py，运行即可。模型的路径和要验证的图片可以在config中配置
```
### captcha_recongnize模块
```
运行方式，运行recongnize.py，只需要输入验证码的路径即可识别。
```