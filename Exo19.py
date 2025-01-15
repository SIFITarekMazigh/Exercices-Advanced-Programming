unique_words = set()

while True:
    word = input("Enter a word : ")
    word = word.strip()
    if word in unique_words :
        print(f"the count of unique words is {len(unique_words)}")
        break
    else:
        unique_words.add(word)


# bonus
all_words = []
unique_words = set()
cond = True
while cond:
    word = input("Enter a word : ")
    word = word.strip()

    for w in unique_words :
        if w.lower() == word.lower() :
            print(f"the count of unique words is {len(unique_words)}")
            cond = False
            break
    all_words.append(word)
    unique_words.add(word)

print(f"total word = {len(all_words)}")
print("sorted_unique_words : ")
sorted_unique_words = sorted(unique_words)
for w in sorted_unique_words :
    print(w)

answer = input("do you want to save unique words to file ? (Y/n):")
if answer.lower() == "y" :
    filename = input("file name : ")
    with open(filename , "w") as f:
        for w in unique_words:
            f.write(w + "\n")