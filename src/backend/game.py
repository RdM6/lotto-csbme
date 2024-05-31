import random


class GameWinningNumbers:
    def __init__(self, winning_numbers: str, winning_super_number: int):
        self.winning_numbers = winning_numbers
        self.winning_super_number = winning_super_number

    @staticmethod
    def create_winning_numbers():
        winning_numbers = repr(random.sample(range(50), 6))
        return winning_numbers

    @staticmethod
    def create_winning_super_number():
        winning_super_number = random.randint(0, 10)
        return winning_super_number
