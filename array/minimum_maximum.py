a = int(input())
arr = list(map(int, input().split()))
min = 1000000
max = -1000000

for i in range(a):
    if(arr[i] < min): min = arr[i]
    if(arr[i] > max): max = arr[i]

print(min, max)

#a = int(input())
#arr = list(map(int, input().split()))
#arr.sort()
#print(arr[0], arr[-1])