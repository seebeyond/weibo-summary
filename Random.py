#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:youxinyu
# Github:yogayu
# Choice a Random Sentence as the summary
import json
import random
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print "reading topics from topicList"
with open('topicList.txt') as f:
    content = f.readlines()
    for topic in content:
        topic_name = topic.rstrip()
        print "\n话题:"
        print topic_name
        train_set = []
        with open('weiboData/'+topic.rstrip()+'.txt') as data:
            # with open('weiboData/'+'#北京电影学院性侵案#'+'.txt') as data:
            for tweet in data.readlines():
                train_set.append(tweet)
        # print json.dumps(train_set,encoding='UTF-8',ensure_ascii=False)
        # 将结果存入文件
        sFilePath = 'resultData/Random'
        output_file = ""
        if not os.path.exists(sFilePath):
            os.mkdir(sFilePath)
        out = open(sFilePath + '/' + topic_name + '-'+'Random'+'.txt', 'w+')

        for i in xrange(0,5):
            random_num = random.randint(0, len(train_set)-1)
            print train_set[random_num]
            output_file = output_file + train_set[random_num]

        out.write(output_file)
        out.close()
