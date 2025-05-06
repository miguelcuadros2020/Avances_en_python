#add the elements in a list
"""
num: list[int] =[1,2,3,4,5,6,7,8,9]
print(sum(num))"""

# remove suplicate elements form a list

"""num: list[int] = [1,2,2,3,3,4,4,4,5,6,7,8,8,9,9,9,9,9]
new_num:list[int] = set(num)
print(new_num)"""

# reverse a list

num : list[int] = [1,2,3,4,5,6]
y = 0
lista = []
for i in num:
    y += 1

while y>0:
    y-=1
    lista += [num[y]]
    
print(lista)