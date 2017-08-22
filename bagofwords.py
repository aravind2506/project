from collections import Counter
import os
import glob
import re #removes everthing else except numbers,letters and underscore
""" To Open a file from the directory"""
#y=os.listdir(path) 
filename=input("enter a .txt file name ")
filename2=input("enter 2nd file name with .txt")
F1=open(filename,"r")
F2=open(filename2,"r")
s1=F1.read()
s2=F2.read()

""" To put the texts in dictonary"""
d1={}
d2={}
s1=s1.lower()
s2=s2.lower()
#s1=''.join([i for i in s1 if not i.isdigit()]) #to remove numbers
s1=s1.replace(","," ").replace("."," ").replace("\n","")
s2=s2.replace(","," ").replace("."," ").replace("\n","")
s1=s1.split(" ")
s2=s2.split(" ")
d1=Counter(s1)
d2=Counter(s2)
if "" in d1:
        del (d1[""])
if "" in d2:
        del (d2[""])
"""for i in s1:
    if i not in d1:
            d1[i]=1
    else:
            d1[i]+=1
    if "" in d1:
        del (d1[""])
for j in s2:
    if j not in d2:
        if j!=' ':
            d2[j]=1
    else:
        if j!=' ':
            d2[j]+=1"""

print(d1)
print(d2)
L=[]
for i in d1:
    for j in d2:
        if i!=' ':
            if i==j:
                L.append(d1[i]*d2[j])
temp=sum(L)
print(temp)
def eu_norm(L1):
        sum1=0
        for i in L1:
                sum1+=i**2
        return sum1**(0.5)
e1=eu_norm(d1.values())
e2=eu_norm(d2.values())
cos=temp/(e1*e2)
print("match","=",cos*100,"%")
""" To close the file """      
F1.close()
F2.close()
