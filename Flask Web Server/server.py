# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

import datetime
import tensorflow as tf
import numpy as np
import pandas as pd

app = Flask(__name__)

from tensorflow import keras
from tensorflow.keras import layers


# 모델 placeholder를 선언합니다.
def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[4]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.legacy.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

# 저장된 모델을 불러오는 객체를 선언합니다.
# saver = tf.train.Saver()
# model = tf.global_variables_initializer()
model = build_model()

# 세션 객체를 생성합니다.
# sess = tf.Session()
# sess.run(model)

# 저장된 모델을 세션에 적용합니다.
# save_path = "./model/saved.cpkt"
# saver.restore(sess, save_path)
checkpoint_path = "training_1/cp.ckpt"
model.load_weights(checkpoint_path)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # 파라미터를 전달 받습니다.
        avg_temp = float(request.form['avg_temp'])
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

        # 배추 가격 변수를 선언합니다.
        price = 0

        # 입력된 파라미터를 배열 형태로 준비합니다.
        # data = ((avg_temp, min_temp, max_temp, rain_fall), (0, 0, 0, 0))
        # arr = np.array(data, dtype=np.float32)
        arr = pd.DataFrame([[avg_temp, min_temp, max_temp, rain_fall]])
        x_data = arr[0:4]

        # 입력 값을 토대로 예측 값을 찾아냅니다.
        # x_data = arr[0:4]
        # dict = sess.run(hypothesis, feed_dict={X: x_data})
        dict = model.predict(x_data).flatten()
            
        # 결과 배추 가격을 저장합니다.
        price = dict[0]

        return render_template('index.html', price=price)

if __name__ == '__main__':
   app.run(debug = True)