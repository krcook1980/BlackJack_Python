import random


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return(card)

def play():
    input("Are you ready to play?")
    total = 0
    hand = []
    dealer = []
    cardD = deal()
    dealer.append(cardD)
    dTotal = cardD

    keep_going = True

    while keep_going:
        cardP = deal()
        hand.append(cardP)
        total += cardP

        if total == 21:
            print(f"{hand} Black Jack!")
            keep_going = False
            play()

        elif total > 21:
            if 11 in hand and sum(hand) > 21:
                hand.remove(11)
                hand.append(1)
            else:
                keep_going = False
                print(f"Total {total}, you bust")
                play()
        
        else:
            print(f"Dealer has a {dealer[0]}, you have {hand}. Current score: {total}")
        
        if input("Do you want to hit or stay? ").lower() == "hit":
            keep_going = True
        else:
            while dTotal < 17:
                cardD = deal()
                dealer.append(cardD)
                dTotal += cardD
                print(f"Dealer has {dTotal}")
            
            if dTotal <= 21 and total <= 21:
                if dTotal == total:
                    print(f"Dealer has {dTotal}, you have {total} - it's a draw")
                elif dTotal < total:
                    print(f"Dealer has {dTotal}, you have {total} - you win!")
                else:
                    print(f"Dealer has {dTotal}, you have {total} - you lose.")
            keep_going = False
            play()

play()


