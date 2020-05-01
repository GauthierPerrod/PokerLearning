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
    return(sorted(l, reverse=True))

def find_pairs(hand):
    l=[]
    values=list(map(get_value,hand))
    for val in values :
        if values.count(val)==2:
            l.append(val)
    return(l)

def find_triplet(hand):
    l=[]
    values=list(map(get_value,hand))
    for val in values :
        if values.count(val)==3:
            l.append(val)
    return(l)

def find_four_of_a_kind(hand):
    l=[]
    values=list(map(get_value,hand))
    for val in values :
        if values.count(val)==4:
            l.append(val)
    return(l)

def find_color(hand):
    colors=list(map(get_color,hand))
    l=[]
    for col in colors :
        if colors.count(col)>=5:
            for index in range(len(hand)):
                if hand[index].color == col:
                    l.append(hand[index])
            return(find_best(l))

def find_straight(hand):
    l=[]
    values=list(map(get_value,hand))
    values=list(set(sorted(values)))
    print(values)
    if 13 in values :
        values=[0]+values
    for i in range(len(values) - 4):
        if values[i]+4==values[i+4]:
            l.append(values[i+4])
    return(max(l))

if __name__ == '__main__':

    card1 = card.Card('Ace', 'Spades')
    card2 = card.Card('Two', 'Spades')
    card3 = card.Card('Three', 'Spades')
    card4 = card.Card('Four', 'Spades')
    card5 = card.Card('Five', 'Spades')
    card6 = card.Card('Queen', 'Spades')
    card7 = card.Card('Two', 'Clubs')
    hand = [card6, card2, card3, card4, card5, card1, card7]
    print(find_color(hand))
    print(find_straight(hand))
    print(find_pairs(hand))
    print(find_triplet(hand))
    print(find_four_of_a_kind(hand))