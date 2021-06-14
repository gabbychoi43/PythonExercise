


# 동명이인의 처리가 필요하다.
#
def solution(enroll, referral, seller, amount):
    answer = []
    dic = {}
    dic['center'] = {}
    dic['center']['amount'] = 0

    degrees = {}
    # 각 노드별 부모 노드 구하기
    for i in range(len(enroll)):
        dic[enroll[i]] = {}
        if referral[i] == '-':
            dic[enroll[i]]['parent'] = 'center'
        else:
            dic[enroll[i]]['parent'] = referral[i]


    #노드별 amount 초기화
    for i in dic:
        dic[i]['amount'] = 0
    # seller별 판매량 입력
    for i in range(len(seller)):
        dic[seller[i]]['amount'] += amount[i] * 100

    # 각 노드의 차수 계산하기. center는 0차
    degrees[0] = ['center']
    m = 0
    for i in dic:
        if i == 'center':
            continue
        degree = 0
        node = i
        #순회하며 center가 나올때까지 degree를 더해준다.
        while True:
            if node == 'center':
                break
            if node != 'center':
                degree += 1
                node = dic[node]['parent']

        dic[i]['degree'] = degree
        # degree 배열에 degree 합해주기
        try:
            degrees[degree].append(i)
        except:
            degrees[degree] = [i]
        m = max(degree, m)
    #degree값 배열 생성
    L = [i for i in range(1, m + 1)]
    while L:
        x = L.pop()
        # 하나씩 뽑으며 해당 차수에 해당하는 노드에서 10%씩 부모로 떼어준다.
        for i in degrees[x]:
            try:
                y = int(dic[i]['amount'] * 0.1)
                dic[dic[i]['parent']]['amount'] += y
                dic[i]['amount'] -= y
            except:
                pass

    for i in enroll:
        answer.append(dic[i]['amount'])
    return answer