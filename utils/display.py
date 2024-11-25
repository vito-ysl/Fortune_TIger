class Display:
    def show_balance(self, balance):
        print(f"\nSeu saldo atual: ${balance}")

    def show_reels(self, reels):
        print(f"| {' | '.join(reels)} |")

    def goodbye(self, balance):
        print(f"\nVocê terminou o jogo com ${balance}. Obrigado por jogar Fortune Tiger! 🎲")
