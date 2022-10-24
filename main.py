from math import fabs
from operator import truediv
import sys
import errno
import string

if(len(sys.argv)!=5):
    print("\nНеверное количество аргументов\n")
    quit()

arg=sys.argv[1:]
input=arg[0]
first=arg[1]
second=arg[2]
count=arg[3]
count_pair=0
counter=0
pos1=-1
flag=True
flag1=False
flag2=False
if(count.isdigit()==False):
    print("\nРасстояние указано неверно\n")
    quit()
count=int(count)
try:
    with open(input, encoding = 'utf-8', mode = 'r') as file:
        for line in file:
            flag=True
            flag1=False
            flag2=False
            while(flag==True):
                if(line.find(first)>=0):
                    flag==True
                    counter=0
                    pos1=line.find(first)
                    temp_line=line[pos1:]
                    words=temp_line.split()
                    for word in words:                                
                        if(string.punctuation.find(word[len(word)-1])!=-1):
                            pos=words.index(word)
                            index = len(word)-1
                            word = word[:index] + word[index+1:]
                            words[pos]=word

                    if(line.find(second)==-1):
                        counter=counter+len(words)
                        if(counter>count):break
                        for line2 in file:
                            flag2=False
                            if(line2.find(second)==-1):
                                counter=counter+len(words)
                            else:
                                words2=line2.split()
                                counter=counter+words2.index(second)+1
                                for word in words2:
                                    if(string.punctuation.find(word[len(word)-1])!=-1):
                                        word=word[:len(word)-2]
                                    if(word==second):
                                        flag2=True
                                if(flag2==False):continue
                                if(counter<=count):
                                    words[words.index(first)]='udalil'
                                    line=" ".join(words)
                                    words2[words2.index(second)]='udalil'
                                    line2=" ".join(words2)
                                    count_pair=count_pair+1
                                    break
                            if(counter>count):break
                    else:
                        for word in words:
                            if(word==first):
                                flag1=True
                            if(word==second):
                                flag2=True
                        if(flag1==False or flag2==False):break
                        diff=words.index(second)-words.index(first)-1
                        if(diff>count):break
                        words[words.index(first)]='udalil'
                        words[words.index(second)]='udalil'
                        if((diff<=count) and (diff>=0)):
                            line=" ".join(words)
                            count_pair=count_pair+1
                else:
                    flag=False
                    if(counter>count):break


except IOError as x:
    if x.errno == errno.ENOENT:
        print (input, '- не существует')
    elif x.errno == errno.EACCES:
        print (input, '- не может быть прочитан')
    else:
        print (input, '- иная ошибка')

print("Кол-во пар:",count_pair)