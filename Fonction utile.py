def dict_to_list(L):
    L_res = []
    
    for i in L:
        for j in i:
            L_res.append(j)
    return L_res



from time import *

def chronometre(sec):
    for i in range(0,sec+1):
        print(i)
        sleep(1)
    print('STOP')
    return 1
