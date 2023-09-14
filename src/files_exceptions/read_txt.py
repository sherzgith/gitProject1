#  Chaper 10: Read files ( txt)

# synatx:
# with open(filepath) as file_object:
#     file_contents = file_object.read()
#     print(file_contents)

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

