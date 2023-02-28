name=input('What is your name? ')
x=len(name)
if x<3:
    print('name must be atleast three characters')
elif x>50:
    print('name can be max of fifty characters')
else:
    print('name looks good')