
n = int(input())
arr = list(map(int, input().split()))
max = -10000

for i in range(n):
    if (arr[i] > max):
        max = arr[i] # 최대값을 구하기

newArray = []
for score in arr:
    newArray.append(score/max*100) #score가 하나씩 추가되어 append함수로 newArray 배열에 추가

totalAvg = sum(newArray)/n

print(totalAvg)