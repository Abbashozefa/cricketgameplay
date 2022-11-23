import random

print("************LETS BEGIN THE GAME*************")

s_for_user=int()
s_for_comp=int()


a = int()
b = int()
over = int(input("ENTER THE NUMBER OF OVERS "))
numberofballs = 6 * over
print("LET'S DO THE TOSS FIRST ************** TOSS YOUR COIN*********PRESS 1 OR 0")
coin = int(input("************HEADS OR  TAILS***********"))


def userplay(sum_for_user):
    print("*********YOU ARE BATTING NOW*******")
    for i in range(1, numberofballs + 1):
        a = int(input("ENTER NUMBER  "))
        b = random.randint(1, 9)
        print("Computer enters",b)
        if (a == b and i == 1):
            sum_for_user = 1
            break
        elif (a == b):
            print("YOU ARE OUT ")
            print("TOTAL SCORE OF USER =", sum_for_user + 1)
            break
        elif(s_for_comp!=0 and sum_for_user > s_for_comp):
            break


        else:
            sum_for_user = sum_for_user + a
        print("CURRENT SCORE =", sum_for_user)
    return sum_for_user


def compplay(sum_for_comp):
    print("**********COMP IS BATTING NOW*********")
    for i in range(1, numberofballs + 1):
        a = int(input("ENTER NUMBER  "))
        b = random.randint(1, 9)
        print("Computer enters",b)
        if (a == b and i == 1):
            sum_for_comp = 1

            break

        elif (a == b):
            print("COMPUTER IS OUT  ")
            print("TOTAL SCORE OF COMPUTER=", sum_for_comp + 1)
            break
        elif(s_for_user!=0 and s_for_user < sum_for_comp):
            break
        else:
            sum_for_comp = sum_for_comp + b
        print("CURRENT SCORE =", sum_for_comp)
    return sum_for_comp


if (coin == random.randint(0, 1)):
    s_for_comp=compplay(0)
    s_for_user=userplay(0)
else:
    s_for_user=userplay(0)
    s_for_comp=compplay(0)
print(s_for_user)
print(s_for_comp)

if (s_for_user > s_for_comp):
    print("************YOU HAVE WON THE GAME*************")
else:
    print('????????????\YOU LOSE THE GAME????????????')
