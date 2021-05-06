import sys
sys.stdin=open('sample_input4311.txt','r')

T = int(input())

for t in range(1, T + 1):

    N, O, M = map(int, input().split())
    num = list(map(int, input().split()))
    oper = list(map(int, input().split()))
    W = int(input())

    Possible_oper = [0, 0, 0, 0]
    for i in range(O):
        Possible_oper[oper[i] - 1] = 1
    pn = [0 for i in range(1000)]

    for i in range(N):
        pn[num[i]] = 1

    for i in range(N):
        if num[i] != 0:
            for j in range(N):
                pn[10 * num[i] + num[j]] = 2

        for i in range(N):
            if num[i] != 0:
                for j in range(N):
                    for k in range(N):
                        pn[100 * num[i] + 10 * num[j] + num[k]] = 3

    ans = -1

    if pn[W] != 0:
        ans = pn[W]
    else:
        Q = []
        A = []
        for i in range(1000):
            if pn[i]:
                Q.append(i)
                A.append(i)

        while len(Q):
            n1 = Q.pop(0)
            for j in range(len(A)):
                n2 = A[j]
                if pn[n1] + pn[n2] + 1 <= M:

                    if Possible_oper[0]:
                        if n1 + n2 < 1000:
                            if (pn[n1] + pn[n2] + 1 < pn[n1 + n2] or pn[n1 + n2] == 0):
                                pn[n1 + n2] = pn[n1] + pn[n2] + 1
                                Q.append(n1 + n2)

                    if Possible_oper[1]:
                        if n1 - n2 >= 0:
                            if (pn[n1] + pn[n2] + 1 < pn[n1 - n2] or pn[n1 - n2] == 0):
                                pn[n1 - n2] = pn[n1] + pn[n2] + 1
                                Q.append(n1 - n2)

                    if Possible_oper[2]:
                        if n1 * n2 < 1000:
                            if (pn[n1] + pn[n2] + 1 < pn[n1 * n2] or pn[n1 * n2] == 0):
                                pn[n1 * n2] = pn[n1] + pn[n2] + 1
                                Q.append(n1 * n2)

                    if Possible_oper[3]:
                        if n2 != 0 and n1 // n2 < 1000:
                            if (pn[n1] + pn[n2] + 1 < pn[n1 // n2] or pn[n1 // n2] == 0):
                                pn[n1 // n2] = pn[n1] + pn[n2] + 1
                                Q.append(n1 // n2)

        if pn[W] != 0 and pn[W] + 1 <= M:
            ans = pn[W] + 1

    print('#%d %d' %(t, ans))