print("New Game")
inventar = []

lauf = 0
lauf2 = 0
lauf3 = 0

def showInventar(list):
    for i in range(list):
        print(list[i])
while lauf < 5:
    male = input("Bist du männlich m oder weiblich w?")
    if male == "w":
        inventar.append(male)
        nameW = input("Wie ist dein Name?")
        inventar.append(nameW)
        print("Hallo " + nameW + ".")
    elif male == "m":
        inventar.append(male)
        nameM = input("Wie ist dein Name?")
        inventar.append(nameM)
        print("Hallo " + nameM + ".")
    else:
        print("Du hast nicht m oder w eingegeben!")
        lauf = lauf + 1
        continue

    print("Du besitzt einen Inventar-Beutel \nder alle wichtigen Informationen bereithält\nund in dem du Items sammeln kannst")
    print("Dein Inventar kannst du später jederzeit mit der Tastenkombi openInv aufrufen.")
    print("Das Abenteuer kann gleich los gehen.\n"
          "Bevor es beginnt, wähle noch deinen Begleiter.")

    while lauf2 < 5:
        begleiter = input("Dir  stehen 2 Gefährten zur Auswahl: Esel e und Schimmel s \n"
                          "Wähle weise:")
        if begleiter == "e":
            nameEsel = input("Du hast den Esel gewählt, nun gib ihm einen Namen:")
            inventar.append(nameEsel)
            print("Dein Esel heißt also " + nameEsel + ". Dann kann es ja nun los gehen!")
        elif begleiter == "s":
            nameSchimmel = input("Du hast den Schimmel gewählt nun gib ihm einen Namen:")
            inventar.append(nameSchimmel)
            print("Dein Schimmel heißt also " + nameSchimmel + ". Dann kann es ja nun los gehen!")
        else:
            print("Du hast etwas falsches eingegeben!")
            lauf2 = lauf2 + 1
            continue

        #for i in range(0,len(inventar)):
        #    print(inventar[i])

        while lauf3 < 5:
            geschichte = input("Du läufst einen Pfad entlang und kommst zu einer Gabelung. "
                                "\nDeine erste wichtige Entscheidung.\n"
                                "Gehst du nach links oder rechts?")

            if geschichte == "links":
                print("Du hast dich für den linken Pfad entschieden. \n"
                      "Deine Reise geht nach Westen in die Berge.")
                blabla = input("Dein Gefährte ist erschöpft, was möchtest du tun?\n"
                               "Futter besorgen oder schlafen?")
                if blabla == "Futter besorgen":
                    geschichte = input("Am Rand des Weges gibt es auf der einen Seite Bergahorn und auf der anderen Seite Feldahorn.\n"
                                       "Was wählst du?")
                    if geschichte == "Feldahorn":
                        print("Deinem Gefährten geht es schon besser und die Reise geht weiter.")
                        break
                    elif geschichte == "Bergahorn":
                        print("Diese Pflanze ist giftig für dein Pferd. Deinem Pferd geht es deutlich schlechter.")
                elif blabla == "schlafen":
                    print("Ihr schlaft eine Runde und erholt euch.")


            elif geschichte == "rechts":
                print("Du hast dich für den rechten Pfad entschieden. \n"
                      "Deine Reise geht nach Osten zur Küste.\n")
            else:
                print("Du hast nicht links oder rechts angegeben!")
                lauf3 = lauf3 + 1
                continue




