
f = open("mini_classes.txt","r")
classes = f.readlines()
f.close()
classes = [c.replace('\n','').replace(' ','_') for c in classes]

import urllib.request
def download():
    base = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'
    for c in classes:
        cls_url = c.replace('_', '%20')
        path = base + cls_url + '.npy'
        print(path)
        urllib.request.urlretrieve(path, 'data/' + c + '.npy')
download()


def load_data(root, vfold_ratio=0.2, max_items_per_class=5000):
    # 20%用作验证数据集
    all_files = glob.glob(os.path.join(root, '*.npy'))
    # 读取data目录下所有后缀为.npy的文件的路径
    # initialize variables
    x = np.empty([0, 784])
    # 784=28*28
    y = np.empty([0])
    class_names = []

    # 导入文件
    for idx, file in enumerate(all_files):
        data = np.load(file)
        data = data[0: max_items_per_class, :]
        labels = np.full(data.shape[0], idx)

        x = np.concatenate((x, data), axis=0)
        y = np.append(y, labels)

        class_name, ext = os.path.splitext(os.path.basename(file))
        class_names.append(class_name)

    data = None
    labels = None

    # 数据集随机离散化
    permutation = np.random.permutation(y.shape[0])
    x = x[permutation, :]
    y = y[permutation]

    # 将训练集和测试集分开
    vfold_size = int(x.shape[0] / 100 * (vfold_ratio * 100))

    x_test = x[0:vfold_size, :]
    y_test = y[0:vfold_size]

    x_train = x[vfold_size:x.shape[0], :]
    y_train = y[vfold_size:y.shape[0]]
    return x_train, y_train, x_test, y_test, class_names


model = Sequential()
#Conv1层输入（28，28，1）输出（24，24，96）使用步长1来减少输出的宽和高，卷积核的数目比lenet大得多
model.add(Conv2D(96,(5,5),strides=(1,1),input_shape=x_train.shape[1:],padding='valid',activation='relu',kernel_initializer='uniform'))
#Pooling1层，输出（11，11，96）
model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
#Conv2层，，输出（11，11，256）filter的数目为256，增加通道数目
model.add(BatchNormalization())#归一化层

model.add(Conv2D(256,(4,4),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
#Pooling2层，输出（5，5，256）
model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
model.add(BatchNormalization())

#连续三个卷积层，前两个卷积层不使用池化层减少宽和高，使用更小的卷积窗口，增加更多的卷积核数目，输出（5，5，384）
model.add(Conv2D(384,(3,3),padding='same',activation='relu',kernel_initializer='uniform'))
model.add(BatchNormalization())

model.add(Conv2D(384,(3,3),padding='same',activation='relu',kernel_initializer='uniform'))
model.add(BatchNormalization())

#输出（5，5，256）
model.add(Conv2D(256,(3,3),padding='same',activation='relu',kernel_initializer='uniform'))
#最后一个Pooling层，减少输出的宽和高（输出2，2，256）
model.add(MaxPooling2D(pool_size=(3,3),strides=(2,2)))
model.add(BatchNormalization())

#将多维输入一维化之后接FC
model.add(Flatten())
# 这里全连接层的输出个数比 LeNet 中的大数倍。使用丢弃层来缓解过拟合
model.add(Dense(4096,activation='relu'))
#Dropout将在训练过程中每次更新参数时按一定概率随机断开输入神经元
model.add(Dropout(0.5))
model.add(BatchNormalization())

model.add(Dense(4096,activation='relu'))
model.add(Dropout(0.5))#使用丢弃层来缓解过拟合
model.add(BatchNormalization())

model.add(Dense(100,activation='softmax'))
adam = tf.train.AdamOptimizer() #随机梯度下降
model.compile(loss='categorical_crossentropy',optimizer=adam,metrics=['top_k_categorical_accuracy'])
#categorical_crossentropy：多类对数损失
#optimizer优化器
#metrics：列表，包含评估模型在训练和测试时的性能的指标
print(model.summary())
model.fit(x = x_train, y = y_train, validation_split=0.1, batch_size = 256, verbose=2, epochs=6)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test accuarcy: {:0.2f}%'.format(score[1] * 100))

mport matplotlib.pyplot as plt
from random import randint
%matplotlib inline
idx = randint(0, len(x_test))
img = x_test[idx]
plt.imshow(img.squeeze())
pred = model.predict(np.expand_dims(img, axis=0))[0]
ind = (-pred).argsort()[:5]
latex = [class_names[x] for x in ind]
print(latex)