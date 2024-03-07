#add import
import question_c

exit = False

while exit != True:
    string = input("Enter a string. Enter 0 to exit")
    string = str(string)
    if string != "0":
        rev_string = question_c.reverse_string(string)
        print (rev_string)
    if string == "0":
        exit = True
if exit == True:
    print ("goodbye")
    
    