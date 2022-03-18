string = input().upper();
uniqueWords = list(set(string));

cntList = [];
for i in uniqueWords:
    cnt = string.count(i);
    cntList.append(cnt)

if cntList.count(max(cntList)) > 1:
    print("?");
else:
    maxindex = cntList.index(max(cntList));
    print(uniqueWords[maxindex]);
