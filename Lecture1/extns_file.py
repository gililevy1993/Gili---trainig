
"""
This function accept a filename from the user 
and print the extension of file.
"""
from asyncore import file_dispatcher


def extns_file(filename):
    extns = filename.split(".")
    print("The extension of the file is : " + repr(extns[-1]))

file_name = input("Please neter filename: ")
extns_file(file_name)