cycle = int(input());
wordContinue = 0;

for i in range(cycle):
    wrong = 0;
    word = input();
    for a in range(len(word)-1):
        if word[a] != word[a+1]:
            new = word[a+1:];
            if new.count(word[a]) > 0:
                wrong +=1;
    if wrong == 0:
        wordContinue += 1;

print(wordContinue);
