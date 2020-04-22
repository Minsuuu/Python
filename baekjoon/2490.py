def result(n):
    dictionary = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '0': 'E'}
    return dictionary.get(n)
for i in range(3):
    play=input()
    num = str(play.count('0'))
    print(result(num))
    
'''
for i in range(3):
    play = input()
    if play.count('0')==1:
        a="A"
    elif play.count('0')==2:
        a= "B"
    elif play.count('0')==3:
        a = "C"
    elif play.count('0')==4:
        a = "D"
    else:
        a = "E"
    print(a)
'''