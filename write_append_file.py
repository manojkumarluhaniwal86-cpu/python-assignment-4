# write_append_file.py

def write_and_append():
    # Step 1: Write data to file
    user_data = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_data + "\n")

    print("Data written successfully!")

    # Step 2: Append extra data
    extra = input("Enter text to append to the file: ")
    with open("output.txt", "a") as file:
        file.write(extra + "\n")

    print("Data appended successfully!")

    # Step 3: Read final file content
    print("\nFinal file content:\n")
    with open("output.txt", "r") as file:
        print(file.read())


write_and_append()
