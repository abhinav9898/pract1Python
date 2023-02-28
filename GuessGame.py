secret_number = int(input('Enter Secret number: '))
guess_limit=3
guess_count=0

while guess_count < guess_limit:
    guess= int(input('Enter a number: '))
    guess_count += 1
    if secret_number == guess:
        print('You won !')
        break
else:
    print('You failed !')
