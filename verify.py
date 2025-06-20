from models.army import Army

if __name__ == "__main__":
    #! Crea dos ejércitos
    army1 = Army("chinese")
    army2 = Army("english")

    print("\n🔍 Number of units before battle:")
    print("Chinese:", len(army1.units))  # debería ser 29
    print("English:", len(army2.units))  # debería ser 30

    print("china initial strength:", army1.get_total_strength())
    print("english initial strength:", army2.get_total_strength())
    # Deberia resultar en:
    # Fuerza inicial de chinese: 300
    # Fuerza inicial de english: 350

    #! Simula una batalla
    army1.attack(army2)

    print("\n🏁 After the battle:")
    print("chinese strength:", army1.get_total_strength())
    print("english strength:", army2.get_total_strength())
    print("china gold:", army1.gold)
    print("english gold:", army2.gold)

    print("\n📜 Battle history:")
    print("Chinese:", army1.battle_history)
    print("English:", army2.battle_history)

    print("\n🔎 Number of units after battle:")
    print("Chinese:", len(army1.units))
    print("English:", len(army2.units))
