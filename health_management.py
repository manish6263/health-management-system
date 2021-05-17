#............HEALTH MANAGEMENT SYSTEM............

import datetime
def gettime():
    return datetime.datetime.now()

def take(b):
    if b==1:
        c=int(input("ENTER 1 FOR EXERSCISE AND 2 FOR FOOD: "))
        if c==1:
            value=input("ENTER YOUR EXERSCISE HERE\n")
            with open("shubham-ex.txt","a") as f:
                f.write(str([str(gettime())])+":  "+value+"\n")
                print("SUCCESSFULLY WRITTEN\n")
        elif c==2:
            value=input("ENTER YOUR FOOD HERE\n")
            with open("shubham-food.txt","a") as f:
                f.write(str([str(gettime())])+":  "+value+"\n")
                print("SUCCESSFULLY WRITTEN\n")   
        else:
            print("ENTER VALID INPUT 1(EXERSCISE) AND 2(FOOD)")
    elif b==2:
        c=int(input("ENTER 1 FOR EXERSCISE AND 2 FOR FOOD: "))
        if c==1:
            value=input("ENTER YOUR EXERSCISE HERE\n")
            with open("satish-ex.txt","a") as f:
                f.write(str([str(gettime())])+":  "+value+"\n")
                print("SUCCESSFULLY WRITTEN\n")
        elif c==2:
            value=input("ENTER YOUR FOOD HERE\n")
            with open("satish-food.txt","a") as f:
                f.write(str([str(gettime())])+":  "+value+"\n")
                print("SUCCESSFULLY WRITTEN\n")   
        else:
            print("ENTER VALID INPUT 1(EXERSCISE) AND 2(FOOD)")                     
    elif b==3:
        c=int(input("ENTER 1 FOR EXERSCISE AND 2 FOR FOOD: "))
        if c==1:
            value=input("ENTER YOUR EXERSCISE HERE\n")
            with open("manish-ex.txt","a") as f:
                f.write(str([str(gettime())])+":  "+value+"\n")
                print("SUCCESSFULLY WRITTEN\n")
        elif c==2:
            value=input("ENTER YOUR FOOD HERE\n")
            with open("manish-food.txt","a") as f:
                f.write(str([str(gettime())])+":  "+value+"\n")
                print("SUCCESSFULLY WRITTEN\n")   
        else:
            print("ENTER VALID INPUT 1(EXERSCISE) AND 2(FOOD)")        
    else:
        print("ENTER VALID INPUT 1(SHUBHAM), 2(SATISH) AND 3(MANISH)")
def retrieve(r):
    if r==1:
        c=int(input("ENTER 1 FOR EXERSCISE AND 2 FOR FOOD: "))
        if c==1:
            with open("shubham-ex.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif c==2:
            with open("shubham-food.txt") as f:
                for i in f:
                    print(i,end=" ")
        else:
            print("ENTER VALID INPUT 1(EXERSCISE) AND 2(FOOD)")
    elif r==2:
        c=int(input("ENTER 1 FOR EXERSCISE AND 2 FOR FOOD: "))
        if c==1:
            with open("satish-ex.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif c==2:
            with open("satish-food.txt") as f:
                for i in f:
                    print(i,end=" ")
        else:
            print("ENTER VALID INPUT 1(EXERSCISE) AND 2(FOOD)")
    elif r==3:
        c=int(input("ENTER 1 FOR EXERSCISE AND 2 FOR FOOD: "))
        if c==1:
            with open("manish-ex.txt") as f:
                for i in f:
                    print(i,end=" ")
        elif c==2:
            with open("manish-food.txt") as f:
                for i in f:
                    print(i,end=" ")
        else:
            print("ENTER VALID INPUT 1(EXERSCISE) AND 2(FOOD)")

print("......HEALTH MANAGEMENT SYSTEM.......")
a=int(input("ENTER 1 FOR LOG THE VALUE AND ENTER 2 FOR RETRIEVE THE VALUE: "))
if a==1:
    b=int(input("ENTER 1 FOR SHUBHAM, 2 FOR SATISH AND 3 FOR MANISH: "))
    take(b)
elif a==2:
    b=int(input("ENTER 1 FOR SHUBHAM, 2 FOR SATISH AND 3 FOR MANISH: "))
    retrieve(b)
else:
    print("ENTER VALID NUMBER 1(LOG THE VALUE) AND 2(RETRIEVE THE VALUE)")