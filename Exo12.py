width = int(input("Width: "))
if width < 0 :
    print("invalid width")
    exit()

height = int(input("Height: "))
if height < 0 :
    print("invalid height")
    exit()

print((" " + "#" * width) * height)