string = input("Please type in a string: ").lower()

vowels = ['a' , 'e' , 'o']

for e in vowels :
    if string.__contains__(e) :
        print(f"{e} found")
    else :
        print(f"{e} not found")