# Task 6 Find bear
# Write a program to work out whether a line of input text contains a
# bear or not. Your program needs to find cases where the word
# appears in full, with no breaks.

def main():
    #Write your code here
    text = input('Enter line: ')

    if 'bear' in text:
        print("There's a bear in the line.")
    else:
        print('No bears in the line.')

        
    
    # End of your code here





if __name__ == '__main__':
    main()