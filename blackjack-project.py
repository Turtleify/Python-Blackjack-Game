import random

face_cards = ['Jack', 'Queen', 'King']
ace_card = ['Ace']
suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
values = list(range(2, 11))
card_pool = values + face_cards + ace_card

total_funds = 10000


def deal_card():
    card = [random.choice(card_pool), random.choice(suits)]
    if card[0] in face_cards:
        card[0] = 10
    return card


def hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        if card[0] == 'Ace':
            aces += 1
            total += 11 
        else:
            total += card[0]

    while total > 21 and aces:
        total -= 10 
        aces -= 1

    return total


def dealer_cards():
    dealer_hand = [deal_card(), deal_card()]
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    return dealer_hand


def player_cards():
    player_hand = [deal_card(), deal_card()]
    for card in player_hand:
        if card[0] == 'Ace':
            ace_value = int(input("You got an Ace! Would you like it to be 1 or 11? "))
            card[0] = ace_value
    return player_hand


def play():
    global total_funds

    print(f"You have ${total_funds}.")

    while True:
        try:
            money_bet = int(input("How much money would you like to bet? "))
            if money_bet > total_funds:
                print("You can't bet more money than you have!")
            elif money_bet > 0:
                print(f"Betting ${money_bet}. Good luck!")
                break
            else:
                print("Please bet a positive amount.")
        except ValueError:
            print("Invalid input. Enter a number.")

    total_funds -= money_bet

    player_hand = player_cards()
    dealer_hand = dealer_cards()

    print(f"Your cards: {player_hand}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    while True:
        player_value = hand_value(player_hand)
        print(f"Your total is: {player_value}")

        if player_value > 21:
            print("Bust! You lose.")
            return
        elif player_value == 21:
            print("Blackjack! You win double your bet!")
            total_funds += money_bet * 2
            return

        next_move = input("Do you want to 'hit' or 'stay'? ").lower()
        if next_move == 'hit':
            player_hand.append(deal_card())
            print(f"Your new hand: {player_hand}")
        elif next_move == 'stay':
            break
        else:
            print("Invalid input. Please type 'hit' or 'stay'.")

    print(f"Dealer's cards: {dealer_hand}")
    dealer_value = hand_value(dealer_hand)
    print(f"Dealer's total: {dealer_value}")

    player_value = hand_value(player_hand)
    if dealer_value > 21 or player_value > dealer_value:
        if player_value == 21:
            print("You won! Exactly 21 gives you 2x your money")
            total_funds += money_bet * 2
        else:
            print("You win! You get 1.5x your bet.")
            total_funds += money_bet * 1.5
    elif player_value == dealer_value:
        print("It's a tie")
        total_funds += money_bet
    else:
        print("Dealer wins. Ur a dummy")

    print(f"Your total funds: ${total_funds}")


def start():
    global total_funds
    while total_funds > 0:
        play_again = input("Do you want to play Blackjack? (y/n): ").lower()
        if play_again == 'y':
            play()
        elif play_again == 'n':
            print("See ya!")
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")

    if total_funds <= 0:
        print("You ran out of money. Stupid loser boy lmao")



start()
