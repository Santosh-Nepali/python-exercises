class Coins:
    def __init__(self, coin_type, value):
        self.coin_type = coin_type
        self.value = value

    def coin_info(self):
        print(f'The type of coin {self.coin_type} and value {self.value}')


class PiggyBank:
    def __init__(self):
        self.coins = []   # PiggyBank HAS a list of coins (composition)

    def add_coin(self, coin):
        self.coins.append(coin)

    def sum_coins(self):
        total = 0
        for c in self.coins:
            c.coin_info()
            total += c.value
        print(f'Total value: {total}')


x = PiggyBank()
x.add_coin(Coins("regular", 223))
x.add_coin(Coins("special", 500))
x.sum_coins()