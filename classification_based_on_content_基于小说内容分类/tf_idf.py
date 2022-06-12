#coding=utf-8
import jieba
import sys
import sklearn
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = []
with open("1 (2).txt", 'r',encoding='utf-8') as f:
    for line in f:
        corpus.append(" ".join(jieba.cut(line.split(',')[0], cut_all=False)))

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)
print (tfidf.shape)

words = vectorizer.get_feature_names()
for i in range(len(corpus)):
    print ('----Document %d----' % (i))
    for j in range(len(words)):
        if tfidf[i,j] > 1e-5:
              print (words[j], tfidf[i,j])
