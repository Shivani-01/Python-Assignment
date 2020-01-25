import random
class Card:   
    def __init__(self,face,suit,value):
        self.face=face
        self.suit=suit
        self.value=value
        
    def __str__(self):
        return f'{self.face} {self.suit} {self.value}'

class Deck:
    def __init__(self):
        a=''
    def shuffle(self,l):
        a=random.shuffle(l)
    def next_card(self):
        a=random.choice(l)
        print(a)
        return a
    def return_cards(self):
        return l
    def addCard(self,l,c):
        l.append(c)  

class Hand:
    def __init__(self):
        self.b=''
        self.l=l
        self.tv=0
 
    def drawn_from(self,hc,d):        
        self.b=d.next_card()
        hc.append(self.b)
        l.remove(self.b)
        self.tv=int(self.b.split()[2])
        return self.tv
    def return_to(self,hc):
        l.append(self.b)
        hc.remove(self.b)
        self.tv=int(self.b.split()[2])
        return self.tv

class Player:
    def __init__(self,credit):
        self.name=input("Enter your name")
        self.credit=credit
        self.hc=[]
    def play(self):
        return(int(input("Do you want to play? Enter 1 for yes and 0 for no")))
    def show_hand(self,h):
        print("Hands in your card",h)
    def stand(self):
        pass

class Game:
    def __init__(self,pname):
        self.player=pname
        self.w=0
    def play(self,n,d,s,h,u):
        c=0
        while c!=n:
            print(self.player[c].name,"turn")
            d.shuffle(l)
            s[c]+=h.drawn_from(self.player[c].hc,d)
            if(int(input("Do you want to replace it in deck? Enter 1 or 0"))):
                s[c]-=h.return_to(self.player[c].hc)     
                self.player[c].show_hand(self.player[c].hc)
                print("Your total score",s[c])
                if s[c]>21:
                    print(self.player[c].name," won")
                    u[c]+=1
                    tv=0
                    return -1
            else:
                self.player[c].show_hand(self.player[c].hc)
                print("Your total score",s[c])
                if s[c]>21:
                    print(self.player[c].name," won")
                    u[c]+=1
                    tv=0
                    self.w=-1
                    return -1
                c+=1
        i=s.index(max(s))
        print(self.player[i].name," won")
             
    def get_bust_probab(self,u,n,p):
        a=sum(u)
        for i in range(n):
            print("Probability of winning of ",self.player[i].name," is ",u[i]/a)
            self.player[i].hc.clear()
            
    
        
        

pname=[]                                                                        #Store object of players
n=int(input("Enter number of players "))
u=[0]*(n+1)                                                                     #Store how many times a player wins
                                                                             
for _ in range(n):
    p=Player(0)
    pname.append(p)
d=Deck()
g=Game(pname)
while(int(input("Do you want to play? Enter 1/0"))):
    l=[]                
    d=Deck()
    h=Hand()
    for i in ['Club','Diamond','Spade','Heart']:
        for j in range(2,11):
            c=Card('No',i,j)
            d.addCard(l,c.__str__())
    for i in ['Club','Diamond','Spade','Heart']:
        for j in ['Jack','Queen','King','Ace']:
            if j=='Ace':
                v=1
            elif j=='King':
                v=13
            elif j=='Queen':
                v=12
            else:
                v=11
            c=Card(j,i,v)
            d.addCard(l,c.__str__())

    s=[0]*(n+1)                                                                     #Stores score of a player                   
    for i in range(10):
        a=g.play(n,d,s,h,u)
        if a==-1:
            break
    g.get_bust_probab(u,n,p)
    
    
