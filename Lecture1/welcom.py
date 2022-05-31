'''
This program prints Welcome to QMasters!! on the screen
'''

print("Welcome to QMasters!!")

"""
THis function takes a sequence of numbers and determines
whether all the numbers are different from each other.
If not, print the index of one of repeated numbers.
"""
def diff_num(number):
    number = str(number)

    for digit in number:
        for j in number:
            if j == digit:
                print(j)
                return
"""
This function accept a filename from the user 
and print the extension of file.
"""
def extns_file(filename):
    extns = filename.split(".")
    print("The extension of the file is : " + repr(extns[-1]))


def main():
    number = input("Pleae enter number: ")
    print("check if there is a diffrent number...")
    diff_num(number)
    filename = input("Please Enter a filename: ")
    extns_file(filename)

if __name__ == "__main__":
    main()
