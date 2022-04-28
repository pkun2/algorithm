croatia_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];
count=0;
num = 0;
word = input();

for a in croatia_list:
    if a in word:
        word = word.replace(a, " ");
print(len(word));