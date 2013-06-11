answer = raw_input("Answer is : ")
right = 0
fault = 0
if answer == 1:
    right = right + 1
elif answer == 2:
    fault = fault + 1
elif answer == 0:
    print("Right: " + right)
    print("Fault: " + fault)

