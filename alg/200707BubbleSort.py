import numpy as np

def Swap(data,f):
    reg = data[f]
    data[f] = data[f+1]
    data[f+1] = reg

def Sort(data):
    count = 0
    leng = len(data)
    for t in range(leng-1):
        for i in range(leng-1-t):
            if(data[i] > data[i+1]):
                Swap(data,i)
            print(data)
            count +=1

data= [63,15,7,21,8,14,25,45]
#data = np.array([63,15,7,21,8,14,25,45])    
#data = np.array([63,15,7,21,8,45,72,88,22,44,33,16,82,56])
print(data)
Sort(data)
print("result = ",data)
