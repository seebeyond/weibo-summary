#! /usr/bin/env python
# -*- coding: utf-8 -*-
#author:youxinyu
#github:yogayu

import re
import os
import sys
import xml.etree.ElementTree as ET

#设置编码格式
reload(sys)
sys.setdefaultencoding('utf-8')

# path = "/Users/apple/weibo/topic/social/1motherDay" #文件夹目录
path = "/Users/apple/weibo/关键字/雄安新区"
files= os.listdir(path) #得到文件夹下的所有文件名称

output_file = ""
keyword_name = ""
count = 0

#遍历文件夹中文件
for file in files:
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
     	file_path = path+"/"+file
     	if os.path.splitext(file_path)[1] == '.xml':
     		print file_path
	     	tree = ET.parse(file_path)
	     	root = tree.getroot()
	     	# print('--------------------------------')
	     	weibo_keyword = root.find(u'列表')[0]
	     	#关键字
	     	keyword_name = weibo_keyword.find(u'关键字').text

	     	# print('---------------------------------')

	     	#博文列表
	     	list = weibo_keyword.find(u'列')
	     	for item in list.iter(u'item'):
 				weibo_content = item.find(u'博文')
 				s = ET.tostring(weibo_content,'utf-8').strip()
 				result = ' '.join(s.split())
 				res_tr = r'<博文>(.*?)</博文>'
 				content = re.findall(res_tr,result,re.S|re.M)
 				for nn in content:
 					#去掉左边空格并编码
 					count += 1
 					output_file = output_file + unicode(nn,'utf-8').lstrip() + '\n'
# print output_file
print ("微博条数:%i" % count)
out = open('/Users/apple/weibo/data' + "/" + keyword_name + ".txt", "w")
out.write(output_file)
print("End")