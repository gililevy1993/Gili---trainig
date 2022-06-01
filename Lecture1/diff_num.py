"""
This function takes a sequence of numbers and determines
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

number = input("Please enter number: ")
diff_num(number)