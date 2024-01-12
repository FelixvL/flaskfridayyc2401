def functieeen():
    import random
    grappen = [
        "Waarom kunnen geheimagenten nooit goed schaken? Omdat ze altijd bang zijn voor lopers!",
        "Waarom kunnen fietsen niet zelfstandig staan? Omdat ze altijd twee-takt!",
        "Waarom kunnen spinnen geen computers gebruiken? Omdat ze altijd het web kwijtraken!",
        "Wat zei de ene muur tegen de andere muur? 'Ik zie je aan de andere kant!'",
        "Waarom nam de wiskundige een ladder mee naar het werk? Omdat hij het dak wilde berekenen!",
        "Waarom nam de fiets een paraplu mee? Omdat hij bang was voor een spatje regen!",
        "Waarom kunnen boeken zo slecht tegen kritiek? Omdat ze altijd uit elkaar vallen!",
        "Waarom kunnen tomaten nooit een feestje geven? Omdat ze altijd in de puree zitten!",
        "Waarom kunnen mummies geen geheimen bewaren? Omdat ze altijd in lappen praten!",
        "Waarom kunnen spoken nooit liegen? Omdat je er dwars doorheen kunt kijken!",
        "Waarom kunnen bomen nooit naar school gaan? Omdat ze altijd al geleerd hebben om te staan!",
    ]
    random.shuffle(grappen)

    while grappen:
        huidige_grap = grappen.pop()
        print(huidige_grap)
        input("Druk op Enter voor de volgende grap...")