File="History.txt"


def show_history():
    file = open(File,'r')
    lines = file.readlines()
    if len(lines)==0:
        print("no calculation history")
    else:
        for line in lines:
            print(line.strip())
        print("\n--------------------------------\n")
    file.close()


def clear_history():
    file=open(File,'w')
    file.close()


def save_history(equ,result):
    file=open(File,'a')
    file.write(f"{equ} = {result} \n")
    file.close()


def calculate(user_input):
    user_input=input("enter the operation(ex: 5+2):")

    parts=user_input.split()

    if len(parts) != 3:
            print("invalid input")
            return

    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op=="+":
        result= num1+num2

    elif op=="-":
        result= num1-num2

    elif op=="*":
        result= num1*num2

    elif op=="/":
        if num2==0:
            print("cannot devide by 0 !")
            return
        else:
            result=num1/num2

    else:
        print("invalid oprator...! try among (+,-,*,/)")

    if result.is_integer():
        result=int(result)
    print(f"{num1} {op} {num2} = {result}\n\n")

    save_history(user_input,result)

def main():
    print("calculate and save the  history of calculation")

    while (True):
        print("1 for calculate\n2 for exit \n3 for clear \n4 for history")
        task=int(input("enter the number to perform corresponding task (1, 2, 3, 4): "))

        if task==1:
            calculate("user_input")

        elif task==2:
            print("exiting the program...")
            break

        elif task==3:
            clear_history()

        elif task==4:
            show_history()

        else:
            print("invalid task...!")

main()










