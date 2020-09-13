list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
i = 0
while i < len(list1) :
    if list1[i] < 0 :
        del list1[i]
    i = i+1
i=0
while i < len(list2) :
    if list2[i] < 0 :
        del list2[i]
    i = i+1
print(list1)
print(list2)
