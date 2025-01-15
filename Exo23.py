try:
    n = int(input("Enter number : "))
    if n < 0:
        print("Number cannot be negative.")
        exit()
except ValueError:
    print("Invalid Input ")
    exit()

for i in range(-n , n+1):
    if i != 0:
        print(i)