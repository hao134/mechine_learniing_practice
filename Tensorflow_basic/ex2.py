import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf 


matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1,matrix2) # matrix multiply equal to np.dot(m1,m2)

# # method 1 
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()

# method 2 
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
