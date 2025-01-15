string = input("Please type in a string : ")
line = ""
for i in string:
    print(i + "*")
    line += i + "*"

print(line)