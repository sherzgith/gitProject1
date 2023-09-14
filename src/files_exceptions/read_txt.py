#  Chaper 10: Read files ( txt)

# synatx:
# with open(filepath, 'r') as file_object:
# or open(filepath, 'w') - we use 'w' to truncate the old content and write brand new
# or we use 'a' to append new content to existing content
# with open(filepath) as file_object:
#     file_contents = file_object.read() # option 1 - get the whole content
#     file_lines = file_object.readlines() # option 2 - get all lines in a list

#     file_line = file_object.readline() # returns line1
#     file_line = file_object.readline() # returns line2
#     file_line = file_object.readline() # returns line3

# print(file_contents)
# print(file_lines[1]) returns the second line of the file ( just like a list)


filepath_txt = "../../data/fruits.txt"
with open(filepath_txt) as file_object:
    file_contents = file_object.read()
    print("********Now printing the contents ***************")
    print(file_contents)



with open(filepath_txt) as file_object:
    print('-----------------Reading line by line------------------')
    for fruit in file_object:
        print(f" Current loop fruit: {fruit.strip()}")

with open("cars.txt") as file_object:
    file_contents = file_object.read()
    print("********Now printing the contents ***************")
print(file_contents)

