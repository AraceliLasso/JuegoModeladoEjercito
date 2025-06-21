from typing import List
from .unit import Unit


class Army:
    INITIAL_GOLD=1000

    INITIAL_UNITS = {
        "chinese": {"pikeman":2, "archer": 25, "knight":2},
        "english": {"pikeman":10, "archer": 10, "knight":10},
        "bizantine": {"pikeman":5, "archer": 8, "knight":15},
    }
    def __init__(self, civilization:str, army_name:str):
        if civilization not in self.INITIAL_UNITS:
            raise ValueError(f"Invalid civilization type: {civilization}")

        self.army_name = army_name 
        self.civilization = civilization
        self.gold = self.INITIAL_GOLD
        self.units: List[Unit] = []
        self.battle_history: List[str] = []

        for unit_type, quantity in self.INITIAL_UNITS[civilization].items():
            for _ in range(quantity):
                self.units.append(Unit(unit_type))

    def show_unit_summary(self):
        summary = {"pikeman": 0, "archer": 0, "knight": 0}
        for unit in self.units:
            summary[unit.unit_type] += 1

        print(f"\n Unit summary for {self.army_name} ({self.civilization} civilization):")
        for unit_type in ["pikeman", "archer", "knight"]:
            print(f" - {unit_type.capitalize()}s: {summary[unit_type]}")


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


    def attack(self, other_army: 'Army'):
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

        self.battle_history.append(f"Attacked {other_army.army_name} → {result}")
        other_army.battle_history.append(
            f"Attacked by {self.army_name} → {'lose' if result == 'win' else 'win' if result == 'lose' else 'draw'}"
        )

    def train_unit(self, unit: Unit):
        cost = unit.TRAINING_COSTS[unit.unit_type]
        self.spend_gold(cost)
        unit.train()

    def transform_unit(self, unit: Unit):
        if not unit.can_transform():
            raise ValueError(f"Unit {unit.unit_type} cannot transform")
        new_type = unit.TRANSFORMATION_RELATIONS[unit.unit_type]
        cost = unit.TRANSFORMATION_COSTS[(unit.unit_type, new_type)]
        self.spend_gold(cost)
        unit.transform()

