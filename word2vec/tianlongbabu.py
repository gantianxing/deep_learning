#-*- coding:utf-8 -*-

from gensim.models import word2vec


sentences = word2vec.Text8Corpus('天龙八部分词.txt')
model = word2vec.Word2Vec(sentences)
for e in model.most_similar(positive=['乔峰'], topn=10):
    print(e[0], e[1])
    
print('乔峰与慕容复关系度：',model.similarity('乔峰', '慕容复'))

list1 = ['乔峰', '慕容复']
list2 = ['萧远山', '慕容博']
print(model.n_similarity(list1, list2))
print(model['乔峰']) 