# Task 9 Cat problem
# You've collected too many cats. Write a program to count how
# many cats you have by reading in their names. All your cats only
# have first names, with no spaces.

def main():
    #Write your code here
    cats = input('Cats: ')
    cats_name = cats.split()
    print('You have ' + str(len(cats_name)) + ' cats.')


    # End of your code here





if __name__ == '__main__':
    main()