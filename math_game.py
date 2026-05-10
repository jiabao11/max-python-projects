import random
questions=20
number_1=list(range(1,questions))
number_2=list(range(1,questions))
lives=3
equation=None
attempt=None
answer=None
score=0
print("Welcome to my math game!")
print(" \"+\" means addition,\"-\" means subtraction,\"*\" means multiplication.")
print("Go!")
i=1
while not score==questions :
    selector=random.randint(0,3)
    list1=random.randint(0,len(number_1)-1)
    list2=random.randint(0,len(number_2)-1)
    num1=number_1[list1]
    num2=number_2[list2]
    if selector==0:
        print(f"Question {i}")
        print(str(num1)+"+"+ str(num2))
        answer=num1+num2
    elif selector==1:
        print(f"Question {i}")
        print(str(num1)+"-"+str(num2))
        answer=num1-num2
    else:
        print(f"Question {i}")
        print(str(num1)+"*"+str(num2))
        answer=num1*num2
    i=i+1
    try:
        attempt=round(int(input("Answer:")))
    except ValueError:
        print("Please enter a number!")
        print("You lost a life!")
        lives=lives-1
        print(f"You now have {lives} lives.")
        continue
    if attempt==answer:
        score=score+1
        print(f"Correct! You now solved {score} questions.")
        continue
    else:
        lives=lives-1
        questions=questions+1
        print("You lost a life!")
        print(f"You now have {lives} lives.")
        if lives==0:
            print("Game over! Out of lives.")
            print(f"You have solved {score} questions")
            break
        else:
            continue
if not lives==0:
    print("Congrats! You won!")
    print(f"You have {lives} lives remaining.")