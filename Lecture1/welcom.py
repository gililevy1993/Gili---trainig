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
                exit()

        

def main():
    number = input("Pleae enter number: ")
    print("check if there is a diffrent number...")
    diff_num(number)

if __name__ == "__main__":
    main()
