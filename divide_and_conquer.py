def divide(string, substring):
    if substring == string: #base case 1
        return True
    if substring and not string: # base case 2
        return False
    if len(string) > 1:
        mid = len(string) // 2
        leftString = string[:mid]
        rightString = string[mid:]
        if substring in leftString or substring in rightString: 
            return True
        divide(leftString, substring)
        divide(rightString, substring)
        return merge(leftString,rightString,substring)
    else:
        return False

def merge(leftString, rightString, substring):
    # base case if merged strings equal substring
    if substring == leftString + rightString:
        return True
    # for loop to go through each range of characters in the right string and appends it to left, then checks if it is equal to it
    for i in range(len(rightString)): # add 1 character to left end at a time
        combo = leftString + rightString[:i+1]
        #print("leftCombo:",combo)
        if (combo == substring):
            return True

    # if length of left string still > 1, will slice off first character and repeat merge
    if len(leftString) > 1: 
        return merge(leftString[1:len(leftString)], rightString, substring) # recursively merge, removing first character on left string
    else:
        return False

#test cases
#rint(divide("Green", "en")) # true
#print(divide("the quick brown fox jumped over the fence", "the quick brown fox jumped ove")) # true
#print(divide("Hello World", "ello W")) # true
#print(divide("Hello World, how are you?", "I am doing fine, how about you?")) # false
print(divide("You have a long string containing many characters (such as this paragraph), and you want to search for a substring within this string.", "bstring wi"))
print(divide("You have a long string containing many characters (such as this paragraph), and you want to search for a substring within this string.", "want to"))
print(divide("You have a long string containing many characters (such as this paragraph), and you want to search for a substring within this string.", "characters"))
print(divide("You have a long string containing many characters (such as this paragraph), and you want to search for a substring within this string.", "language"))