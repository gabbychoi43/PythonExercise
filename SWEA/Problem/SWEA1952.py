
import sys

sys.stdin = open('SWEA1952', 'r')


T = int(input())

for t in range(1, T + 1):
    day, month, quater, year = [int(i) for i in input().split()]
    Month = [int(i) for i in input().split()]
	# f(n) = n번째 달까지 최소 금액으로 정의
    DP = [0]
    for i in range(len(Month)):
        DP.append(min(day * Month[i],month))
	#각 달별로 일자별이 작은지 월별이 작은지 기록
    for i in range(1,13) :
        DP[i]=min(DP[i-1]+DP[i],DP[i-3]+quater)
	#달을 순회하면서 이전달+다음달 최소가 작은지 3달전+3달치가 작은지 기록
    print('#%d %d'%(t,min(DP[-1],year)))