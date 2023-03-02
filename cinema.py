films = {
    "Finding dory":[3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Burners":[12,5]
}
while True:
    choice = input("Hi, which movie you wanna watch?: ").strip().title()
    if choice in films:
        age= int(input("How old are you?: ").strip())
        if (age >= films[choice][0]) and (films[choice][1] >0):
            print(f'We have {films[choice][1]} seats left, pls book fast')
        else:
            print("pls try some other movie")
    else:
        print("We dont have that film")

