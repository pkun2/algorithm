max = 0
judge = False

n = list(input().upper())

processed_n = list()
for i in n:
    if i not in processed_n:
        processed_n.append(i)

for i in processed_n:
    if n.count(i) > 1:
        if n.count(i) == max:
            judge = True
            break
        if n.count(i) > max:
            max = n.count(i)
            maxStr = i
            
if judge == True:
    print("?")
else:
    print(maxStr)
   