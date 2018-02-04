环境:win10+python3.5+tensorflow1.5.0

测试使用数据为上升型的sin函数，数据文件在data文件夹下

predict_result.png是模型训练1000次的结果
# observed曲线是原数据曲线
# evaluated曲线是拟合曲线
# predicted曲线是预测曲线

使用pre.py中的train_and_predict(csv_file_name, model_save_dir, training_steps, predicted_steps)函数就可以进行预测
# csv_file_name是数据文件名，model_save_sir是训练模型保存的暂时目录
# training_steps是训练次数(训练数据量的2-4倍)，predicted_steps是向后预测的数据数目
# 数据曲线图像将会保存在model_save_dir/predict_result.png
# 运行后还会打印出预测的时间点和对应的值

train_and_predict()会返回两个参数，predicted_times, predicted
# predicted_times存储时间点，predicted存储时间点对应的预测数据

