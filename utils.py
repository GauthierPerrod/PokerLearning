''' fonctions usefull'''
import card #for debuging purpose

str_to_value = {'Ace':13, 'Two': 1, 'Three': 2, 'Four': 3, 'Five': 4, 'Six': 5, 'Seven': 6, 'Eight': 7, 'Nine': 8, 'Ten': 9, 'Jack': 10, 'Queen': 11, 'King': 12}
value_to_str = {v: k for k, v in str_to_value.items()}

def get_value(card):
    return(str_to_value[card.value])

def get_color(card):
    return(card.color)

def find_best(hand):
    l=[]
    values=list(map(get_value,hand))
    for val in values:
        l.append(val)
    return(sorted(l, reverse=True)) #return list in descending order for higher card

def find_pairs(hand):
    l=[]
    values=list(map(get_value,hand))
    for val in values :
        if values.count(val)==2:
            l.append(val)
    return(sorted(l, reverse=True)) #return list sorted in descending order for all pairs found

def find_triplet(hand):
    l=[]
    values=list(map(get_value,hand))
    for val in values :
        if values.count(val)==3:
            l.append(val)
    return(sorted(l, reverse=True)) #return list sorted in descending order for all triplets found

def find_four(hand):
    l=[]
    values=list(map(get_value,hand))
    for val in values :
        if values.count(val)==4:
            l.append(val)
    return(l)

def find_color(hand):
    colors=list(map(get_color,hand))
    new_hand = []
    for col in colors :
        if colors.count(col)==5:
            for card in hand :
                if card.color==col :
                    new_hand.append(card)
            return(find_best(new_hand))
    return(find_best(new_hand))

def find_straight(hand): #function to find the straight (hand here is a list of objects card)
    l=[]
    values=list(map(get_value,hand))
    values=list(set(sorted(values)))
    if 13 in values :
        values=[0]+values
    if (len(values) - 4) >= 0: #condition on at least 4 unique values in hand to avoid list index out of range (e.g: four of a kind + pair = 3 unique values in hand)
        for i in range(len(values) - 4):
            if values[i]+4==values[i+4]:
                l.append(values[i+4])
        if len(l) > 0:
            return([max(l)]) #return list of highest card in the straight
        else:
            return([])

def find_straight_flush(hand): #special function in the event of a straight flush (hand here is the output of find_color, a list of int)
    l=[]
    values=list(set(sorted(hand)))
    if 13 in values :
        values=[0]+values
    if (len(values) - 4) >= 0: #condition on at least 4 unique values in hand to avoid list index out of range (e.g: four of a kind + pair = 3 unique values in hand)
        for i in range(len(values) - 4):
            if values[i]+4==values[i+4]:
                l.append(values[i+4])
        if len(l) > 0:
            return([max(l)]) #return list of highest card in the straight
        else:
            return([])


if __name__ == '__main__':
    card0 = card.Card('Ace', 'Hearts')
    card1 = card.Card('King', 'Hearts')
    card2 = card.Card('Queen', 'Hearts')
    card3 = card.Card('Jack', 'Hearts')
    card4 = card.Card('Ten', 'Spades')
    card5 = card.Card('Nine', 'Spades')
    card6 = card.Card('Eight', 'Spades')
    hand = [card0, card1, card2, card3, card4, card5, card6]
    print(len(find_color(hand)))
    print(find_straight(hand))
    print(len(find_pairs(hand)))
