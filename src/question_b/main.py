import question_b

Exit = False

while Exit != True:
    num = input("Enter a number between 1 and 7. Enter Exit to exit")
    if num != "Exit":
        num = int(num)
        day = question_b.get_day_of_week(num)
        print(day)
    if num == "Exit":
        Exit = True
if Exit == True:
    print ("Goodbye")
