from toServer import send

def cam(y):
    if y>0:
        print(1)
        send("camUp=1")
    elif y==0:
        print(0)
        send("camStale=1")
    else:
        print(-1)
        send("camDown=1")
    
        