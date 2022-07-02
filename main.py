import random

CARDS = [_ for _ in range(2, 10)] + ['J', 'Q', 'K', 'A']
random.shuffle(CARDS)


class WrongPlayerChoice(Exception):
    def __init__(self):
        pass


def change_ace_value(deck: list) -> list:
    result_deck = []

    for card in deck:
        if card == 'A':
            card = 2

        result_deck.append(card)

    return result_deck


def get_init_deck():
    init_deck = [
        CARDS.pop()
        for _ in range(2)
    ]

    init_deck_value = get_hand_value(init_deck)

    if init_deck_value > 21:
        init_deck = change_ace_value(init_deck)

    return init_deck


def get_hand_value(hand: list) -> int:
    value = 0

    for card in hand:
        if card == 'J':
            value += 11
        elif card == 'Q':
            value += 12
        elif card == 'K':
            value += 13
        elif card == 'A':
            value += 14
        else:
            value += card

    return value


def check_result(player_hand: list, dealer_hand: list) -> bool:
    player_hand_value = get_hand_value(player_hand)
    dealer_hand_value = get_hand_value(dealer_hand)

    if player_hand_value == 21 and dealer_hand_value != 21:
        print('Players blackjack')
    elif dealer_hand_value == 21 and player_hand_value != 21:
        print('Dealers blackjack')
    elif player_hand_value > 21 and dealer_hand_value < 21:
        print('Dealer win')
    elif dealer_hand_value > 21 and player_hand_value < 21:
        print('Player win')
    elif player_hand_value == 21 and dealer_hand_value == 21 \
            or player_hand_value > 21 and dealer_hand_value > 21:
        print('Draw')
    elif dealer_hand_value > player_hand_value > 17 and dealer_hand_value > 17:
        print('Dealer win')
    else:
        return False

    return True


def hit(hand: list) -> list:
    hand.append(CARDS.pop())

    return hand


def hold(dealer_hand: list, player_hand: list):
    dealer_hand_value = get_hand_value(dealer_hand)
    player_hand_value = get_hand_value(player_hand)

    while dealer_hand_value < 17 or dealer_hand_value <= player_hand_value:
        dealer_hand = hit(dealer_hand)
        dealer_hand_value = get_hand_value(dealer_hand)

    return dealer_hand


def get_player_choice() -> str:
    passed = 0
    player_choice = 0

    while passed == 0:
        try:
            player_choice = input('Your choice:')
            player_choice = str(player_choice)

            player_choice = player_choice.lower()

            if player_choice not in ['h', 's', 'q']:
                raise WrongPlayerChoice

            passed = 1
        except Exception as e:
            print('Error: ', repr(e))

    return player_choice


def print_hands(dealer_hand, player_hand):
    print('P: ', player_hand, '\n' + 'D: ', dealer_hand, '\n')
    print('P: ', get_hand_value(player_hand), '\n' + 'D: ', get_hand_value(dealer_hand), '\n')


def main():
    dealer_hand, player_hand = [], []
    player_hand_value, dealer_hand_value = 22, 22

    while player_hand_value > 21 or dealer_hand_value > 21:
        player_hand = get_init_deck()
        dealer_hand = get_init_deck()

        player_hand_value = get_hand_value(player_hand)
        dealer_hand_value = get_hand_value(dealer_hand)

    print_hands(dealer_hand, player_hand)

    done = check_result(player_hand, dealer_hand)

    while not done:
        player_choice = get_player_choice()

        if player_choice == 'h':
            player_hand = hit(player_hand)
        elif player_choice == 's':
            dealer_hand = hold(dealer_hand, player_hand)

        print_hands(dealer_hand, player_hand)
        done = check_result(player_hand, dealer_hand)


if __name__ == "__main__":
    main()
