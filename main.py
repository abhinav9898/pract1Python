numbers=[2,3,3,4,6,7,8,9,10,9,8]
uniques=[]

for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)