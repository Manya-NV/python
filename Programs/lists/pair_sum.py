num=[1, 2, 3, 4, 5, 6]
sum=6
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==sum:
            print(num[i],num[j])


