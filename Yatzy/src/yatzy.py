from multiprocessing.sharedctypes import Value
from src.pips import *

PAIR = 2

class Yatzy:
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        score = 0
        for score in dice:
            score += dice
        return score

    @staticmethod 
    def yatzy(*dice):
        return 50 if set(dice) == 1 else 0

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(*dice):
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE

    @staticmethod
    def sixes(*dice):
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX

    @staticmethod
    def score_pair(*dice):
        for pip in Pips.values_reversed():
            if dice.count(pip) >= PAIR:
                return pip * PAIR

    @staticmethod
    def two_pair(cls, *dice):
        pip_pair = cls.filter_pips_repeated(dice, PAIR)
        return sum(pip_pair) * PAIR if len(pip_pair) == 2 else 0
        
    @staticmethod
    def three_of_a_kind(cls, *dice):
        for die in dice.count:
            if dice.count(die) >= Pips.THREE.value:
                return die * Pips.THREE
            else: return 0

         

    @staticmethod
    def four_of_a_kind(cls, *dice):
        for die in dice.count:
            if dice.count(die) >= Pips.FOUR.value:
                return die * Pips.FOUR
            else: return 0

    @staticmethod
    def smallStraight(cls, *dice):
        small_straight = list(map(range(Pips.ONE.value, Pips.FIVE.value)))
        if list(dice) == small_straight:
            return sum(small_straight)
        else: 0

    @staticmethod
    def largeStraight(cls, *dice):
        large_straight = list(map(range(Pips.TWO.value, Pips.SIX.value)))
        if list(dice) == large_straight:
            return sum(large_straight)
        else: 0
            

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.two_pair and Yatzy.three_of_a_kind == True:
            return Yatzy.chance(dice)
        else: 0
