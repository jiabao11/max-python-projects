print("="*20)
print("hello, this is RSM calculator")
print("="*20)

while True:
    equation=input("Enter your problem:")
    print(eval(equation))
    going=input("keep going?(y/n)")
    if going=="y":
        continue
    else:
        break