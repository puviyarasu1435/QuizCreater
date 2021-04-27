file = open("QuizCreater/quiz.txt","r")
Qui=file.read()
exec(Qui)
file.close()
number=1
score=0
try:
    for i in range(len(Quizlist)):
        print(f"{i}) {(Quizlist[i][0])} ?")
        for j in range(1,6):
            print(f"   {number}) {Quizlist[i][j]} \n")
            number+=1
        try:
            print("Enter the chosse number")
            ans=int(input())
        except ValueError or TypeError:
            print("pls Enter the choose number")
            ans=int(input())
        number=0
        if ans==Quizlist[i][6]:
            score+=10
            print(f"You are score is {score}")
except NameError:
    print("!!!pls Reset the quiz!!!")
