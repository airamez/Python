import random

"""
The finally clause is optional however when present it is always executed, whether an exception has occurred or not.
The finally clause is important to do clean-up code
I tis possible
"""


def read_file(file_name: str) -> str:
    """
    Simulate an operation to read a file
    :return: Fake content of a file
    """
    try:
        print("Open file:", file_name)
        for i in range(1, 4):
            rnd = random.randint(1, 5)
            if rnd != 5:
                print("Read a record =", i)
            else:
                raise Exception("Error reading the file: " + file_name)
        return "File content"
    finally:
        print("Close File:", file_name)

try:
    file_content = read_file("my_file")
    print("File Content", file_content)
except Exception as error:
    print("ERROR =>", error)
