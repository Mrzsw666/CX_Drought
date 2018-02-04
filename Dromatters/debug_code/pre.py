from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf

from tensorflow.contrib.timeseries.python.timeseries import estimators as ts_estimators
from tensorflow.contrib.timeseries.python.timeseries import model as ts_model

import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt

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

    def initialize_graph(self, input_statistics):
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
        return (new_state_tuple, predictions)

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


def train_and_predict(csv_file_name, model_save_dir, training_steps, predicted_steps):
    # 显示训练信息
    tf.logging.set_verbosity(tf.logging.INFO)

    # 读取数据文件
    reader = tf.contrib.timeseries.CSVReader(csv_file_name)

    # 训练参数设置
    train_input_fn = tf.contrib.timeseries.RandomWindowInputFn(
        reader, batch_size=4, window_size=200)
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

    # 预测数据存储在predicted中，predicted_times代表时间点，predicted中包含时间点对应的预测数据
    return predicted_times, predicted


# csv_file_name是数据文件名，model_save_sir是训练模型保存的暂时目录
# training_steps是训练次数(训练数据量的2-4倍)，predicted_steps是向后预测的数据数目
# 数据曲线图像将会保存在model_save_dir/predict_result.png
# 运行后还会打印出预测的时间点和对应的值
print(train_and_predict(csv_file_name='./data/dataset.csv', model_save_dir='model1/', training_steps=1000,
                        predicted_steps=240))
