from models.army import Army

if __name__ == "__main__":
    # Crea dos ejércitos
    army1 = Army("chinese")
    army2 = Army("english")

    print("Fuerza inicial de chinese:", army1.get_total_strength())
    print("Fuerza inicial de english:", army2.get_total_strength())

    # Simula una batalla
    # army1.attack(army2)

    # print("\n🏁 Después de la batalla:")
    # print("Fuerza de chinese:", army1.get_total_strength())
    # print("Fuerza de english:", army2.get_total_strength())
    # print("Oro de chinese:", army1.gold)
    # print("Oro de english:", army2.gold)

    # print("\n📜 Historial de batallas:")
    # print("Chinese:", army1.battle_history)
    # print("English:", army2.battle_history)

    # print("\n🔎 Cantidad de unidades:")
    # print("Chinese:", len(army1.units))
    # print("English:", len(army2.units))
