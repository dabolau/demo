import tensorflow as tf
import numpy as np

# 随机创建数据
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# 开始创建tensorflow结构 #
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# tf.initialize_all_variables() 已经停用，请使用 tf.global_variables_initializer()
init = tf.global_variables_initializer()
# 结速创建tensorflow结构 #

sess = tf.Session()
sess.run(init)  # 非常重要

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))
