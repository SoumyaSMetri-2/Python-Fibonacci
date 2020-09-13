num = int(input('How many numbers do you want Fibonacci series: '))
i = 0;
lst = list()
while i<2 :
    lst.append(i)
    i = i+1
while i<num:
    lst.append(lst[i-2]+lst[i-1])
    i = i+1
print(lst)
print(len(lst))
