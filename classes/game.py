from classes.card import Deck
from classes.player import Player
from utils.scoring import calculate_score, determine_winner

class Game:
    def __init__(self, player_name="Player 1", starting_balance=100):
        self.deck = Deck()  # Колода карт
        self.player = Player(player_name, balance=starting_balance)  # Игрок
        self.dealer = Player("Dealer")  # Дилер
        self.is_game_over = False  # Флаг окончания игры

    def start_game(self):
        print("Welcome to Blackjack!")
        while not self.is_game_over:
            self.play_round()

    def play_round(self):
        # Проверяем количество карт в колоде и баланс игрока
        print(f"\n>> Cards left: {self.deck.remaining_cards()} {self.player.name}: ${self.player.balance} <<")
        
        if self.player.balance < 10:
            print(f"\n{self.player.name} is out of money! Game over.")
            self.is_game_over = True
            return

        # Раздача начальных карт
        self.player.hand.clear()
        self.dealer.hand.clear()

        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

        print(f"\n{self.player.name}'s hand: {self.player.show_hand()} (Score: {self.player.score})")
        print(f"{self.dealer.name}'s hand: {self.dealer.hand[0]} and [Hidden Card]")

        
        # Ход игрока
        self.player_turn()

        # Если у игрока не перебор, дилер делает ход
        if self.player.score <= 21:
            self.dealer_turn()

        # Определение победителя
        self.end_round()

    def player_turn(self):
        while self.player.score < 21:
            action = input("\nDo you want to (h)it or (s)tand? ").lower()
            if action == 'h':
                self.player.add_card(self.deck.deal_card())
                print(f"{self.player.name}'s hand: {self.player.show_hand()} (Score: {self.player.score})")
            elif action == 's':
                break

    def dealer_turn(self):
        while self.dealer.score < 17:
            self.dealer.add_card(self.deck.deal_card())
        print(f"\nDealer's final hand: {self.dealer.show_hand()} (Score: {self.dealer.score})")

    def end_round(self):
        print("\nRound over!")
        result = determine_winner(self.player, self.dealer)
        print(result)

        # Обработка результата:
        if result == f"{self.player.name} wins!":
            if self.player.score == 21 and len(self.player.hand) == 2:
                self.player.balance += 15  # Блэкджек (выигрыш 1.5x ставки)
            else:
                self.player.balance += 10  # Обычная победа
        elif result == f"{self.player.name} busts!" or result == "Dealer wins!":
            self.player.balance -= 10  # Проигрыш игрока
        elif result == "Dealer busts!":
            self.player.balance += 10
        elif result == "It's a draw!":
            pass  # Ничья, баланс не изменяется

        print(f"{self.player.name}'s balance: {self.player.balance}")

        # Если баланс игрока опустился до 0 или ниже, игра заканчивается
        if self.player.balance <= 0:
            print(f"\n{self.player.name} is out of money! Game over.")
            self.is_game_over = True
            return

        # Предлагаем начать новый раунд
        self.ask_for_new_round()



    def ask_for_new_round(self):
        if self.player.balance > 0:
            play_again = input("\nDo you want to play another round? (y/n): ").lower()
            if play_again != 'y':
                self.is_game_over = True
        else:
            self.is_game_over = True
