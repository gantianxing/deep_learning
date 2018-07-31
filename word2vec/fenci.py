#-*- coding:utf-8 -*-
import jieba
import codecs

with codecs.open('天龙八部.txt', 'r+','utf-8') as fp:
   lines = fp.readlines()
   for line in lines:
	   seg_list = jieba.cut(line)

	   with codecs.open('天龙八部分词.txt', 'a','utf-8') as ff:
		   ff.write(' '.join(seg_list))  # 逗号分隔



