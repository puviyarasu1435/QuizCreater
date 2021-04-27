
print ("Hi....you reset the quiz\n")
print("how many quiz you want (max 20)")
limit=int(input())
def store(value):
    file = open("QuizCreater/quiz.txt","w")
    file.write(value)
    print(value)
    file.close
list=[]
for i in range(limit):
    print (f"Enter the quiz number {i+1}")
    quiz=input()
    list.append([quiz])
    for j in range(5):
        print (f"Enter the chosse number {j+1}")
        Value=input()
        list[i].append(Value)
    print(list[i])
    print("Enter the answer(1,2,3,4,5) use number\n")
    try:
        ans=int(input())
    except ValueError or TypeError:
        print("pls enter only number")
        ans=int(input())
    list[i].append(ans)

store(f"Quizlist={list}")





    
   
    