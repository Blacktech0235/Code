#BlackJack
import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values_D = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
values_P = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
Initial=100
while Initial>1:
    p1=0
    a1=int(input("Enter The Bid Amount "))
    if(a1==0):
        print("Your Final Winnings=",Initial)
        break
    Dealer_Suit=suits[random.randint(0,3)]
    Dealer_Rank=ranks[random.randint(0,12)]
    if(Dealer_Rank=='A'):
        values_D['A']=int(input("What Value Of Dealer's A Will You Take? "))
    print("Dealer=",Dealer_Rank,"Of",Dealer_Suit)
    d1=values_D[Dealer_Rank]
    for i in range(2):
        Player_Suit=suits[random.randint(0,3)]
        Player_Rank=ranks[random.randint(0,12)]
        if(Player_Rank=='A'):
            values_P['A']=int(input("What Value Of Player's A Will You Take? "))
        print("You=",Player_Rank,"Of",Player_Suit)
        p1+=values_P[Player_Rank]
    while(1>0):
        f=input("Would You Like More Cards? ")
        if(f=='yes'):
            Player_Suit=suits[random.randint(0,3)]
            Player_Rank=ranks[random.randint(0,12)]
            if(Player_Rank=='A'):
                values_P['A']=int(input("What Value Of Player's A Will You Take? "))
            print("You=",Player_Rank,"Of",Player_Suit)
            p1+=values_P[Player_Rank]
            if(p1>21):
                print("Bust!")
                break 
        elif(f=='no'):
            break 
    a1+=int(input("Would You Like To Increase Your Bid? (Give Number Value) "))
    Initial=Initial-a1
    Dealer_Suit=suits[random.randint(0,3)]
    Dealer_Rank=ranks[random.randint(0,12)]
    if(Dealer_Rank=='A'):
        values_D['A']=int(input("What Value Of Dealer's A Will You Take? "))
    d1+=values_D[Dealer_Rank]
    print("Dealer=",Dealer_Rank,"Of",Dealer_Suit)
    while(d1<17):
        if(d1<17):
            while(d1<17):
                Dealer_Suit=suits[random.randint(0,3)]
                Dealer_Rank=ranks[random.randint(0,12)]
                if(Dealer_Rank=='A'):
                    values_D['A']=int(input("What Value Of Dealer's A Will You Take? "))
                print("Dealer=",Dealer_Rank,"Of",Dealer_Suit)
                d1+=values_D[Dealer_Rank]
    if(d1>21):
        print("Dealer Bust!,You Win!")
        Initial=Initial+(a1*2)
    elif(p1>21):
        print("You Lost!")
    elif(d1==p1):
        print("Its a tie ")
        Initial+=a1
    elif(d1==21):
        print("You Lost!")
    elif(p1==21):
        print("You Won!")
        Initial=Initial+(a1*2)
    elif(d1>p1):
        print("You Lost!")
    elif(p1>d1):
        print("You Won!")
        Initial=Initial+(a1*2)
    print("Your Balance=",Initial)