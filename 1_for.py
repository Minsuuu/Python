list1=["a","b","c"]
list2=["j","d","k"]

for i in [0,1,2]:
    print(i, end=" ")
    for j in list1 :
        print(j,end="")
    print()
    print(i, end=" ")
    for k in list2 :
        print(k,end="")
    print()