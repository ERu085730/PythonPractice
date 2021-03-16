import numpy as np


def Merge(data,L,R):
    i = j = 0
    while i <len(L) and j<len(R):
        if (L[i] <R[j]):
            data[i+j]= L[i]
            i+=1
        else:
            data[i+j]=R[j]
            j+=1

    while (i+j) <(len(L)+len(R)):
        if(i < len(L)):
            data[i+j] = L[i]
            i+=1
        else:
            data[i+j] = R[j]
            j+=1
    print(data)
    
def Sort(data):
    leng = len(data)
    if(leng > 1):
        mid = leng//2
        L = data[:mid]
        R = data[mid:]

        Sort(L)
        Sort(R)
        print("L",L)
        print("R",R)
        Merge(data,L,R)

data= [63,15,7,21,8,14,25,45]
#data = np.array([63,15,7,21,8,14,25,45])
#data = np.array([63,15,7,21,8,45,72,88,22,44,33,16,82,56])
print(data)
Sort(data)
print("result = ",data)
