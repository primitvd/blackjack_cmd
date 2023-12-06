import  random
set_cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

def give_card():
    return random.choice(set_cards)

def score_check(cards):
    score = 0
    for card in cards:
        if card == "J" or card == "Q" or card == "K":
            score += 10
            print("a",score)
        elif card == "A":
            score += 11
            print("b",score)
        else:
            score += set_cards.index(card) + 1
            print("c",score)
    for card in cards:
        if score > 21 and card == "A":
            score -= 10
    return score


computer = [give_card(),give_card()]
player = [give_card(),give_card()]

print("Your Cards:",player)
print("Computer's first card:",computer[0])

while input("Type y to get another card, type n to pass: ") == "y":
    computer.append(give_card())
    player.append(give_card())
    print("Your Cards:",player)
    print("Computer's first card:",computer[0])
    if score_check(player) > 21:
        print("You lose")
        break

print("Your final hand:",player)
print("Computer's final hand:",computer)

player_score = score_check(player)
computer_score = score_check(computer)

print("Player score:",player_score)
print("Computer Score:",computer_score)

if player_score > 21 or (player_score < computer_score and computer_score <= 21):
    print("You lose")

elif (computer_score < player_score and player_score <= 21) or computer_score > 21:
    print("You win")

else:
    print("Draw")

