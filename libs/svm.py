# -*- coding: utf-8 -*-

import os
import random
import chardet
import sys
import pickle
reload(sys)
sys.setdefaultencoding('utf-8')
import opt_ori_data as ood 

import numpy as np 
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
def train(file_src):
    #split the data to train and test
    dataX, dataY = ood.run_train_data() 
    trainX, testX, trainY, testY = train_test_split(dataX, dataY, test_size = 0.2, stratify = dataY)

    clf = SVC(kernel = 'linear')
    clf.fit(trainX, trainY)
    print 'mean accuracy: ' + str(clf.score(trainX, trainY))
    file_pickle = open(file_src, 'wb')
    p = pickle.dump(clf, file_pickle)
    return p

def predict(predictX, file_src):
    file_pickle = open(file_src, 'rb')
    clf = pickle.load(file_pickle)
    predictX = ood.run_predict_data(predictX)
    return clf.predict(predictX)

def predict_API(predictX):
    file_src = os.path.join(os.path.abspath('.'), 'libs\svm_model.pkl')
    result =  predict(predictX, file_src)
    print result[0]
    return result[0]

def train_API():
    file_src = os.path.join(os.path.abspath('.'), 'libs\svm_model.pkl')
    return train(file_src)

def run():
    # train_API()
    predict_API('我最近晚上失眠。有半个月了吧，睡的不好，早上也什么都不想做，特别萎靡，东西也不想吃。有时候很饿，但是就是故意让自己饿着，感觉这样我才活着。没事儿，不说了啊，累了。')
    # predict_API('哈哈哈，今天我去爬山了。还行，天还挺蓝的，很不错。好久没运动了，超级爽，开心。哎呀，没事儿也出去走走，可以像我游泳什么的。我最近刚学会了游泳，特别喜欢去，还有个新鲜劲儿呢哈哈哈。我也是哈哈哈，不过过了那个劲儿就好了，释放压力。')
    # predict_API('最近不知道怎么了，害怕洗澡，有时候会四肢僵硬地躺在床上哭，因为太害怕而无法起来洗澡，这简单的过程对我就像经历耶稣的历程一样困难。')
    # predict_API('不想见人，不想接电话，不想和人说话不想出门，哎，太痛苦了。每天从早晨一睁眼开始，我就不知道这一天怎么度过。')
    # predict_API('我感觉我进入如深渊般的社交困境，我的手脚也如同长出了绳索一般，把我彻底捆缚住了，我开始觉得我的人生彻底无望了')
    # predict_API('今天看了《感动中国》，哭得稀里哗啦，小到亲情，大到国家大义，我真的是抑制不住被那份最真实的感情感动。')
    # predict_API('今天去打了球，神清气爽，碰到了一个对手，还是挺佩服的。又去图书馆读了书，觉得非常不错。对于每天都充满希望，每天都过得非常幸福。希望未来自己也能成为一个了不起的人。')
    # predict_API('本人是一名大一学生，大一的生活一直处于浑浑噩噩的状态，直到我看到了《杜拉拉升职记》。它让我开始重新审视自己的生活，开始规划自己的未来，在今后，我希望我能向拉拉一样所向无敌。人际关系的交际技巧，与上司下属的巧妙沟通，善于利用学习机会，每一次的金玉良言，我想说，杜拉拉不仅仅给在职的白领以启迪，她势必将改变我的生活。')

if __name__ == '__main__':
    run()

