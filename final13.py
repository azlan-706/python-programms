import random
computer=random.choice([-1,0,1])
you=input("enter your choice:  ")
dict={"rock":-1,"paper":0,"scissor":1}
reverse={-1:"rock",0:"paper",1:"scissor"}
y_cho=dict[you]
print(f"you chose {reverse[y_cho]}\n computer chose {reverse[computer]}")
if computer==you:
    print("draw")
else:
    if computer==-1 and y_cho==0:
        print("you won")
    elif computer==-1 and y_cho==1:
        print("computer won")
    elif computer==0 and y_cho==-1:
        print("computer won")
    elif computer==0 and y_cho==1:
        print("you won")
    elif computer==1 and y_cho==-1:
        print("you won")
    elif computer==1 and y_cho==0:
        print("computer won")
    else:
        print("something wrong")