import time
from game.reel import Reel
from player.player import Player
from utils.display import Display

class SlotMachineGame:
    def __init__(self):
        self.reel = Reel()
        self.player = Player()
        self.display = Display()
        self.spin_cost = 10
        self.jackpot = 500
        self.small_prize = 50

    def start(self):
        while self.player.balance > 0:
            self.display.show_balance(self.player.balance)
            play = input("Pressione Enter para girar (ou digite 'sair' para encerrar): ").strip().lower()
            
            if play == "sair":
                self.display.goodbye(self.player.balance)
                break

            if self.player.balance < self.spin_cost:
                print("Saldo insuficiente para girar. Jogo encerrado!")
                break

            self.player.balance -= self.spin_cost
            self.spin()

    def spin(self):
        print("\nGirando os rolos...")
        time.sleep(1)
        result = self.reel.spin_reels()
        self.display.show_reels(result)
        
        # Verificar combinações
        if len(set(result)) == 1:  # Todos os símbolos iguais
            print("🎉 JACKPOT! Você ganhou $500! 🎉")
            self.player.balance += self.jackpot
        elif len(set(result)) == 2:  # Dois símbolos iguais
            print("🎁 Parabéns! Você ganhou $50! 🎁")
            self.player.balance += self.small_prize
        else:
            print("💔 Melhor sorte na próxima vez!")
