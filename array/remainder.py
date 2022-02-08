arr = []

for i in range(10):
    n = int(input())
    arr.append(n % 42) #append 함수를 통해 arr 배열에 새로운 요소 추가

arr = set(arr) #set함수를 이용해 중복되는 값제거
print(arr) #서로다른값만 있는 배열의 길이를 통해 수를 측정
