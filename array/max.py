arr = []
max = -1000000
count = int

for i in range(9):
    arr.append(int(input()))
    if(arr[i] > max): 
        max = arr[i]
        count = i+1
    
print(max)
print(count)