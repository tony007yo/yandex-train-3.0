from collections import deque

class Queue:    
    def __init__(self) -> None:
        self.deque = deque()

    def push(self, n):
        self.deque.append(int(n))
        
    def pop(self):
        if len(self.deque) > 0:
            return self.deque.popleft()
        return None

    def is_empty(self):
        return len(self.deque) == 0


def game(cards_first, cards_second):
    first_card = cards_first.pop()
    second_card = cards_second.pop()
    is_first_winner = None 
    result = [first_card, second_card]
    
    if (first_card == 0 and second_card == 9) or (second_card == 0 and first_card == 9):
        if first_card < second_card:
            is_first_winner = True
        else:
            is_first_winner = False
    else:
        if first_card < second_card:
            is_first_winner = False
        else:
            is_first_winner = True
    
    if is_first_winner:
        for card in result:
            cards_first.push(card)
    else:
        for card in result:
            cards_second.push(card)


if __name__ == '__main__':
    with open('input.txt', 'r') as f_in:
        cards = deque(
            line.rstrip()
            for line in f_in.readlines()
        )
    
    cards_first = Queue()
    cards_second = Queue()

    for card in cards[0].split():
        cards_first.push(int(card))
    for card in cards[1].split():
        cards_second.push(int(card))
    i = 1
    answer = "botva"
    while i!= 10**6:
        game(cards_first, cards_second)
        if cards_first.is_empty():
            answer = f"second {i}"
            break
        if cards_second.is_empty():
            answer = f"first {i}"
            break
        i += 1
    print(answer)