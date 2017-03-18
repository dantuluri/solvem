from mnist import MNIST




mndata = MNIST('/Users/surya/Downloads')
training_images, training_labels = mndata.load_training()
testing_images, testing_labels   = mndata.load_testing()


NUM_CLASSES = 15

def to_one_hot(x):
    x_ = [0]*NUM_CLASSES
    x_[x] = 1
    return x_

testing_labels = map(to_one_hot, testing_labels)
training_labels = map(to_one_hot, training_labels)

print(len(testing_labels), len(testing_labels[0]))

import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 15]))
b = tf.Variable(tf.zeros([15]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 15])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()


batch_xs, batch_ys = training_images[:1000], training_labels[:1000]
# for i in range(1000):
#   #batch_xs, batch_ys = mnist.train.next_batch(100)
#   batch_xs = training_images[(100*i)%59900:((100*i)%59900 ) +100 ]
#   batch_ys = training_labels[(100*i)%59900:((100*i)%59900 ) +100 ]
#
#   #print(len(batch_ys), len(batch_ys[0]))
sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#  if i % 100 == 0:
#    print('Accuracy', accuracy)
print(sess.run(accuracy, feed_dict={x: testing_images, y_: testing_labels}))


print("Weights", b)

# cPickle
load
dump


# Upload (raw data)
# filename = uuid.uuid4().hex + '.png'
# open( filename):
#    write ....

# import tensorflwo,
#   data = scipy.misc.imread(filename) 100*200
# y = tf.multiply(W, data) + b
# [.45,.0,0.1,.999,]
# return max(enum( [.45,.0,0.1,.999,etc]))


# trainin phase  /data/random1.png, /data/random2.png, etc,...
#
