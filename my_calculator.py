first_num=input("Enter your first number \t")
second_num=input("Enter your second number \t")
first_num_int=int(first_num)
second_num_int=int(second_num)
choose_option=input("Enter the type of operation you want(add,subtract,multiply,divide,all).Press enter to exit ! \t")
my_option=choose_option.lower()
print(choose_option.lower())
if (my_option=="add"):
    print(first_num_int+second_num_int)
elif(my_option=="subtract"):
    if (first_num_int>=second_num_int):
     print(first_num_int - second_num_int)
    else :
     print(second_num_int - first_num_int)
elif(my_option=="multiply"):
    print(first_num_int * second_num_int)
elif(my_option=="divide"):
    if (first_num_int >= second_num_int):
        print(first_num_int / second_num_int)
    else:
        print(second_num_int / first_num_int)
elif(my_option==""):
    print("Good Bye")
else:
    print("Please choose operation from one of the options and try again. Press enter to exit ! \t")