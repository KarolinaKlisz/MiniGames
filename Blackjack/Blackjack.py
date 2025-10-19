import random, sys

# cons
HEART = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def get_bet(max_bet):
    while True:
        print("How much do you want to bet? (1-{} or END)".format(max_bet))
        bet = input('> ').upper().strip()
        if bet == 'END':
            print(f"Thanks for your game. You won {max_bet} PLN!")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet

def get_deck():
    deck = []
    for suit in (HEART, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit))
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck

def get_hand_value(cards):
    value = 0
    number_of_aces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value

def display_cards(cards):
    rows = ['', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_{rank.rjust(2, '_')}| '

    for row in rows:
        print(row)


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()

    # dealer
    if show_dealer_hand:
        print("Dealer: ", get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("Dealer: ???")
        display_cards([BACKSIDE] + dealer_hand[1:])

    print()
    # player
    print("Player: ", get_hand_value(player_hand))
    display_cards(player_hand)

def get_move(player_hand, money):
    while True:
        moves = ['(D)raw', '(S)top']

        if len(player_hand) == 2 and money > 0:
            moves.append('(P)lus bet')
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('D', 'S'):
            return move
        if move == 'P' and '(P)lus bet' in moves:
            return move


def main():
    print()
    print("Blackjack Game!\n".center(75))
    print("""\
            Try to get a score as close to 21 as possible, but not over. 
            Kings, Queens, and Jacks are worth 10 points each.
            Aces can be worth either 1 or 11 points.
            Cards from 2 to 10 are worth their face value.
            Press H to draw another card.
            Press S to stop drawing cards.
            During your first round, you can press P to double your bet,
            but you must do it exactly once before you stop drawing cards.
            In case of a tie, the bet amount is returned to the player.
            The dealer stops drawing cards at 17. """)
    print()

    money = 5000

    while True:
        if money <= 0:
            print("You're broke!")
            print("Thanks for the game and your money.")
            sys.exit()

        print("Your budget: ", money)
        print()
        bet = get_bet(money)

        deck = get_deck()

        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # player moves
        print("Your bet: ", bet)
        while True:

            display_hands(player_hand, dealer_hand, False)
            print()
            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)
            if move == 'P':
                additional_bet = get_bet(min(bet, (money-bet)))
                bet += additional_bet
                print(f"Double bet to: {bet}.")
                print(f"Your bet: {bet}.")

            if move in ('D', 'P'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew: {rank}{suit}")
                player_hand.append(new_card)

            if move in ('S', 'P'):
                break

        # dealer moves

        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print("Dealer draws the card...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)
                if get_hand_value(dealer_hand) > 21:
                    break
                print()
                input("Please press Enter, to continue...")
                print("\n\n")

        display_hands(player_hand, dealer_hand, True)
        print()
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print(f"Dealer exceeded 21! You win {bet} PLN!")
            money += bet
        elif(player_value > 21) or (player_value < dealer_value):
            print("You lost.")
            money -= bet
        elif player_value > dealer_value:
            print(f"You won {bet} PLN!")
            money += bet
        elif player_value == dealer_value:
            print("It's a tie! Your bet is returned.")

        print()
        input("Please press Enter, to continue...")
        print("\n\n")


if __name__ == "__main__":
    main()

