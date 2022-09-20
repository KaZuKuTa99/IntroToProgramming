#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #5
# Due---------October 24,2018
#
# converts English words to Herd Latin. It includes a 
# sentinel loop to enable the user to enter and convert 
# any number of words. The user enters a null string to
# serve as the sentinel to terminate the loop.
#--------------------------------------------------------

word = input("English ----- ")
seperator = 'bison'
count = 0
count_sep = 0
herd = ""
while len(word) > 0:
# Sets the sentinal to stop when user enters a null string
    while count < len(word):
# Makes sure secondary while loop stops when the word ends
        herd += word[count] + seperator[count_sep]
        count += 1
        count_sep += 1
        if count_sep > 4:
            count_sep = 0
# Makes 'bison' loop back once 'bison' string ends
    print(herd[:-1])
    word = input("English ----- ")
# Resets variables for new word string 
    count = 0
    count_sep = 0
    herd = ""
