import tensorflow as tf
import numpy as np
import json
import helper
y=[]

a=helper.preProcess(json.loads(open('./a.txt','r').read()))
b=helper.preProcess(json.loads(open('./b.txt','r').read()))
c=helper.preProcess(json.loads(open('./c.txt','r').read()))
d=helper.preProcess(json.loads(open('./d.txt','r').read()))
e=helper.preProcess(json.loads(open('./e.txt','r').read()))
f=helper.preProcess(json.loads(open('./f.txt','r').read()))

data=a+b+c+d+e+f

for i in range(len(a)):
    y.append(tf.one_hot(0,6))
for i in range(len(b)):
    y.append(tf.one_hot(1,6))
for i in range(len(c)):
    y.append(tf.one_hot(2,6))
for i in range(len(d)):
    y.append(tf.one_hot(3,6))
for i in range(len(e)):
    y.append(tf.one_hot(4,6))
for i in range(len(f)):
    y.append(tf.one_hot(5,6))


data=np.asarray(data)
y=np.asarray(y)



data=tf.convert_to_tensor(data)
y=tf.convert_to_tensor(y)





model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(21, 3)),
    tf.keras.layers.Dense(20, activation='relu'),
    #tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(6, activation='softmax'),
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


model.fit(data,y , epochs=500)

test=[[[2273, 2126, 6.155313485578517e-07], [2009, 2058, -0.029398014768958092], [1812, 1867, -0.04850389435887337], [1654, 1718, -0.065284363925457], [1494, 1627, -0.08241712301969528], [2000, 1502, -0.03165881335735321], [1994, 1211, -0.05487631633877754], [2012, 1027, -0.07390271127223969], [2039, 876, -0.08701972663402557], [2168, 1468, -0.03449943661689758], [2169, 1138, -0.05349602922797203], [2177, 918, -0.07066270709037781], [2187, 736, -0.08264367282390594], [2333, 1494, -0.04077209532260895], [2329, 1186, -0.0589146614074707], [2315, 1000, -0.07167717814445496], [2301, 842, -0.08031188696622849], [2494, 1571, -0.04972591996192932], [2521, 1339, -0.06490044295787811], [2523, 1188, -0.07081232964992523], [2515, 1049, -0.07418320327997208]]]
test=helper.preProcess(test)
print(model.predict(test))




