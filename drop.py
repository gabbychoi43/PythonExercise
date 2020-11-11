def drop(map):
    count = 0
    K=[]
    for m in map :
        while 0 in m:
            m.remove(0)
            count += 1
        l = [0] * count
        m=l+m
        K.append(m)
        count=0

    return K


print(drop([[0,0,5,4,0,0,6,2],[0,0,7,3,0,8,3,0]]))