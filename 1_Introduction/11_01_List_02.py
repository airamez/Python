# TODO: Prepare this file

my_list = []

while True:
    my_string = input("Type something [EMPTY to end] = ")
    if my_string == "":
        break
    else:
        my_list.append(my_string)
print(my_list)
print(len(my_list))
first = 0
last = len(my_list) - 1
print(my_list[first])
print(my_list[last])

print(my_list[len(my_list)])  # IndexError: list index out of range
