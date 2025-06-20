from typing import List
from .unit import Unit


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

        for unit_type, quantity in self.INITIAL_UNITS[civilization].items():
            for _ in range(quantity):
                self.units.append(Unit(unit_type))
    
    def get_total_strength(self) -> int:
        return sum(unit.get_strength() for unit in self.units)

    
    def add_gold(self, amount:int):
        self.gold += amount

    def spend_gold(self, amount:int):
        if self.gold < amount:
            raise ValueError(f"Not enough gold in army")
        self.gold -= amount

    def lose_strongest_units(self, n: int = 2):
        self.units.sort(key=lambda u: u.get_strength(), reverse=True)
        self.units= self.units[n:]


    def attack(self, other_army='Army'):
        own_strength = self.get_total_strength()
        enemy_strength = other_army.get_total_strength()

        if own_strength > enemy_strength:
            winner = self
            loser = other_army
            result = "win"
        elif own_strength < enemy_strength:
            winner = other_army
            loser = self
            result = "lose"
        else:
            winner = None
            loser = None
            result = "draw"
        
        if result == "draw":
            self.lose_strongest_units(1)
            other_army.lose_strongest_units(1)
        else:
            loser.lose_strongest_units(2)
            winner.add_gold(100)

        self.battle_history.append(f"Attacked {other_army.civilization} → {result}")
        other_army.battle_history.append(f"Attacked by {self.civilization} → {'lose' if result == 'win' else 'win' if result == 'lose' else 'draw'}")