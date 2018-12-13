marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
list1 = []
for i in marks:
    if i > 50:
        list1.append(i)
list2 = []
for i in marks:
    if i < 50:
        list2.append(i)        
print(list1)
for i in list1:
    if i >= 90:
        print('Excellent')
    elif i >= 60 or i == 69:
        print('good') 
    elif i >= 40 or i == 59:
        print('poor')  
    elif i >= 20 or i == 39:
        print('very poor')
    else:
        print('repeat')  
print(list2)
for i in list2:
    if i >= 90:
        print('Excellent')
    elif i >= 60 or i == 69:
        print('good') 
    elif i >= 40 or i == 59:
        print('poor')  
    elif i >= 20 or i == 39:
        print('very poor')
    else:
        print('repeat')  