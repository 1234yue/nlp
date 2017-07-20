print 'hello world'
import tensorflow as tf
import os
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
print os.path.abspath('.')
if __name__=='__main__':
    print 'hello'