'''
A program that simulates the poker dice game. http://en.wikipedia.org/wiki/Poker_dice

Functions:
play(): randomly gives a hand and the dice can be kept by either inputting all or ALL or any current card. Nothing is kept otherwise.
Simulate(): Shows the probability of each type of hand given the number of times played.

Written by Benny Hwang 17/08/2017
'''

from random import randint

def roll_dice(dices):

    dice_list = sorted(dices)
        
    dice_dict = {0:'Ace',1:'King',2:'Queen',3:'Jack',4:'10',5:'9'}

    roll = []
    for d in dice_list:
        roll.append(dice_dict[d])

    print("The roll is: " + str(roll[0]) + " " + str(roll[1]) + " " + str(roll[2]) + " " + str(roll[3]) + " "+ str(roll[4]))

    repeated = []
    num = []
    for i in dice_list:
        if i not in repeated:
            num.append(dice_list.count(i))
            repeated.append(i)

    single = False
    pairs = False
    tri = False
    quad = False
    penta = False

    ones = []
    double = []
    triple = []
    quadriple = []
    pentagon = []
    for i in num:
        if i == 1:
            single = True
            ones.append(i)
        if i == 2:
            pairs = True
            double.append(i)
        if i == 3:
            tri = True
            triple.append(i)
        if i == 4:
            quad = True
            quadriple.append(i)
        if i == 5:
            penta = True
            pentagon.append(i)

    if single:
        if len(ones) == 5:
            if dice_list == list(range(min(dice_list),max(dice_list)+1)):
                print("It is a Straight")
            else:
                print("It is a Bust")

    if pairs:
        if len(double) == 1 and tri == False:
            print("It is a One pair")
        if len(double) == 2:
            print("It is a Two pair")

    if tri:
        if pairs == False:
            print("It is a Three of a kind")
        if pairs == True:
            print("It is a Full house")

    if penta:
        print("It is a Five of a kind")
        
    if quad:
        print("It is a Four of a kind")

    return roll

def roll_dice2(dices):

    dice_list = sorted(dices)
        
    dice_dict = {0:'Ace',1:'King',2:'Queen',3:'Jack',4:'10',5:'9'}

    roll = []
    for d in dice_list:
        roll.append(dice_dict[d])

    repeated = []
    num = []
    for i in dice_list:
        if i not in repeated:
            num.append(dice_list.count(i))
            repeated.append(i)

    single = False
    pairs = False
    tri = False
    quad = False
    penta = False

    FiveOfaKind = 0
    FourOfaKind = 0
    FullHouse = 0
    Straight = 0
    ThreeOfaKind = 0
    Two_pair = 0
    One_pair = 0
    Bust = 0

    ones = []
    double = []
    triple = []
    quadriple = []
    pentagon = []
    for i in num:
        if i == 1:
            single = True
            ones.append(i)
        if i == 2:
            pairs = True
            double.append(i)
        if i == 3:
            tri = True
            triple.append(i)
        if i == 4:
            quad = True
            quadriple.append(i)
        if i == 5:
            penta = True
            pentagon.append(i)

    if single:
        if len(ones) == 5:
            if dice_list == list(range(min(dice_list),max(dice_list)+1)):
                Straight += 1
            else:
                Bust += 1

    if pairs:
        if len(double) == 1 and tri == False:
            One_pair += 1
        if len(double) == 2:
            Two_pair += 1

    if tri:
        if pairs == False:
            ThreeOfaKind += 1
        if pairs == True:
            FullHouse += 1

    if penta:
        FiveOfaKind += 1
        
    if quad:
        FourOfaKind += 1
	
    return tuple([roll,FiveOfaKind,FourOfaKind,FullHouse,Straight,ThreeOfaKind,Two_pair,One_pair,Bust])

def play():

    get_out = False
    rN = 2

    dice1 = randint(0,5)
    dice2 = randint(0,5)
    dice3 = randint(0,5)
    dice4 = randint(0,5)
    dice5 = randint(0,5)

    dices = [dice1,dice2,dice3,dice4,dice5]

    while get_out == False:

        roll = roll_dice(dices)
        
        num_dict = {2:'second', 3:'third'}

        if rN >3:
            break
        
        roll_num = num_dict[rN]
        rN += 1

        roll_copy = roll.copy()
        #print(roll_copy)
        To_use = []
        valid = False
        
        while valid == False:
            user_input = input('Which dice do you want to keep for the ' +str(roll_num) + ' roll? ')
            if user_input == 'all' or user_input == 'All':
                print('Ok, done.')
                get_out = True
                break
            else:
                in_list = user_input.split(' ')
                #print(in_list)
                valid = True
                for i in in_list:
                    #print(i)
                    if i != '' and i not in roll_copy:
                        if valid == True:
                            print('That is not possible, try again!')
                            valid = False
                            roll_copy = roll.copy()
                            To_use = []
                    elif i in roll_copy:
                        roll_copy.remove(i)
                        #print(roll_copy)
                        To_use.append(i)
                        #print(To_use)
                        if len(To_use) == 5:
                            print('Ok, done.')
                            get_out = True
                            break
                            
        if get_out == False:
            reverse_dice_dict = {'Ace':0,'King':1,'Queen':2,'Jack':3,'10':4,'9':5}
            hold_dice = []
            for i in To_use:
                dice_num = reverse_dice_dict[i]
                hold_dice.append(dice_num)

            while len(hold_dice)<5:
                hold_dice.append(randint(0,5))

            dices = hold_dice

    return

def simulate(n):

    reverse_dice_dict = {'Ace':0,'King':1,'Queen':2,'Jack':3,'10':4,'9':5}

    FiveOfaKind = 0
    FourOfaKind = 0
    FullHouse = 0
    Straight = 0
    ThreeOfaKind = 0
    Two_pair = 0
    One_pair = 0
    Bust = 0
    
    x = 1
    
    while x <= n:

        dice1 = randint(0,5)
        dice2 = randint(0,5)
        dice3 = randint(0,5)
        dice4 = randint(0,5)
        dice5 = randint(0,5)

        dices = [dice1,dice2,dice3,dice4,dice5]
		
        result = roll_dice2(dices)

        
    
        FiveOfaKind = FiveOfaKind + result[1]
        FourOfaKind = FourOfaKind + result[2]
        FullHouse = FullHouse + result[3]
        Straight = Straight + result[4]
        ThreeOfaKind = ThreeOfaKind + result[5]
        Two_pair = Two_pair + result[6]
        One_pair = One_pair + result[7]
        Bust = Bust + result[8]

        x+=1

    Total = FiveOfaKind+FourOfaKind+FullHouse+Straight+ThreeOfaKind+Two_pair+One_pair+Bust

    print('Five of a kind : ' + str('%.2f' % (100*FiveOfaKind/Total))+'%')
    print('Four of a kind : ' + str('%.2f' % (100*FourOfaKind/Total))+'%')
    print('Full house     : ' + str('%.2f' % (100*FullHouse/Total))+'%')
    print('Straight       : ' + str('%.2f' % (100*Straight/Total))+'%')
    print('Three of a kind: ' + str('%.2f' % (100*ThreeOfaKind/Total))+'%')
    print('Two pair       : ' + str('%.2f' % (100*Two_pair/Total))+'%')
    print('One pair       : ' + str('%.2f' % (100*One_pair/Total))+'%')

    return


