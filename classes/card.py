import random

# Класс для представления карты
class Card:
    def __init__(self, suit, rank, value):
        # Сопоставляем масти с символами
        self.suits = {
            'Hearts': '❤️',
            'Diamonds': '♦️',
            'Clubs': '♣️',
            'Spades': '♠️'
        }
        self.suit = self.suits.get(suit, suit)  # Заменяем масть на символ
        self.rank = rank  # Ранг: 2-10, J, Q, K, A
        self.value = value  # Очки карты

    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = self.create_deck()
        random.shuffle(self.cards)

    def create_deck(self):
        """Создает колоду с заданным количеством колод."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                  '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

        deck = []
        for _ in range(self.num_decks):
            for suit in suits:
                for rank in ranks:
                    deck.append(Card(suit, rank, values[rank]))
        return deck

    def deal_card(self):
        """Выдает карту из колоды, если колода не пуста, иначе перегенерирует новую колоду."""
        if len(self.cards) == 0:
            print("\nКолода закончилась! Перегенерируем новую колоду...")
            self.cards = self.create_deck()
            random.shuffle(self.cards)
        
        return self.cards.pop()

    def remaining_cards(self):
        """Возвращает количество оставшихся карт в колоде."""
        return len(self.cards)
