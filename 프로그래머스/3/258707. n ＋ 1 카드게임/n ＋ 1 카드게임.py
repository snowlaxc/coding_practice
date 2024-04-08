# from collections import deque


def solution(coin, cards):
    len_cards = len(cards)
    max_num = len_cards + 1
    
    hands = cards[:len_cards//3]
    deck = cards[len_cards//3:]
    draw_cards = []
    
    rounds = 1
    
    def draw():
        if deck:
            draw_cards.append(deck.pop(0))
            draw_cards.append(deck.pop(0))
            
    def match(source, target):
        for i in source:
            if max_num - i in target:
                source.remove(i)
                target.remove(max_num - i)
                return True
        return False
        
    while deck:
        draw()
        if match(hands, hands):
            rounds += 1
        elif coin >= 1 and match(hands, draw_cards):
            coin -= 1
            rounds += 1
        elif coin >= 2 and match(draw_cards, draw_cards):
            coin -= 2
            rounds += 1
        else:
            break
            
    return rounds