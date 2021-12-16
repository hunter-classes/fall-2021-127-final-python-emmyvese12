#Question 1
def isIncreasing(L):
    tf_list = []
    new = []
    temp = L[0]
    for item in L:
        if item > temp:
            tf_list.append("True")
            temp = item
        else:
            tf_list.append("False")
            temp = item
    tf_list.remove(tf_list[0]) #removes the first one because the first item of the list will never be greater than temp because they are the same 
    for item in tf_list:
        if item == "True":
            result = True
        elif item == "False":
            result = False
            break 
    return result

#Question 2
def NumConvert(numlist):
    result = ""
    for num in numlist:
        num = int(num)     
        result = result + str(num)
    int_result = int(result)
    return int_result

#Question 3
def BinConvert(binary_string): #binary to decimal 
    reversed = []
    decimal = 0
    for num in binary_string:
        reversed.append(num)
    reversed.reverse()
    final_binlist = "".join(reversed) #reversed to make it easier to match up the index (2^0, 2^1 etc)
    bin_length = len(final_binlist)
    for item in range(bin_length):
        decimal = decimal + 2**item * int(final_binlist[item]) #binary is base 2
    return decimal

if __name__ == "__main__":
    print("------------------------Question 1------------------------")
    print("The function takes in a list of integers and sets a temp variable (the first item L[0]) to test whether the items of the list are greater than that variable, if it is, it adds 'True' to a list, if not, it adds 'False', and another for loop is created to check if all of the strings in that list are 'True', (disregarding the first one), if a 'False' string is detected, the function breaks, and returns False.\n")
    print("==ANSWERS==")
    print("[1,2,3,4,5] should return True:", isIncreasing([1,2,3,4,5]))
    print("[1,2,4,5,2,7] should return False:", isIncreasing([1,2,4,5,2,7]))
    print("[8,2,3,4,5] should return False:", isIncreasing([8,2,3,4,5]))
    print("------------------------Question 2------------------------")
    print("The function takes in a list of numbers and a new string is created to hold the number, for every number in the list, it is added to the empty string, result, and result is then converted to an integer.\n")
    print("==ANSWERS==")
    print("Should return 351:", NumConvert([3,5,1]))
    print("Should return 457:", NumConvert([4,5,7]))
    print("------------------------Question 3------------------------")
    print("The function takes in a string with a binary number, then each number is added to a list, which will be reversed to make it easier to match up each position (most significant bit to least). Once reversed, every item in the range of the length of the list, will add 2 to the power of its postion multiplied by the item corresponding to that position, (for example: 2^1 * 1). The total will be calculated and returned.\n")
    print("==ANSWERS==")
    print("'100' should return 4:", BinConvert("100"))
    print("'101' should return 5:", BinConvert("101"))
    print("'1011' should return 11:", BinConvert("1011"))