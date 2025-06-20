from datetime import datetime

class Unit:
    BASE_STRENGTH={
        "pikeman":5,
        "archer":10,
        "knight":20
    }
    TRAINING_BENEFITS={
        "pikeman":3,
        "archer":7,
        "knight":10
    }
    TRAINING_COSTS={
        "pikeman":10,
        "archer":20,
        "knight":30
    }
    TRANSFORMATION_COSTS={
        ("pikeman","archer"):30,
        ("archer", "knight"):40
    }
    TRANSFORMATION_RELATIONS={
        "pikeman":"archer",
        "archer":"knight",
        "knight":None
    }
    def __init__(self, unit_type:str):
        if unit_type not in self.BASE_STRENGTH:
            raise ValueError(f"Invalid unit type: {unit_type}")
        self.unit_type=unit_type
        self.base_strength=self.BASE_STRENGTH[unit_type]
        self.extra_strength = 0
        self.creation_date=datetime.now()
    
    def get_strength(self) -> int:
        return self.base_strength + self.extra_strength
    
    def get_years_lived(self) -> int:
        time = datetime.now() - self.creation_date
        return time.days

    def train(self, army_gold: int) -> int:
        cost = self.TRAINING_COSTS[self.unit_type]
        if army_gold < cost:
            raise ValueError("Not enough gold to train unit")
        self.extra_strength += self.TRAINING_BENEFITS[self.unit_type]
        return army_gold - cost
    
    def can_transform(self) -> bool:
        return self.TRANSFORMATION_RELATIONS[self.unit_type] is not None
    
    def transform(self, army_gold:int):
        
        if not self.can_transform():
            raise ValueError(f"{self.unit_type} cannot be transformed further")
        new_type = self.TRANSFORMATION_RELATIONS[self.unit_type]
        cost = self.TRANSFORMATION_COSTS[(self.unit_type, new_type)]
        if army_gold < cost:
            raise ValueError("Not enough gold to transform unit")
        self.unit_type = new_type
        self.base_strength = self.BASE_STRENGTH[new_type]
        self.extra_strength = 0
        return army_gold - cost
