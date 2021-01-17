noeud=0
def switchPlayer(currenPlayer):
    if currenPlayer==1:
        return 2;
    else:
        return 1;

def action(state):
    moves=[]

    for i in range(0,len(state)):
        move=[];
        number=state[i]
        if number !=1 and number !=2: 
            for j in range(0,i):
                move.append(state[j])
            for k in range(1,int(number/2)+1): 
                aux=move.copy()
                if(number-k!=k) :
                    move.append(k);
                    move.append(number-k);
                    for j in range(i+1, len(state)):
                        move.append(state[j])
                    moves.append(move);
                    move=aux
    return moves

def terminalTest(state): 
    for n in state:
        if n!=1 and n!=2:
            return 0
    return 1

def maxValue(state):
    global noeud
    if terminalTest(state)==1:
        return 0
    v=-1;   
    for s in action(state):
        noeud=noeud+1
        v=max(v,minValue(s))
        if v==1:
            break
    return v

def minValue(state):
    global noeud
    if terminalTest(state)==1:
        return 1
    v=2;   
    for s in action(state):
        noeud=noeud+1
        v=min(v,maxValue(s))
        if v==0:
            break
    return v

def humanPlay(state):
    print("**** your turn ******")
    print(" your possibles moves :")
    moves=action(state)
    index=0
    for item in moves :
        print(index,". ",item)
        index+=1
    i=input("What is your move :  ")
    return(moves[int(i)].copy())

def computerPlay(state):
    print("**** computer turn ******")
    print("the computer plays")
    moves=action(state)
    index=0
    for item in moves :
        min=minValue(item);
        if min == 0:
            return item;
    return moves[0].copy()

def play(state,player):
    if player==1:
       return humanPlay(state)
    else:
       return computerPlay(state)

player=1
state=[7];
noeud = 0 ;
n=input("nbr de jetons :  ")
state=[int(n)]
while 1 :
    state=play(state,player)
    print(state)
    if terminalTest(state)==1:
        break
    player=switchPlayer(player);

    state=play(state,player)
    print(state)
    if terminalTest(state)==1:
        break
    player=switchPlayer(player);
print ("game is over");
if (player==1):
    print("you won !!")
else:
    print("the computer won !!")
print("noeud=",noeud+1)