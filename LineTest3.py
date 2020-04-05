def solution(road, n):
    indexes = []
    for i in range(len(road)):
        if road[i] == '0':
            indexes.append(i)
    road = list(road)
    cntlist = []
    if len(indexes) < n:
        return len(road)

    for j in range(len(indexes) - n + 1):
        temp = list(road)
        for x in indexes[j:j + n]:
            temp[x] = '1'
        print(temp)
        temp.append('0')
        cnt = 0
        for y in range(len(temp)):
            if temp[y] == '1':
                if cnt == 0:
                    cnt = +1
                else:
                    if temp[y + 1] == '1':
                        cnt += 1
                    else:
                        cnt += 1
                        cntlist.append(cnt)
                        cnt = 0

    cntlist.append(0)
    answer = max(cntlist)
    return answer