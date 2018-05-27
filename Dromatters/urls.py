"""Dromatters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from django.conf.urls import url
from django.contrib import admin
from drought.models import RF, Realtime
from django.conf import settings
from drought import views

import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.contrib.timeseries.python.timeseries import estimators as ts_estimators
from tensorflow.contrib.timeseries.python.timeseries import model as ts_model

import urllib
import urllib.request
import chardet
import re
import requests
import csv
import os
import sys
from threading import Timer
from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
import xlrd

apipatterns = [
    url(r'^AllData/$', views.AllData.as_view()),
    url(r'^RegionData/$', views.RegionData.as_view()),
    url(r'^TQ/$', views.TQ.as_view()),
    url(r'^GetForcast/$', views.GetForcast.as_view()),
]

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=r'base/')),
    url(r'^base/$', TemplateView.as_view(template_name="base.html")),
    url(r'^region/$', TemplateView.as_view(template_name="region.html")),
    url(r'^knowledge/$', TemplateView.as_view(template_name="knowledge.html")),
    url(r'^table/$', TemplateView.as_view(template_name="table.html")),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += format_suffix_patterns(apipatterns)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

CITYS_CNS = {u'北京': "bjave", u'上海': "shave", u'广州': "gzave"}


def get_pic():
    page = urllib.request.urlopen("http://www.cwb.gov.tw/V7/observe/satellite/Sat_EA.htm#")
    html = page.read()
    encode_type = chardet.detect(html)
    html = html.decode(encode_type['encoding'])
    reg = r's1p/(.*?)\" />'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    for link in imglist:
        html_url = 'http://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/' + str(link)
        fatherPath = os.getcwd()
        abspath = os.path.abspath(fatherPath)
        filename = os.path.basename(html_url)
        urllib.request.urlretrieve(html_url, abspath + "/static/css/images/cloudp.jpg")


pre_data = {'Beijing', 'Guangzhou', 'Shanghai'}
CITY_CN = {u'Beijing': "北京", u'Guangzhou': "广州", u'Shanghai': "上海"}


def get_info():
    data = xlrd.open_workbook("./static/datasheet.xlsx")
    table = data.sheet_by_index(0)
    qset = RF.objects.all()
    max_year = 0
    max_month = 0
    #if qset.count() == 441:
        #print("finish")
        #return
    qset.delete()
    for i in range(0, 3):
        cn = table.cell_value(i, 0)
        for j in range(1, 13):
            ave = float(table.cell_value(i, j))
            obj = RF.objects.create(cityName=CITYS_CNS[cn], month=j, rainfall=ave)
            obj.save()
    for i in range(3, table.nrows):
        cityname = table.cell_value(i, 0)
        year = int(table.cell_value(i, 1))
        max_year = max(max_year, year)
        month = int(table.cell_value(i, 2))
        max_month = max(max_month, month)
        rainfall = float(table.cell_value(i, 3))
        obj = RF.objects.create(cityName=cityname, year=year, month=month, rainfall=rainfall)
        obj.save()
    for ci in pre_data:
        loc = 'Dromatters/pre_data/' + ci + '.txt'
        f = open(loc)
        i = 1
        while i <= 3:
            d = f.readline()
            cityname = CITY_CN[ci]
            year = 2018
            month = 5 + i
            rainfall = float(d)
            obj = RF.objects.create(cityName=cityname, year=year, month=month, rainfall=rainfall)
            obj.save()
            i += 1
    makelevel()


def makelevel():
    for i, j in CITYS_CNS.items():
        obj = RF.objects.filter(cityName=i)
        for o in obj:
            m = o.month
            ob = RF.objects.get(cityName=j, month=m)
            ave = ob.rainfall
            rf = o.rainfall
            temp = (rf - ave) / ave
            if temp > -0.15:
                o.level = "无旱"
            elif temp > -0.3:
                o.level = "轻旱"
            elif temp > -0.4:
                o.level = "中旱"
            elif temp > -0.45:
                o.level = "重旱"
            else:
                o.level = "特旱"
            o.save()
    print("finish!")


he_key = "9dc4601daea4464d8ff6ab5d2868c81d"
CITYS_ID = {u'Beijing': u'北京', u'Shanghai': u'上海', u'Guangzhou': u'广州'}


def tq():
    cnt = 0
    he_str = "https://free-api.heweather.com/s6/weather/forecast"
    for city_str in CITYS_ID:
        payload = {'location': CITYS_ID[city_str], 'key': he_key}
        r = requests.get(he_str, params=payload)
        J = r.json()
        J = J[u"HeWeather6"][0]
        qset = Realtime.objects.filter(cityName=CITYS_ID[city_str])
        if qset:
            qset.delete()
        now = Realtime(cityName=CITYS_ID[city_str])
        Jnow = J[u"daily_forecast"][0]
        now.tmp_max = int(Jnow[u"tmp_max"])
        now.tmp_min = int(Jnow[u"tmp_min"])
        now.cond_txt_d = Jnow[u"cond_txt_d"]
        now.cond_txt_n = Jnow[u"cond_txt_n"]
        now.save()
        # print(cnt, flag)
    Timer(1200, tq).start()


# 基于RNN的LSTM结构定义
class _LSTMModel(ts_model.SequentialTimeSeriesModel):
    def __init__(self, num_units, num_features, dtype=tf.float32):
        super(_LSTMModel, self).__init__(
            train_output_names=["mean"],
            predict_output_names=["mean"],
            num_features=num_features,
            dtype=dtype)
        self._num_units = num_units
        self._lstm_cell = None
        self._lstm_cell_run = None
        self._predict_from_lstm_output = None

    def initialize_graph(self, input_statistics=None):
        super(_LSTMModel, self).initialize_graph(input_statistics=input_statistics)
        self._lstm_cell = tf.nn.rnn_cell.LSTMCell(num_units=self._num_units)
        self._lstm_cell_run = tf.make_template(
            name_="lstm_cell",
            func_=self._lstm_cell,
            create_scope_now_=True)
        self._predict_from_lstm_output = tf.make_template(
            name_="predict_from_lstm_output",
            func_=lambda inputs: tf.layers.dense(inputs=inputs, units=self.num_features),
            create_scope_now_=True)

    def get_start_state(self):
        return (
            tf.zeros([], dtype=tf.int64),
            tf.zeros([self.num_features], dtype=self.dtype),
            [tf.squeeze(state_element, axis=0)
             for state_element
             in self._lstm_cell.zero_state(batch_size=1, dtype=self.dtype)])

    def _transform(self, data):
        mean, variance = self._input_statistics.overall_feature_moments
        return (data - mean) / variance

    def _de_transform(self, data):
        mean, variance = self._input_statistics.overall_feature_moments
        return data * variance + mean

    def _filtering_step(self, current_times, current_values, state, predictions):
        state_from_time, prediction, lstm_state = state
        with tf.control_dependencies(
                [tf.assert_equal(current_times, state_from_time)]):
            transformed_values = self._transform(current_values)
            predictions["loss"] = tf.reduce_mean(
                (prediction - transformed_values) ** 2, axis=-1)
            new_state_tuple = (current_times, transformed_values, lstm_state)
        return new_state_tuple, predictions

    def _prediction_step(self, current_times, state):
        _, previous_observation_or_prediction, lstm_state = state
        lstm_output, new_lstm_state = self._lstm_cell_run(
            inputs=previous_observation_or_prediction, state=lstm_state)
        next_prediction = self._predict_from_lstm_output(lstm_output)
        new_state_tuple = (current_times, next_prediction, new_lstm_state)
        return new_state_tuple, {"mean": self._de_transform(next_prediction)}

    def _imputation_step(self, current_times, state):
        return state

    def _exogenous_input_step(
            self, current_times, current_exogenous_regressors, state):
        raise NotImplementedError(
            "Exogenous inputs are not implemented for this example.")


# LSTM预测函数（神经网络模型预测）
def lstm_predict(csv_file_name, model_save_dir, city_name, training_steps=300, predicted_steps=3, batch_size=1,
                 window_size=132):
    # 显示训练信息
    tf.logging.set_verbosity(tf.logging.INFO)

    # 读取数据文件
    reader = tf.contrib.timeseries.CSVReader(csv_file_name)

    # 训练参数设置
    train_input_fn = tf.contrib.timeseries.RandomWindowInputFn(
        reader, batch_size=batch_size, window_size=window_size)
    estimator = ts_estimators.TimeSeriesRegressor(
        model=_LSTMModel(num_features=1, num_units=128),
        optimizer=tf.train.AdamOptimizer(0.001), model_dir=model_save_dir)

    # 训练开始，训练training_steps次
    estimator.train(input_fn=train_input_fn, steps=training_steps)

    # 模型拟合
    evaluation_input_fn = tf.contrib.timeseries.WholeDatasetInputFn(reader)
    evaluation = estimator.evaluate(input_fn=evaluation_input_fn, steps=1)

    # 预测开始，向后预测predicted_steps个数据
    (predictions,) = tuple(estimator.predict(
        input_fn=tf.contrib.timeseries.predict_continuation_input_fn(
            evaluation, steps=predicted_steps)))

    # 原数据
    observed_times = evaluation["times"][0]
    observed = evaluation["observed"][0, :, :]

    # 模型拟合数据
    evaluated_times = evaluation["times"][0]
    evaluated = evaluation["mean"][0]

    # 向后预测数据
    predicted_times = predictions['times']
    predicted = predictions["mean"]

    # 画图观察
    plt.figure(figsize=(15, 5))
    observed_lines = plt.plot(observed_times, observed, label="observed", color="k")  # 原数据曲线
    evaluated_lines = plt.plot(evaluated_times, evaluated, label="evaluated", color="g")  # 模型拟合曲线
    predicted_lines = plt.plot(predicted_times, predicted, label="predicted", color="r")  # 预测结果曲线
    plt.legend(handles=[observed_lines[0], evaluated_lines[0], predicted_lines[0]],
               loc="upper left")
    plt.savefig(model_save_dir + 'predict_result.png')  # 图保存在对应模型目录下
    # plt.show()

    # 预测数据存储在predicted中，predicted_times代表时间点，predicted中包含时间点对应的预测数据
    # return predicted_times, predicted

    pre_data = predicted
    i = 0
    pre_dir = 'Dromatters/pre_data/' + city_name + '.txt'
    while i < 3:
        if pre_data[i] < 0:
            pre_data[i] += 30
        with open(pre_dir, 'a') as f:
            f.write(str(round(pre_data[i][0], 1)) + '\n')
        i += 1


# AR预测函数（自回归模型预测）
def ar_predict(csv_file_name, model_save_dir, city_name, training_steps=300, predicted_steps=3, batch_size=16,
               window_size=12):
    # 显示训练信息
    tf.logging.set_verbosity(tf.logging.INFO)

    # 读取数据
    reader = tf.contrib.timeseries.CSVReader(csv_file_name)
    train_input_fn = tf.contrib.timeseries.RandomWindowInputFn(reader, batch_size=batch_size, window_size=window_size)
    with tf.Session() as sess:
        data = reader.read_full()
        coord = tf.train.Coordinator()
        tf.train.start_queue_runners(sess=sess, coord=coord)
        data = sess.run(data)
        coord.request_stop()

    # 参数设置
    ar = tf.contrib.timeseries.ARRegressor(
        periodicities=132, input_window_size=9, output_window_size=3,
        num_features=1,
        loss=tf.contrib.timeseries.ARModel.NORMAL_LIKELIHOOD_LOSS,
        model_dir=model_save_dir)

    # 训练
    ar.train(input_fn=train_input_fn, steps=training_steps)

    # 拟合
    evaluation_input_fn = tf.contrib.timeseries.WholeDatasetInputFn(reader)
    evaluation = ar.evaluate(input_fn=evaluation_input_fn, steps=1)

    # 预测
    (predictions,) = tuple(ar.predict(
        input_fn=tf.contrib.timeseries.predict_continuation_input_fn(
            evaluation, steps=predicted_steps)))

    predicted_times = predictions['times'].reshape(-1)
    predicted = predictions['mean'].reshape(-1)

    # 画图显示
    plt.figure(figsize=(15, 5))
    plt.plot(data['times'].reshape(-1), data['values'].reshape(-1), label='origin')
    plt.plot(evaluation['times'].reshape(-1), evaluation['mean'].reshape(-1), label='evaluation')
    plt.plot(predictions['times'].reshape(-1), predictions['mean'].reshape(-1), label='prediction')
    plt.xlabel('time_step')
    plt.ylabel('values')
    plt.legend(loc="upper left")
    plt.savefig(model_save_dir + 'predict_result.png')  # 图保存在对应模型目录下
    # plt.show()

    # 预测数据存储在predicted中，predicted_times代表时间点，predicted中包含时间点对应的预测数据
    # return predicted_times, predicted

    pre_data = predicted
    i = 0
    pre_dir = 'Dromatters/pre_data/' + city_name + '.txt'
    while i < 3:
        if pre_data[i] < 0:
            pre_data[i] += 30
        with open(pre_dir, 'a') as f:
            f.write(str(round(pre_data[i][0], 1)) + '\n')
        i += 1


def train_and_pre():
    # csv_file_name是数据文件名，model_save_sir是训练模型保存的暂时目录
    lstm_predict(csv_file_name='Dromatters/source_data/dataset_1.csv', model_save_dir='Dromatters/model1/',
                 city_name='Beijing')
    lstm_predict(csv_file_name='Dromatters/source_data/dataset_2.csv', model_save_dir='Dromatters/model2/',
                 city_name='Shanghai')
    lstm_predict(csv_file_name='Dromatters/source_data/dataset_3.csv', model_save_dir='Dromatters/model3/',
                 city_name='Guangzhou')


def go():
    o = sys.argv
    if o[1] == "runserver":
        Timer(0, get_info).start()
        Timer(0, get_pic).start()
        Timer(0, tq).start()

Timer(0, go).start()
