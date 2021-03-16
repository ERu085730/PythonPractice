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

def BuildHeap(data,dt):
    if(dt ==0):         # for first times
        for i in range((leng-1-dt)//2,0,-1): 
            MaxHeap(data,dt,i)
    else:                   # for sort of maxheap
        for i in range(1,((leng-1-dt)//2)+1):
            MaxHeap(data,dt,i)

 
def Sort(data): #heap sort
    data= np.insert(data,0,0)
    global leng,dt
    leng = len(data)
    dt = 0
    BuildHeap(data,dt)
    for i in range(1,leng-1):
        dt +=1
        Swap(data,1,leng-dt)
        BuildHeap(data,dt)
    data = np.delete(data,0)
    print("result = ",data)

#data = np.array([63,15,7,21,8,14])    
data = np.array([63,15,7,21,8,45,72,88,22,44,33,16,82,56])
print(data)
Sort(data)
