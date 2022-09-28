#!/usr/bin/env python3
# shuffle_scorer.py

import numpy as np
import random


def deal_cards(deck):
    hands = np.zeros((4, 4, 13), dtype=int)
    for card_pos, card_num in enumerate(deck):
        hand_num = card_pos % 4
        suit_num = card_num // 13
        rank_num = card_num % 13
        hands[hand_num][suit_num][rank_num] = 1
    return hands


def score_deal(hands):
    score = 0
    for player in range(4):
        # Ideally each player would have 3.25 cards of each suit
        for suit in range(4):
            score += (np.sum(hands[player][suit]) - 3.25) ** 2

        # Ideally each player would have one card of each rank
        for rank in range(13):
            score += (hands[player][0][rank] - 1) ** 2
            score += (hands[player][1][rank] - 1) ** 2
            score += (hands[player][2][rank] - 1) ** 2
            score += (hands[player][3][rank] - 1) ** 2

    return score


def wash_shuffle(deck):
    for card_pos, card_num in enumerate(deck):
        new_card_pos = random.randint(0, 51)
        deck[card_pos] = deck[new_card_pos]
        deck[new_card_pos] = card_num
    return deck


def riffle_shuffle(deck):
    # Cut the deck into two equal halves
    left_pile = deck[:26]
    right_pile = deck[26:]
    # Prepare a new empty deck to hold the riffled halves
    new_deck = np.zeros(0, dtype=int)
    while len(new_deck) < 52:
        # Riffle in a set of cards from the left pile
        chunk = random.randint(1, 4)
        new_deck = np.append(new_deck, left_pile[:chunk])
        left_pile = left_pile[chunk:]
        # Riffle in a set of cards from the right pile
        chunk = random.randint(1, 4)
        new_deck = np.append(new_deck, right_pile[:chunk])
        right_pile = right_pile[chunk:]
    return new_deck


def score_shuffle(shuffle_func, num_deals=10_000):
    total_score = 0
    deck = np.arange(52, dtype=int)
    for _ in range(num_deals):
        deck = shuffle_func(deck)# generates deck using the appropriate function
        total_score += score_deal(deal_cards(deck))#cacl
    return total_score / num_deals


def main():
    random.seed(2016)
    print(f"Wash Shuffle Avg. Score = {score_shuffle(wash_shuffle)}")#calls score shuffle passes in the shuffle we want to use
    print(f"Riffle Shuffle Avg. Score = {score_shuffle(riffle_shuffle)}")


if __name__ == "__main__":
    main()
