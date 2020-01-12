#simple calculator - Python
#Mohamad Darwiche

def handleAdd(x,y):
    return x+y

def handleSub(x,y):
    return x-y

def handleDiv(x,y):
    return x/y

def handleMult(x,y):
    return x*y

def displayChoices():
    print("1-Addition")
    print("2-Subtraction")
    print("3-Division")
    print("4-Multiplication")
    print("5-Quit")

def handleChoice(ch,x,y):
    if(ch==1):
        print("Adding ", x ,"+", y, "gives you",handleAdd(x,y))
    elif(ch==2):
        print("Subtracting " , x , "-" , y , "gives you" , handleSub(x, y))
    elif (ch == 3):
        print("Dividing " , x , "/" , y , "gives you" , handleDiv(x, y))
    elif (ch == 4):
        print("Multiplying " , x , "*" , y , "gives you" , handleMult(x, y))
    elif (ch == 5):
        print("Quitting...")
    else:
        print("invalid input")

def main():
    print("this is the main function")

    choice=1
    while(choice != 5):
        print("\n Please select an option ")
        displayChoices()
        inp = input("your choice >> ")
        choice = int(inp)
        if(choice==5):
            break
        inp=input("enter the first number >> ")
        num1=int(inp) #because input is a string and i need to convert to a number
        inp = input("enter the second number >> ")
        num2 = int(inp)  # because input is a string and i need to convert to a number
        handleChoice(choice,num1,num2)

    print("Thank you for using simple calculator!")

if __name__=='__main__':
    main()