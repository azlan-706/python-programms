score_x_y=["6:4","3:4","7:7","8:4","7:6","5:9"]
total_point=0
for i in score_x_y:
    x,y=i.split(":")
    x=int(x)
    y=int(y)
    if x > y:
        total_point+=3
    elif x < y:
        total_point+=0
    elif x==y:
        total_point+=1
print(f"total point of team x is {total_point}")