import os.path                          #to import files from directory
from collections import Counter         #to count number of words 
import math                             #to round off the integer
import string                           #to remove punctuations 

path=input("Enter the path of dir")
a=os.listdir(path)
os.chdir(path)

def file_split(s):                                              #function for spliting words from file
        s=s.lower()
        s=s.replace("\n"," ").replace("\xa0"," ")
        s=s.split(" ")
        s=[word.strip(string.punctuation)for word in s]         #removing punctuations
        return s

def frequency(str1):                                            #function to calculate the frequency of words
        d1=Counter(str1)
        if "" in d1:
            del (d1[""])
        return d1
    
def eu_numerator(d1,d2):                                        #function to calculate the numerator of cosine function   
        L=[]
        for i in d1:
            for j in d2:
                if i==j:
                    L.append(d1[i]*d2[j])
        return sum(L)

def eu_denominator(d):                                          #function to calculate the denominator of cosine function
        sum1=0
        for i in d:
            sum1+=(d[i])**2
        return (sum1**(1/2))
    
def plag(file1,file2):                                          #function to determine plagarism of files

    str1=file_split(file1.read())
    str2=file_split(file2.read())
    d1=frequency(str1)
    d2=frequency(str2)
    numer=eu_numerator(d1,d2)
    denom=(eu_denominator(d1))*(eu_denominator(d2))
    return round((numer/denom)*100)                             #returning the cos value

final=[]
for m in range (len(a)):
    for n in range (len(a)):
        if m==n:
            final.append("None")
        else:
            file1=open(a[m],"r")
            file2=open(a[n],"r")
            final.append(plag(file1,file2))
            file1.close()
            file2.close()
    print(a[m],final,"\n")                                      #printing of matching percentage
    final=[]    
