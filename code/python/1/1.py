# -*- coding:utf-8 -*-
"""
@Time:2018/8/15 9:35
@Author:yuhongchao
"""
import tensorflow as tf
# 预定义两个占位符，一般都是32float
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

y = tf.add(a, b)

sess = tf.Session()

print(sess.run(y, feed_dict={a:3, b:3}))

sess.close()
