A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))

for i in range(10):
    print(result.count(str(i))) 
    #count 함수를 이용하여 result내의 문자열에 수를 문자열화된 i와 비교하여 같은수를count한다