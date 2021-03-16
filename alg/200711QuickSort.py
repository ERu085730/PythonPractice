import numpy as np


def Swap(data,f,s):
    reg = data[f]
    data[f] = data[s]
    data[s] = reg

def Sort(data,f,e):
    pivot = data[e]
    j = f
    if(f<e):
        for i in range(f,e):
            if((data[i]< pivot) and (i!=j)):
                Swap(data,i,j)
                j+=1
            elif(data[i]< pivot):
                j+=1
            
        Swap(data,j,e)
        print(data)
        Sort(data,f,j-1)
        Sort(data,j+1,e)

#data= [63,15,7,21,8,14,25,45]
data= [63,15,7,14,45,21,8,25]
print(data)
Sort(data,0,len(data)-1)
print("result = ",data)

