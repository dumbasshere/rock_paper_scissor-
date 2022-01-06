import random
listCh = ['rock','paper','scissor']
def func():
    pointx=0
    pointy=0
    for i in range(rounds):
        x=input("enter your choice from rock,paper or scissor:")
        y=str(random.choice(listCh))
        if x==y:
            pass
        elif x=='rock' and y=='paper':
            pointy=pointy+1
        elif x=='paper' and y=='rock':
            pointx=pointx+1
        elif x=='rock' and y=='scissor':
            pointx=pointx+1
        elif x=='scissor' and y=='rock':
            pointy=pointy+1
        elif x=='paper' and y=='scissor':
            pointy=pointy+1
        elif x=='scissor' and y=='paper':
            pointx=pointx+1
        else:
            print("wrong input")
        print("computer:")
        print(y)
        print(pointx, pointy)
        


    print("final score:")
    print(pointx, pointy)
    if pointx > pointy :
        print("winner")
    elif pointy> pointx:
        print("better luck next time ")
    else:
        print("tie")
rounds=int(input("how many rounds do you want to play?"))
func()