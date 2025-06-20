from typing import List
from unit import Unit


class Army:
    INITIAL_GOLD=1000

    INITIAL_UNITS = {
        "chinese": {"pikeman":2, "archer": 25, "knight":2},
        "english": {"pikeman":10, "archer": 10, "knight":10},
        "bizantine": {"pikeman":5, "archer": 8, "knight":15},
    }
    def __init__(self, civilization:str):
        if civilization not in self.INITIAL_UNITS:
            raise ValueError(f"Invalid civilization type: {civilization}")
        self.civilization = civilization
        self.gold = self.INITIAL_GOLD
        self.units: List[Unit] = []
        self.battle_history: List[str] = []

        for unit_type in self.INITIAL_UNITS[civilization].items():
            for _ in range(quantity):
                self.units.append(Unit(unit_type))
    def get_total_strength
    def add_gold
    def spend_gold
    def lose_strongest_units
    def attack