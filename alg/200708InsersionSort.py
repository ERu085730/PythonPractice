import numpy as np

def Swap(data,f):
    reg = data[f]
    data[f] = data[f+1]
    data[f+1] = reg

def Sort(data):
    print(data)
    count = 0
    leng = len(data)
    for t in range(1,leng):    #from data[1] start to sort ,and end of data[end]
        for i in range(t,0,-1):      #compare data and swap
            count +=1
            if(data[i-1]>data[i]):
               Swap(data,i-1)
               print(data)
            else:
                break
    print("times ",count)
    print("result of sort ",data)

data = np.array([63,15,7,21,8,45])
Sort(data)

    
