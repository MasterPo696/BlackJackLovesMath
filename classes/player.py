class Player:
    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance  # Баланс игрока
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        self.update_score()

    def update_score(self):
        self.score = sum(card.value for card in self.hand)
        # Корректировка для туза (если сумма больше 21, меняем туза с 11 на 1)
        aces = sum(1 for card in self.hand if card.rank == 'A')
        while self.score > 21 and aces > 0:
            self.score -= 10
            aces -= 1

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)
