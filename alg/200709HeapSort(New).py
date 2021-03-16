import numpy as np

def Swap(data,f,large): #Swap data posision
    reg = data[f]
    data[f]=data[large]
    data[large]=reg

def MaxHeap(data,dt,i): #makesure data was  maxheap_tree
    reg = i
    if(2*i<=(leng-1-dt) and (data[i]<data[2*i])):
        reg = 2*i
        
    if((2*i+1)<=(leng-1-dt) and (data[reg]<data[2*i+1])):
        reg = 2*i+1
            
    if(reg != i):
        Swap(data,i,reg)
        print(data)
        MaxHeap(data,dt,reg)
 
def Sort(data): #heap sort
    data= np.insert(data,0,0)
    global leng,dt
    leng = len(data)
    dt = 0
    
    for i in range((leng-1)//2,0,-1): 
            MaxHeap(data,dt,i)
            
    for i in range(1,leng-1):
        dt +=1
        Swap(data,1,leng-dt)
        MaxHeap(data,dt,1)
    data = np.delete(data,0)
    print("result = ",data)

#data = np.array([63,15,7,21,8,14])    
data = np.array([63,15,7,21,8,45,72,88,22,44,33,16,82,56])
print(data)
Sort(data)
