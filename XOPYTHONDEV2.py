def prntarr(array):
    print("                                  ")
    print(array[0][0],"   ",array[0][1],"   ",array[0][2])
    print("                                  ")
    print(array[1][0],"   ",array[1][1],"   ",array[1][2])
    print("                                  ")
    print(array[2][0],"   ",array[2][1],"   ",array[2][2])
    print("                                  ")
print("this is an XO game ! \nyou need 3Xs beside each other for P1 and 3Os for P2 \nenter 1 to choose playing against another player : \nenter 2  to choose playing against the computer player : ")
q=int(input())
if q==2 :
    print("instructions")
    print("player1 is x and computer is o")
    print("you will take turns and all you need to do is to enter the number of box you choosed ")
    print("ENJOY ! !")
    print("                ")
    print("|     |     |     |")
    print("|  1  |  2  |  3  |")
    print("|     |     |     |")
    print("------------------")
    print("|     |     |     |")
    print("|  4  |  5  |  6  |")
    print("|     |     |     |")
    print("------------------")
    print("|     |     |     |")
    print("|  7  |  8  |  9  |")
    print("|     |     |     |")
    x=int(0)
    y=int(0)
    a=int(0)
    b=int(0)
    z=int(0)
    array = [["-","-","-"],["-","-","-"],["-","-","-"]]
    while(z<5):
        o=int(input("p1 : enter the number of the box : "))
        x=int()
        y=int()
        e=int(0)
        for e in range (0,10):
            if o > int(9) or o < int(1):
                print ("choose correct place (1:9)")
                o=int(input("p1 : enter the number of the box : "))
            if o < int(10) and o > int(0):
                break
        if o == 1:
            x=0
            y=0
        elif o == 2:
            x=0
            y=1
        elif o == 3:
            x=0
            y=2
        elif o == 4:
            x=1
            y=0
        elif o == 5:
            x=1
            y=1
        elif o == 6:
            x=1
            y=2
        elif o == 7:
            x=2
            y=0
        elif o == 8:
            x=2
            y=1
        elif o == 9:
            x=2
            y=2
        e=int(0)
        for e in range (0,10):
            if(array[x][y]!="-"):
                print("box is taken ! choose another box")
                o=int(input("p1 : enter the number of the box : "))
                if o == 1:
                    x=0
                    y=0
                elif o == 2:
                    x=0
                    y=1
                elif o == 3:
                    x=0
                    y=2
                elif o == 4:
                    x=1
                    y=0
                elif o == 5:
                    x=1
                    y=1
                elif o == 6:
                    x=1
                    y=2
                elif o == 7:
                    x=2
                    y=0
                elif o == 8:
                    x=2
                    y=1
                elif o == 9:
                    x=2
                    y=2
            if(array[x][y]=="-"):
                break
           
        array[x][y]= "x"
        prntarr(array)
        m=int(0)
        for m in range (0,3):
            n=int(0)
            if (array[m][n]==array[m][n+1] and array[m][n]==array[m][n+2] and array[m][n]== "x"):
                print("p1 wins ! ")
                z=int(10)
                break
            elif (array[n][m]==array[n+1][m] and array[n][m]==array[n+2][m] and array[n][m]== "x"):
                print("p1 wins ! ")
                z=int(10)
                break
            elif (array[0][0]==array[1][1] and array[0][0]==array[2][2] and array[0][0]== "x"):
                print("p1 wins ! ")
                z=int(10)
                break
            elif (array[0][2]==array[1][1] and array[1][1]==array[2][0] and array[1][1]=="x"):
                print("p1 wins ! ")
                z=int(10)
                break
            m = m+1
        if (z==10):
            break
        if (z==4):
            print("Draw !")
            break
#---------------------------
        
        nobe=int(0)
        s=int(0)
        for s in range (0,3):
            v=int(0)
            if (array[s][v]==array[s][v+1] and array[s][v]=="o" and array[s][v+2]== "-"):
                array[s][v+2]="o"
                nobe = int(1)
                break
            elif (array[s][v]=="-"and array[s][v+1] == array[s][v+2] and array[s][v+2]== "o"):
                array[s][v]="o"
                nobe = int(1)
                break
            elif (array[s][v]== array[s][v+2] == array[s][v+2]== "o" and array[s][v+1]== "-"):
                array[s][v+1]="o"
                nobe = int(1)
                break
            elif (array[v][s]==array[v+1][s] and array[v][s]=="o" and array[v+2][s]== "-"):
                array[v+2][s]="o"
                nobe = int(1)
                break
            elif (array[v+1][s]==array[v+2][s] and array[v+1][s]=="o" and array[v][s]== "-"):
                array[v][s]="o"
                nobe = int(1)
                break
            elif (array[v][s]==array[v+2][s] and array[v][s]=="o" and array[v+1][s]== "-"):
                array[v+1][s]="o"
                nobe = int(1)
                break
            elif (array[0][0]==array[1][1] and array[0][0]=="o" and array[2][2]== "-"):
                array[2][2]="o"
                nobe = int(1)
                break
            elif (array[0][0]==array[2][2] and array[0][0]=="o" and array[1][1]== "-"):
                array[1][1]="o"
                nobe = int(1)
                break
            elif (array[1][1]==array[2][2] and array[1][1]=="o" and array[0][0]== "-"):
                array[0][0]="o"
                nobe = int(1)
                break
            elif (array[0][2]==array[1][1] and array[1][1]=="o" and array[2][0]=="-"):
                array[2][0]="o"
                nobe = int(1)
                break
            elif (array[0][2]==array[2][0] and array[1][1]=="o" and array[1][1]=="-"):
                array[1][1]="o"
                nobe = int(1)
                break
            elif (array[2][0]==array[1][1] and array[1][1]=="o" and array[0][2]=="-"):
                array[0][2]="o"
                nobe = int(1)
                break
            s=s+1
        no=int(0)
        if nobe == 0 :
            m=int(0)
            for m in range (0,3):
                n=int(0)
                if (array[m][n]==array[m][n+1] and array[m][n]=="x" and array[m][n+2]== "-"):
                    array[m][n+2]="o"
                    no=int(1)
                    break
                elif (array[m][n]=="-"and array[m][n+1] == array[m][n+2] and array[m][n+2]== "x"):
                    array[m][n]="o"
                    no=int(1)
                    break
                elif (array[m][n]== array[m][n+2] == array[m][n+2]== "x" and array[m][n+1]== "-"):
                    array[m][n+1]="o"
                    no=int(1)
                    break
                elif (array[n][m]==array[n+1][m] and array[n][m]=="x" and array[n+2][m]== "-"):
                    array[n+2][m]="o"
                    no=int(1)
                    break
                elif (array[n+1][m]==array[n+2][m] and array[n+1][m]=="x" and array[n][m]== "-"):
                    array[n][m]="o"
                    no=int(1)
                    break
                elif (array[n][m]==array[n+2][m] and array[n][m]=="x" and array[n+1][m]== "-"):
                    array[n+1][m]="o"
                    no=int(1)
                    break
                elif (array[0][0]==array[1][1] and array[0][0]=="x" and array[2][2]== "-"):
                    array[2][2]="o"
                    no=int(1)
                    break
                elif (array[0][0]==array[2][2] and array[0][0]=="x" and array[1][1]== "-"):
                    array[1][1]="o"
                    no=int(1)
                    break
                elif (array[1][1]==array[2][2] and array[1][1]=="x" and array[0][0]== "-"):
                    array[0][0]="o"
                    no=int(1)
                    break
                elif (array[0][2]==array[1][1] and array[1][1]=="x" and array[2][0]=="-"):
                    array[2][0]="o"
                    no=int(1)
                    break
                elif (array[0][2]==array[2][0] and array[1][1]=="x" and array[1][1]=="-"):
                    array[1][1]="o"
                    no=int(1)
                    break
                elif (array[2][0]==array[1][1] and array[1][1]=="x" and array[0][2]=="-"):
                    array[0][2]="o"
                    no=int(1)
                    break
                m = m+1
        never = int(0)
        if nobe == 0 :
            if no == 0 :
                t=int(0)
                for t in range (0,3):
                    r=int(0)
                    if (array[t][r]=="o" and array[t][r+1]== "-" and array[t][r+2]== "-" ):
                        array[t][r+2]="o"
                        never = int(1)
                        break
                    elif (array[t][r+1]=="o" and array[t][r+2] == "-" and array[t][r]== "-"  ):
                        array[t][r]="o"
                        never = int(1)
                        break
                    elif (array[t][r+1]=="o"and array[t][r]== "-" and array[t][r+2]== "-"  ):
                        array[t][r]="o"
                        never = int(1)
                        break
                    elif (array[t][r+2]=="o"and array[t][r+1] =="-" and array[t][r]== "-" ):
                        array[t][r+1]="o"
                        never = int(1)
                        break
                    elif (array[r][t]=="o" and array[r+1][t]== "-" and array[r+2][t]== "-" ):
                        array[r+1][t]="o"
                        never = int(1)
                        break
                    elif (array[r+1][t]=="o"and array[r+2][t] =="-" and array[r][t]== "-" ):
                        array[r+2][t]="o"
                        never = int(1)
                        break
                    elif (array[r+1][t]=="o" and array[r][t]== "-" and array[r+2][t]== "-"):
                        array[r][t]="o"
                        never = int(1)
                        break
                    elif (array[r+2][t]=="o"and array[r+1][t] =="-"and array[r][t]== "-" ):
                        array[r+1][t]="o"
                        never = int(1)
                        break
                    elif (array[0][0]=="o" and array[1][1]=="-" and array[2][2]=="-" ):
                        array[1][1]="o"
                        never = int(1)
                        break
                    elif (array[1][1]=="o" and array[2][2]=="-" and array[0][0]=="-" ):
                        array[2][2]="o"
                        never = int(1)
                        break
                    elif (array[2][2]=="o" and array[1][1]=="-" and array[0][0]=="-" ):
                        array[1][1]="o"
                        never = int(1)
                        break
                    elif (array[1][1]=="o" and array[0][0]=="-"and array[2][2]=="-"):
                        array[0][0]="o"
                        never = int(1)
                        break
                    elif (array[0][2]=="o" and array[1][1]=="-" ):
                        array[1][1]="o"
                        never = int(1)
                        break
                    elif (array[1][1]=="o" and array[2][0]=="-"  and array[0][2]=="-"):
                        array[2][0]="o"
                        never = int(1)
                        break
                    elif (array[2][0]=="o" and array[1][1]=="-" and array[0][2]=="-" ):
                        array[1][1]="o"
                        never = int(1)
                        break
                    elif (array[1][1]=="o" and array[0][2]=="-" and array[2][0]=="-"):
                        array[0][2]="o"
                        never = int(1)
                        break
                    t=t+1
        none=int(0)
        if z == 0 :
            if (array[0][0]=="x" or array[0][2]=="x" or array[2][2]=="x" or array[2][0]=="x"):
                array[1][1]="o"
                none=int(1)
        if no == 0 :
            if nobe == 0 :
                if never == 0 :
                    if none == 0 :
                        from random import (randint)
                        f=int(0)
                        for f in range (0,50):
                            x=randint(0,2)
                            y=randint(0,2)
                            if array[x][y]== "-" :
                                array[x][y]= "o"
                                break
                            f=f+1
                        
                        
        
        prntarr(array)
        m=int(0)
        for m in range (0,3):
            if (array[m][n]==array[m][n+1] and array[m][n]==array[m][n+2] and array[m][n]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            elif (array[n][m]==array[n+1][m] and array[n+1][m]==array[n+2][m] and array[n][m]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            elif (array[0][0]==array[1][1] and array[0][0]==array[2][2] and array[0][0]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            elif (array[0][2]==array[1][1] and array[1][1]==array[2][0] and array[1][1]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            m=m+1
        z=z+1


#----------------------------------------------------------------


elif q==1 :
    print("instructions \nplayer1 is x and player2 is o \nyou will take turns and all you need to do is to enter the number of box you choosed \nENJOY ! !\n")
    print("|     |     |     |")
    print("|  1  |  2  |  3  |")
    print("|     |     |     |")
    print("------------------")
    print("|     |     |     |")
    print("|  4  |  5  |  6  |")
    print("|     |     |     |")
    print("------------------")
    print("|     |     |     |")
    print("|  7  |  8  |  9  |")
    print("|     |     |     |")
    x=int(0)
    y=int(0)
    a=int(0)
    b=int(0)
    z=int(0)
    array = [["-","-","-"],["-","-","-"],["-","-","-"]]
    while(z<5):
        o=int(input("p1 : enter the number of the box : "))
        x=int()
        y=int()
        e=int(0)
        for e in range (0,50):
            if o > int(9) or o < int(1):
                print ("choose correct place (1:9)")
                o=int(input("p1 : enter the number of the box : "))
            if o < int(10) and o > int(0):
                break
        if o == 1:
            x=0
            y=0
        elif o == 2:
            x=0
            y=1
        elif o == 3:
            x=0
            y=2
        elif o == 4:
            x=1
            y=0
        elif o == 5:
            x=1
            y=1
        elif o == 6:
            x=1
            y=2
        elif o == 7:
            x=2
            y=0
        elif o == 8:
            x=2
            y=1
        elif o == 9:
            x=2
            y=2
        e=int(0)
        for e in range (0,50):
            if(array[x][y]!="-"):
                print("box is taken ! choose another box")
                o=int(input("p1 : enter the number of the box : "))
                if o == 1:
                    x=0
                    y=0
                elif o == 2:
                    x=0
                    y=1
                elif o == 3:
                    x=0
                    y=2
                elif o == 4:
                    x=1
                    y=0
                elif o == 5:
                    x=1
                    y=1
                elif o == 6:
                    x=1
                    y=2
                elif o == 7:
                    x=2
                    y=0
                elif o == 8:
                    x=2
                    y=1
                elif o == 9:
                    x=2
                    y=2
            if(array[x][y]=="-"):
                break
        array[x][y]= "x"
        prntarr(array)
        m=int(0)
        for m in range (0,3):
            n=int(0)
            if (array[m][n]==array[m][n+1] and array[m][n]==array[m][n+2] and array[m][n]== "x"):
                print("p1 wins ! ")
                z=int(10)
                break
            elif (array[n][m]==array[n+1][m] and array[n][m]==array[n+2][m] and array[n][m]== "x"):
                print("p1 wins ! ")
                z=int(10)
                break
            elif (array[0][0]==array[1][1] and array[0][0]==array[2][2] and array[0][0]== "x"):
                print("p1 wins ! ")
                z=int(10)
                break
            elif (array[0][2]==array[1][1] and array[1][1]==array[2][0] and array[1][1]=="x"):
                print("p1 wins ! ")
                z=int(10)
                break
            m = m+1
        if (z==10):
            break
        if (z==4):
            print("Draw !")
            break
        o=int(input("p2 : enter the number of the box : "))
        a=int()
        b=int()
        e=int(0)
        for e in range (0,10):
            if o > int(9) or o < int(1):
                print ("choose correct place (1:9)")
                o=int(input("p2 : enter the number of the box : "))
            if o < int(10) and o > int(0):
                break
        if o == 1:
            a=0
            b=0
        elif o == 2:
            a=0
            b=1
        elif o == 3:
            a=0
            b=2
        elif o == 4:
            a=1
            b=0
        elif o == 5:
            a=1
            b=1
        elif o == 6:
            a=1
            b=2
        elif o == 7:
            a=2
            b=0
        elif o == 8:
            a=2
            b=1
        elif o == 9:
            a=2
            b=2
        e=int(0)
        for e in range (0,10):
            if(array[a][b]!="-"):
                print("box is taken ! choose another box")
                o=int(input("p2 : enter the number of the box : "))
                if o == 1:
                    a=0
                    b=0
                elif o == 2:
                    a=0
                    b=1
                elif o == 3:
                    a=0
                    b=2
                elif o == 4:
                    a=1
                    b=0
                elif o == 5:
                    a=1
                    b=1
                elif o == 6:
                    a=1
                    b=2
                elif o == 7:
                    a=2
                    b=0
                elif o == 8:
                    a=2
                    b=1
                elif o == 9:
                    a=2
                    b=2
            if(array[a][b]=="-"):
                break
        array[a][b]= "o"
        prntarr(array)
        m=int(0)
        for m in range (0,3):
            if (array[m][n]==array[m][n+1] and array[m][n]==array[m][n+2] and array[m][n]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            elif (array[n][m]==array[n+1][m] and array[n+1][m]==array[n+2][m] and array[n][m]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            elif (array[0][0]==array[1][1] and array[0][0]==array[2][2] and array[0][0]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            elif (array[0][2]==array[1][1] and array[1][1]==array[2][0] and array[1][1]== "o"):
                print("p2 wins ! ")
                z=int(10)
                break
            m=m+1
        z=z+1
