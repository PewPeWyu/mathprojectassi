import random


# Ask the user how many questions do they want to answer
numQuestion=int(input("How many questions would you like to answer, monsieur?"))
# Ask the user what the lowest number is
numlow=int(input("What is the lowest number?"))
low=1
# Ask the user what the highest number is
numhigh=int(input("What is the highest number?"))
high=10
# Ask them which operation they want: 1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide
numoperation=int(input("press 1 if addition, press 2 if substraction, press 3 if multiplication, and press 4 if division:"))
# Loop:
u = 0
for question in range(1,numQuestion+1):
    # print(f"Question {question}:")
    #     question1=random.randint(low,high)
    # - Pick two random numbers, ask the user a question
    if numoperation == 1:
            num1 = random.randint(low, high)
            num2 = random.randint(low, high)
            ans = num1 + num2
            print(f"Question: {num1} + {num2} = ?")
            userAns = int(input())
            if userAns == ans:
                print(f"Correct!\ncontinue doing questions\n")
                u=u+1
            else:
                print(f"Wrong!", ans)

    elif numoperation == 2:
            num1 = random.randint(low, high)
            num2 = random.randint(low, high)
            ans = num1 - num2
            print(f"Question: {num1} - {num2} = ?")
            userAns = int(input())
            if userAns == ans:
                print(f"Correct!\ncontinue doing questions\n")
                u=u+1
            else:
                print(f"Wrong!", ans)

    elif numoperation == 3:
            num1 = random.randint(low, high)
            num2 = random.randint(low, high)
            ans = num1 * num2
            print(f"Question: {num1} * {num2} = ?")
            userAns = int(input())
            if userAns == ans:
                print(f"Correct!\ncontinue doing questions\n")
                u=u+1
            else:
                print(f"Wrong!", ans)


    elif numoperation == 4:
            num1 = random.randint(low, high)
            num2 = random.randint(low, high)
            num1 = num1 * num2
            ans = num1 // num2
            print(f"Question: {num1} / {num2} = ?")
            userAns = int(input())
            if userAns == ans:
                print(f"Correct!\ncontinue doing questions\n")
                u=u+1
            else:
                print(f"Wrong!", ans)


# - If they are right, give them a point
# - If they are wrong, show them the correct answer

# After the loop, print out their score
print(f"You got {u} correct!")