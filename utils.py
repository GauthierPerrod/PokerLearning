''' fonctions usefull'''
import card #for debuging purpose

str_to_value = {'Ace':13, 'Two': 1, 'Three': 2, 'Four': 3, 'Five': 4, 'Six': 5, 'Seven': 6, 'Eight': 7, 'Nine': 8, 'Ten': 9, 'Jack': 10, 'Queen': 11, 'King': 12]
value_to_str = {v: k for k, v in str_to_value.items()}

def get_value(card):
    return(card.value)

def get_color(card):
    return(card.color)

def find_best(hand):
    l=[]
    values=list(map(get_value,hand))
    for j in values:
        l.append(str_to_value[j])
    return(sorted(l, reverse=True))

def find_pairs(hand):
    l=[]
    values=list(map(get_value,hand))
    for j in values :
        if values.count(j)==2:
            l.append(j)
    return(l)

def find_triplet(hand):
    l=[]
    values=list(map(get_value,hand))
    for j in values :
        if values.count(j)==3:
            l.append(j)
    return(l)

def find_color(hand):
    col=list(map(get_color,hand))
    for col in colors :
        if colors.count(col)==5:
            return(find_best(hand))

'''def find_straight(hand):
    l=[]
    values=list(map(get_value,hand))
    values=list(set(sorted(values)))
    for i in range(len(values)-5):
        if values[i]%13==(values[i+4]-4)%13'''
        



