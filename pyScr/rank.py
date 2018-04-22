import tensorflow as tf

sess = tf.Session()

zeroD = tf.constant(5)
print("ZeroD:", sess.run(tf.rank(zeroD)))

oneD = tf.constant(["How", "are", "you?"])
print("oneD:", sess.run(tf.rank(oneD)))

twoD = tf.constant([[1.0, 2.3], [1.5, 2.9]])
print("twoD:", sess.run(tf.rank(twoD)))

threeD = tf.constant([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
print("threeD:", sess.run(tf.rank(threeD)))

sess.close()
