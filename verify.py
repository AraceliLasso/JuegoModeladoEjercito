from models.army import Army

if __name__ == "__main__":
    #! Crea dos ejércitos
    army1 = Army("bizantine", "Blasters")
    army2 = Army("english", "TeaTime")

    army1.show_unit_summary()
    army2.show_unit_summary()


    print("\n🔍 Number of units before battle:")
    print("the", army1.army_name, "a/an", army1.civilization, "army has", len(army1.units), "units") 
    print("the", army2.army_name, "a/an", army2.civilization, "army has", len(army2.units), "units") 

    print(army1.army_name, "initial strength:", army1.get_total_strength())
    print("TeaTime initial strength:", army2.get_total_strength())


    #! Simula una batalla
    army1.attack(army2)

    print("\n🏁 After the battle:")
    print(army1.army_name,"strength:", army1.get_total_strength())
    print(army2.army_name,"strength:", army2.get_total_strength())
    print(army1.army_name, "gold:", army1.gold)
    print(army2.army_name,"gold:", army2.gold)

    print("\n📜 Battle history:")
    print(army1.army_name, army1.civilization,"civilization:", army1.battle_history)
    print(army2.army_name,army2.civilization,"civilization:", army2.battle_history)

    print("\n🔎 Number of units after battle:")
    print(army1.army_name,":", len(army1.units))
    print(army2.army_name,":", len(army2.units))
