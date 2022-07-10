# To change string we can use concatenation
# str="Damar"
# lastStr=str[1:]
#
# print("A"+lastStr) # Using plus operator
#
# print(10 * lastStr) # Using * to print same multiple times
#########################################################################################################

#To add new string without using concatenation
#(1).format()method
#(2)f-strings(formatted string literals

#
# print("This is a string {}".format("Added"))#--Grab the string which needs to be inserted and add it to curly braces.
#
# print("This is a string {1} {0}".format("Added","Hello"))#-->Can put index values to add string accordingly
#
# print("The {q} {b} {f}".format(f="fox",b="brown",q="quick"))#-->Can assign variable for easy read
#
# str=input("Enter the string:")
# print("{} {}".format(str[0:5],str[6:]))


#float formatting follows "{value:width.percision f}"
#-->value--that needs to print,width-->how long you want,precision-->place upto which it should print

result=1/77
print("The result {r:1.3f}".format(r=result))

#f-string literal method

name="Aditya"
print(f"Hello, My name is {name}")#-->giving the variable in curly braces

firstName=input("Enter first name:")
lastName=input("Enter last name:")
print(f"User full name is {firstName} {lastName}")