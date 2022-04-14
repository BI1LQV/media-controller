import tensorflow as tf
import numpy as np
import json
import helper
y = []

a = helper.preProcess(json.loads(open('./datas/a.txt', 'r').read()))
b = helper.preProcess(json.loads(open('./datas/b.txt', 'r').read()))

data = a+b

for i in range(len(a)):
    y.append(tf.one_hot(0, 2))
for i in range(len(b)):
    y.append(tf.one_hot(1, 2))



data = np.asarray(data)
y = np.asarray(y)


toShuffle=[]
for i in range(len(data)):
    toShuffle.append([data[i],y[i]])
import random
random.shuffle(toShuffle)
data=[p[0] for p in toShuffle]
y=[p[1] for p in toShuffle]

print(len(data))
print(len(y))

trainx=data[0:22]
trainy=y[0:22]
testx=data[22:30]
testy=y[22:30]



trainx = tf.convert_to_tensor(trainx)
trainy = tf.convert_to_tensor(trainy)
testx = tf.convert_to_tensor(testx)
testy = tf.convert_to_tensor(testy)


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(21, 3)),
    tf.keras.layers.Dense(20, activation='relu'),
    # tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(2, activation='softmax'),
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


model.fit(trainx, trainy,validation_data=(testx,testy), epochs=50)


def predictPoint(points):
    points = helper.preProcess([points])
    return helper.maxIndex(model.predict(points)[0])
