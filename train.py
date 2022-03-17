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
#print(1)
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

test=[[[812, 861, 4.985762984688336e-07], [691, 832, -0.03883993998169899], [612, 753, -0.06349804997444153], [557, 679, -0.08375724405050278], [492, 626, -0.10491574555635452], [709, 595, -0.05149902030825615], [708, 461, -0.0817883089184761], [712, 377, -0.10449948161840439], [720, 304, -0.11985357105731964], [782, 585, -0.051072392612695694], [785, 437, -0.07703430950641632], [789, 341, -0.09653119742870331], [797, 257, -0.11037775129079819], [849, 601, -0.0542522631585598], [853, 466, -0.0775221660733223], [851, 381, -0.09094364941120148], [850, 308, -0.09994131326675415], [914, 635, -0.060765136033296585], [919, 533, -0.08059275150299072], [916, 465, -0.08811325579881668], [912, 402, -0.09256209433078766]]]
test=helper.preProcess(test)
print(model.predict(test))




