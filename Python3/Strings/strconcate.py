# To change string we can use concatenation
# str="Aditya"
# lastStr=str[1:]
#
# print("D"+lastStr) # Using plus operator
#
# print(10 * lastStr) # Using * to print same multiple times
#########################################################################################################

#To add new string without using concatenation
#(1).format()method
#(2)f-strings(formatted string literals


print("This is a string {}".format("Added"))#--Grab the string which needs to be inserted and add it to curly braces.

print("This is a string {1} {0}".format("Added","Hello"))#-->Can put index values to add string accordingly

print("The {q} {b} {f}".format(f="fox",b="brown",q="quick"))#-->Can assign variable for easy read
