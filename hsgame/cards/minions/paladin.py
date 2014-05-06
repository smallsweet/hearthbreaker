import hsgame.targetting
from hsgame.constants import CHARACTER_CLASS, CARD_RARITY, MINION_TYPE
from hsgame.game_objects import MinionCard, Minion, Card
from hsgame.cards.battlecries import change_attack_to_one, give_divine_shield

__author__ = 'Daniel'


class AldorPeacekeeper(MinionCard):
    def __init__(self):
        super().__init__("Aldor Peacekeeper", 3, CHARACTER_CLASS.PALADIN, CARD_RARITY.RARE, True, hsgame.targetting.find_enemy_minion_battlecry_target)

    def create_minion(self, player):
        minion = Minion(3, 3)
        minion.bind("added_to_board", change_attack_to_one)
        return minion
    
class ArgentProtector(MinionCard):
    def __init__(self):
        super().__init__("Argent Protector", 2, CHARACTER_CLASS.PALADIN, CARD_RARITY.COMMON, True, hsgame.targetting.find_friendly_minion_battlecry_target)

    def create_minion(self, player):
        minion = Minion(2, 2)
        minion.bind("added_to_board", give_divine_shield)
        return minion