numbers = [1, 2, 3, 4, 5]

def save_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")
    print(f"List saved to {filename}")

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
print("Initial List:", numbers)
while True: 
    print("\nMenu:\n1. Append\n2. Insert\n3. Pop\n4. Remove\n5. Sort\n6. Reverse\n7. Search\n8. Save to file\n9. Load from file\n10. Quit")
    try:
        choice = int(input("Choose an option: "))
        if choice == 1:
            value = int(input("Enter value: "))
            numbers.append(value)
            print("Updated List:", numbers)
        elif choice == 2:
            value = int(input("Enter value: "))
            index = int(input("Enter index: "))
            if index < 0 or index > len(numbers):
                print("Invalid index. Please try again.")
            else:
                numbers.insert(index, value)
                print("Updated List:", numbers)
        elif choice == 3:
            if len(numbers) == 0:
                print("List is empty cannot pop.")
            else:
                numbers.pop()
                print("Updated List:", numbers)
        elif choice == 4:
            value = int(input("Enter value: "))
            if value not in numbers:
                print("Value not found in list cannot remove .")
            else:
                numbers.remove(value)
                print("Updated List:", numbers)
        elif choice == 5:
            numbers.sort()
            print("Sorted List:", numbers)
        elif choice == 6:
            numbers.reverse()
            print("Reversed List:", numbers)
        elif choice == 7:
            value = int(input("Enter value to search: "))
            if value in numbers:
                print(f"Value {value} found at index {numbers.index(value)}")
            else:
                print("Value not found in list.")
        elif choice == 8:
            filename = input("Enter filename to save: ")
            save_to_file(numbers, filename)
        elif choice == 9:
            filename = input("Enter filename to load: ")
            numbers = load_from_file(filename)
            print("Loaded List:", numbers)
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")

print("Goodbye!")

