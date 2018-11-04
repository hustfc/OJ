import math
class AdaBoost:
    def __init__(self):
        self.flag = 0 #判断分类器的符号
        self.Flags = []  #存放每一个分类器的符号
    def sign(self, x):
        if x > 0:
            return 1
        if x < 0:
            return -1
        else:
            return 0
    def func(self, classifier, x, flag):  #根据阈值确定分类函数
        if flag == 0:
            if x < classifier:
                return 1
            else:
                return -1
        else:
            if x < classifier:
                return -1
            else:
                return 1
    # 基于权值判断每一个分类器的误分率
    def getErrorRate(self, label, classifier, weight):
        errorRate1, errorRate2 = 0, 0
        for i in range(int(classifier + 0.5)):
            if label[i] != 1:
                errorRate1 += weight[i]
        for i in range(int(classifier + 0.5), len(label)):
            if label[i] != -1:
                errorRate1 += weight[i]
        for i in range(int(classifier + 0.5)):
            if label[i] != -1:
                errorRate2 += weight[i]
        for i in range(int(classifier + 0.5), len(label)):
            if label[i] != 1:
                errorRate2 += weight[i]
        if errorRate1 <= errorRate2:
            return errorRate1, 0
        else:
            return errorRate2, 1
    def getClassifier(self, label, weight):
        length = len(label)
        minErrorRate, self.flag = self.getErrorRate(label, 0.5, weight)
        minClassifier = 0.5
        classifier = 1.5
        while classifier <= length - 0.5:
            errorrate, flag = self.getErrorRate(label, classifier, weight)
            if errorrate < minErrorRate:
                minErrorRate, flag = self.getErrorRate(label, classifier, weight)
                minClassifier = classifier
                self.flag = flag
            classifier += 1
        self.Flags.append(self.flag)  #存取这个分类器的flag
        return minClassifier, minErrorRate
    def getNewWeigh(self, label, classifier, weight, ratio):
        Zm = 0
        exp = [0] * len(label)
        for i in range(len(label)):#计算每一项的规范化因子
            if self.flag == 0:
                if (i < classifier and label[i] == 1) or (i > classifier and label[i] == -1):
                    yG = 1   #如果被分对，那么同号
                else:
                    yG = -1  #分错则异号
            else:
                if (i < classifier and label[i] == -1) or (i > classifier and label[i] == 1):
                    yG = 1  # 如果被分对，那么同号
                else:
                    yG = -1  # 分错则异号
            exp[i] = weight[i] * math.e ** (-1 * ratio * yG)
            Zm += exp[i]
        for i in range(len(label)):#更新每一项的权系数
            weight[i] = exp[i] / Zm
        return weight
    def Run(self, label):
        length = len(label)
        weight = [1 / length] * length  #初始化权重
        gloErrorRate = 1  #全局错误率
        Classifier = []  #保存分类器的数组
        Ratio = []       #保存权重的数组
        while gloErrorRate:
            print('第 %d 轮迭代开始' % (len(self.Flags) + 1))
            funClassifier, errorRate = self.getClassifier(label, weight)  #得到基本分类器和误差率
            if self.flag == 0:
                print('得到基本的分类器为：G(x) = 1 [x < %.1f] || G(x) = -1 [x > %.1f]，最低误分率为：%.4f' % (funClassifier, funClassifier, errorRate))
            else:
                print('得到基本的分类器为：G(x) = -1 [x < %.1f] || G(x) = 1 [x > %.1f]，最低误分率为：%.4f' % (funClassifier, funClassifier, errorRate))
            ratio = 0.5 * math.log((1 - errorRate) / errorRate, math.e)
            print('这个基本分类器的权值为：%.4f' % ratio)
            Classifier.append(funClassifier) #将分类器计入数组
            Ratio.append(ratio) #将权值计入数组
            weight = self.getNewWeigh(label, funClassifier, weight, ratio)  #计算新的权值
            print('更新权值之后，下一轮迭代的样本权值为：')
            for i, wei in enumerate(weight):
                print('%d:%.3f  ' % (i, wei), end='')
            print()
            gloErrorRate = 0
            for x in range(len(label)): #重新计算全局错误率
                gloClassifier = 0
                for i in range(len(Classifier)):
                    gloClassifier += Ratio[i] * self.func(Classifier[i], x, self.Flags[i])
                gloClassifier = self.sign(gloClassifier)
                if gloClassifier != label[x]:
                    gloErrorRate += 1
            print('经过以上几轮迭代，加权得到的强分类器的分错了 %d 个样本' % gloErrorRate)
            print('第 %d 轮迭代结束' % len(self.Flags))
            print()
label1 = [1, 1, 1, -1, -1, -1, 1, 1, 1, -1]
AdaBoost().Run(label1)
import random
length = random.randint(10, 20)
print('随机生成训练数据：')
label2 = []
for i in range(length):
    label2.append(random.randrange(-1, 3, 2))
print(label2)
AdaBoost().Run(label2)