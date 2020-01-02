#coding:gbk
"""
统计人物关系
作者:李莲秋
"""

import codecs
import jieba.posseg as pseg
import jieba
name={}
relation={}
linename=[]
jieba.load_userdict("1.txt")
with codecs.open("黎明破晓的街道.txt","r","utf8") as f:
	for x in f.readlines():
		x=pseg.cut(x)
		linename.append([])
		for y in x:
			if y.flag!="nr" or len(y.word)<2:
				continue
			linename[-1].append(y.word)
			if name.get(y.word) is None:
				name[y.word]=0
				relation[y.word]={}
				name[y.word]+=1
		
for line in linename:
	for name1 in line:
		for name2 in line:
			if name1==name2:
				continue
			if relation[name1].get(name2) is None:
				relation[name1][name2]=1
			else:
				relation[name1][name2]=relation[name1][name2]+1

with codecs.open("people_node.txt","w","utf8") as f:
	f.write("ID Label Weight\r\n")
	for name,times in name.items():
		if times>10:
			f.write(name+" "+name+" "+str(times)+"\r\n")

with codecs.open("People_edge.txt","w","utf8") as f:
	f.write("Source Target Weight\r\n")
	for name,edges in relation.items():
		for v,w in edges.items():
			if w>10:
				f.write(name+" "+v+" "+str(w)+"\r\n")
