# Using Absolute path:
with open("/Users/Guilherme/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Using Relative Path:
with open("../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
