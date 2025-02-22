'''
This is the code ex4: 
Almost the same with ex3.
But remove the definition of the add_layer,
by using tf.dense.
'''

import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import timeit
 # batch size
batch_size = 10

### use tf.dense to replace define layer 
# # add layer ============================================
# def add_layer(inputs,in_size,out_size,activation_function = None):
#     Weights = tf.Variable(tf.random_normal([in_size,out_size]))
#     biases  = tf.Variable(tf.zeros([1,out_size]) + 0.1)       # this term is recommended not to be zero
#     Wx_plus_b = tf.matmul(inputs,Weights) + biases

#     if activation_function is None:
#         outputs = Wx_plus_b
#     else:
#         outputs = activation_function(Wx_plus_b)
#     return outputs

# # =======================================================


x_data = np.linspace(-1,1,300000)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
#y_data = np.square(x_data) - 0.5 + noise
y_data = x_data**3 - 0.5 + noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

# neural network layers  
l1 = tf.layers.dense(xs,10,tf.nn.relu) #first hidden layer
output = tf.layers.dense(l1,1)
loss = tf.losses.mean_squared_error(ys, output)

'''
indices for 0 means take mean with row direcion
and 1 means take mean with column directin.       
'''
# important step
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(loss) # learning rate 0.1 
#initialize variable first
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# ax.scatter(x_data,y_data)
# plt.ion()
# plt.show()

start = timeit.default_timer()
for i in range(1000):
    # random select batch set 
    batch_select = np.random.randint(0,len(x_data)-1,batch_size)
    # training
    sess.run(train_step, feed_dict={xs:x_data[batch_select], ys: y_data[batch_select]})
    
    if i % 50 == 0:
        #print(sess.run(loss,feed_dict={xs: x_data,ys: y_data}))

        # to visualize the result and improvement
        #==================================
        # try:
        #     ax.lines.remove(lines[0])  #lines[0] is the lines itself
        # except Exception:
        #     pass     
        #================================== old way
        plt.cla()           ##clear an axis, current active axis in the current drawing
        prediction_value = sess.run(output,feed_dict = {xs: x_data})
        loss_value=sess.run(loss,feed_dict={xs: x_data, ys: y_data})
        # plot the prediction
        ax.scatter(x_data,y_data)
        lines = ax.plot(x_data,prediction_value,'r-',lw = 5)
        plt.text(-0.50,0, 'Loss =%.4f'%loss_value,fontdict={'size':20,'color':'green'})
        plt.pause(0.5)
stop = timeit.default_timer()
print('time elapse={0}'.format(stop-start)) 
plt.ioff()