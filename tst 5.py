lst=[]
nlst=[]
L1=int(input("Enter number of elements in list 1 "))
for ELE in range(L1): 
    L_ele=int(input("Enter List 1 element "))
    lst.append(L_ele)
L2=int(input("Enter number of elements in list 2 "))
for ELE in range(L2): 
    L_ele=int(input("Enter List 2 element "))
    nlst.append(L_ele)
s1=set(lst)
s2=set(nlst)
print(s1.intersection(s2))
