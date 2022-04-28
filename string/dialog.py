alphabet_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"];
time = 0;
word = input();

for a in alphabet_list:
    for i in a:
        for j in word:
            if i == j:
                time += alphabet_list.index(a) + 3;
                
print(time);