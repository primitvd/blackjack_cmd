import  random

def give_card():
    cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    return random.choice(cards)

def score_check(cards):
    score = 0
    for card in cards:
        if card == "J" or cards == "Q" or cards == "K":
            score += 10
        if card == "A":
            score += 11
        else:
            score += cards.index(card) + 1
    if score > 21 and "A" in cards:
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

print("Your final hand:",player)
print("Computer's final hand:",computer)

player_score = score_check(player)
computer_score = score_check(computer)

if player_score > 21 or player_score < computer_score:
    print("You lose")

elif computer_score < player_score and player_score <= 21:
    print("You win")

else:
    print("Draw")

