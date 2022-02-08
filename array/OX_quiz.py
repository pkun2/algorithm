n = int(input())

for i in range(n):
    ox = input()
    arr = list(ox)
    sum = 0
    c = 1
    for i in arr:
        if i == "O":
            sum += c 
            c += 1  # O를 만났을때 1더하기
        else:
            c = 1 #아닐시 c = 1로 변환
    print(sum)