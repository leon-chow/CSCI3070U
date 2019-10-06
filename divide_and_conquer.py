def divide(string, substring):
    if substring == string: #base case 1
        return True
    if substring and not string: # base case 2
        return False
    if len(string) > 1:
        mid = len(string) // 2
        leftString = string[:mid]
        rightString = string[mid:]
        if leftString == substring or rightString == substring:
            print(True)
            return True
        divide(leftString, substring)
        divide(rightString, substring)
        return (merge(leftString,rightString,substring))

def merge(leftString, rightString, substring):
    # base case if merged strings equal substring
    if substring == leftString + rightString:
        print(True)
        return True

    # for loop to go through each range of characters in the right string and appends it to left, then checks if it is equal to it
    for i in range(len(rightString)): # add 1 character to left end at a time
        combo = leftString + rightString[:i+1]
        #print("leftCombo:",leftCombo)
        if (combo == substring):
            print(True)
            return True

    # if length of left string still > 1, will slice off first character and repeat merge
    if len(leftString) > 1: 
        return merge(leftString[1:len(leftString)], rightString, substring) # recursively merge, removing first character on left string
    return False

#test drive
divide("the quick brown fox jumped over the fence", "own fo") # true
divide("Hello World", " ") # true
divide("Hello World, how are you?", "I am doing fine, how about you?") # false