# File Creation
with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1\n")
    file.write("12345\n")
    file.write("Adding a mix of strings and numbers\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

# File Appending
with open("my_file.txt", "a") as file:
    file.write("Appending line 1\n")
    file.write("67890\n")
    file.write("Adding more content to the file\n")

# Error Handling
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File handling completed.")

