# Подсчет очков игрока
def calculate_score(hand):
    score = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == 'A')
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def determine_winner(player, dealer):
    if player.score > 21:
        return f"{player.name} busts!"
    elif dealer.score > 21:
        return "Dealer busts!"
    elif player.score > dealer.score:
        return f"{player.name} wins!"
    elif player.score < dealer.score:
        return "Dealer wins!"
    else:
        return "It's a draw!"
