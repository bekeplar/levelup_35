#words = input('sentence: ')
# printing a given sentence in capital letters.
#print(words.upper())
def capitalize(sen):
    """Function to capitalize a given sentence."""
    return sen.upper()

if __name__ == '__main__':
    sen = input('Please type a sequence of characters \n')
    """Asking for user input"""
    print(capitalize(sen))