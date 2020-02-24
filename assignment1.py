lst1=list(map(str,input().split()))
lst2=[lst1[0]]
for i in range(len(lst1)):
    for j in range(1,len(lst2)):
        if lst2[i][-1]==lst1[j][0]:
            lst2.append(lst1[j])
            lst1.remove(lst1[j])
            break
print(lst2)
