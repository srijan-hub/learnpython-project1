x= input("Enter values sep by commas: ").split(",")

def add():
    sum=0
    for e in x:
        sum = sum+ int(e)
    return sum
my_sum=add()
print(my_sum)

def multiply():
    multiple=1
    for e in x:
        multiple = multiple* int(e)
    return multiple
my_mul=multiply()
print(my_mul)

def subtract():
    sub=0
    for e in x:
       sub = sub* int(e)
    return sub
my_sub=subtract()
print(my_sub)

def divide():
    div=1
    for e in x:
        div = div* int(e)
    return div
my_div=divide()
print(my_div)
