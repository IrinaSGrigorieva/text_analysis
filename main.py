#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']='StixGeneral'
#открываем файл для чтения
stream = open(sys.argv[1])
text = stream.read()
text = text.decode('utf-8')
#заменяем знаки
tochka=["...","?","?..","!","!..",".  "]
probel=[", "]
pusto=[":","\n",";","   ","\r","   ","- ","\n  ",'"',"  "]
for p in tochka:
    text = text.replace(p,".")
for p in probel:
    text = text.replace(p," ")
for p in pusto:
    text = text.replace(p,"")
text = text.replace(". ",".")
text = text.replace("..",".")
#создаем словарь
kolich = dict()
#делим текст на предложения и записываем в predloj
predloj = text.split(".")
maxim=len(predloj)
#удаляем пустые элементы
for i in range(0,maxim):
    if (predloj[i] == ""):
         del predloj[i]
i=1
dlina=maxim-1
while (i<dlina):
#записывает в temp первый символ предложения
    temp=predloj[i][0]
#проверяем, если не заглавная, то соединяем с предыдущим
    if not temp.istitle():
        predloj[i-1]=predloj[i-1]+" "+predloj[i]
        del predloj[i]
        dlina=dlina-1
        i=i-1
    i=i+1

#for i in range(0,dlina):
#    print predloj[i]

#заполняем словарь, подсчитывая предложения
for i in predloj:
    kolich[len(i.split(" "))] = kolich.get(len(i.split(" ")),0) + 1

for k in sorted(kolich):
    print u'из' ,k, u'слов -', kolich[k], u'предложений'

#строим график
plt.bar(kolich.keys(), kolich.values(), 0.3, color='Green')
plt.ylabel(u'Число предложений', {'fontsize':18})
plt.xlabel(u'Число слов в предложении', {'fontsize':18})
plt.ylim([0,max(kolich.values())+1])
plt.show()
