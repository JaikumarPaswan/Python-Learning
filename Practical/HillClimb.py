SuccList ={ 'A':[['B',3],['C',2]], 'B':[['D',2],['E',3]], 'C':[['F',2],['G',4]], 'D':[['H',1],['I',99]],'F': [['J',1]]
,'G':[['K',99],['L',3]]}
Start='A'

Closed = list()
SUCCESS=True
FAILURE=False

def MOVEGEN(N):
    New_list=list()
    if N in SuccList.keys():
        New_list=SuccList[N]
    return New_list

def SORT(L):
    L.sort(key = lambda x: x[1])
    return L    

def heu(Node): 
    if Node == []:
        return 0
    else:
        return Node[1]

def APPEND(L1,L2):
    New_list=list(L1)+list(L2)
    return New_list

def Hill_Climbing(Start):
    global Closed
    N=Start
    CHILD = MOVEGEN(N)
    SORT(CHILD)
    N=[Start,5]
    print("\nStart=",N)
    print("Sorted Child List=",CHILD)
    newNode=CHILD[0]
    CLOSED=[N]

    while (heu(newNode) <= heu(N)) and (len(CHILD) !=0):
        print("\n--------------------------")
        N= newNode
        print("N=",N)
        CLOSED = APPEND(CLOSED,[N])
        CHILD = MOVEGEN(N[0])
        SORT(CHILD)
        print("Sorted Child List=",CHILD)
        print("CLOSED=",CLOSED)
        if CHILD == []:
            newNode=CHILD
        else:
            newNode=CHILD[0]

    Closed=CLOSED
Hill_Climbing(Start)