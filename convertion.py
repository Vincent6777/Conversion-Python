messure = input("Wil je temperatuur, gewicht of lengte omzetten")
# start van temperatuur
if messure == "temperatuur":
    temperatuur = input("als je vanaf farenheit wilt zeg dan F, als je vanaf celcius wilt zeg dan C, als je vanaf kelvin wilt zeg dan K ")
    # start van farenheid naar celcius
    if temperatuur == 'F':
        x = input("als je van farenheit naar celcius wilt zeg dan C, als je van farenheit naar kelvin wilt zeg dan K")
        if x == 'C':
            graden = float(input("Hoeveel graden farenheit is het?"))
            print((graden - 32) * 5 / 9)
    # einde van farenheit naar celcius
    # start van farenheit naar kelvin
        elif x == 'K':
            graden = float(input("Hoeveel graden farenheit is het?"))
            print((graden - 32) * 5 / 9 + 273.15)
    # einde van farenheid naar kelvin
        else: print("Wrong")
    # start van celcius naar farenheit
    elif temperatuur == 'C':
        x = input("als je van celcius naar farenheit wilt zeg dan F, als je van celsius naar kelvin wilt zeg dan K")
        if x == 'F':
            graden = float(input("Hoeveel graden celsius is het?"))
            print((graden * 9 / 5) + 32)
    # einde van celcius naar farenheit
    # start van celcius naar kelvin
        elif x == 'K':
            graden = float(input("Hoeveel graden celsius is het?"))
            print(graden + 273.15)
    # einde van celcius naar kelvin
        else: print("Wrong")
    # start van kelvin naar farenheit
    elif temperatuur == 'K':
        x = input("als je van kelvin naar farenheit wilt zeg dan F, als je van kelvin naar celsius wilt zeg dan C")
        if x == 'F':
            graden = float(input("Hoeveel graden kelvin is het?"))
            print((graden - 273.15) * 9 / 5 + 32)
    # einde van kelvin naar farenheit
        elif x == 'C':
            graden = float(input("Hoeveel graden kelvin is het?"))
            print(graden - 273.15)
        else: print("Wrong")
    else: print("Wrong")
# einde van temperatuur

# start van gewicht
elif messure == "gewicht":
    weight = input("als je vanaf pound naar kg wilt zeg dan P, als je van kg naar pound wilt zeg dan K")
    # start van pound
    if weight == 'P':
        Nummer = float(input("Hoeveel pound is het?"))
        print(Nummer * 0.453592)
    # einde van pound
    # start van kg
    elif weight == 'K':
        Nummer = float(input("Hoeveel kg is het?"))
        print(Nummer * 2.20462)
    # einde van pound
    else: print("Wrong")
# einde van gewicht

# start van lengte
elif messure == "lengte":
    lengte = input("als je van cm naar inch wilt zeg dan C, als je van inch naar cm wilt zeg dan I, als je van foot naar meter wilt zeg dan F, als je van meter naar foot wilt zeg dan M, als je van km naar mile wilt zeg dan K, als je van mile naar km wilt zeg dan MI")
    # start van cm naar inch
    if lengte == 'C':
     x = float(input("Hoeveel cm is het?"))
     print(x / 2.54)
    # einde van cm naar inch
    # start van inch naar cm
    elif lengte == 'I':
     x = float(input("Hoeveel inch is het?"))
     print(x * 2.54)
    # einde van inch naar cm
    # start van foot naar meter
    elif lengte == 'F':
     x = float(input("Hoeveel foot is het?"))
     print(x * 0.3048) 
    # einde van foot naar meter
    # start van meter naar foot
    elif lengte == 'M':
     x = float(input("Hoeveel meter is het?"))
     feet = x * 3.28084
     inches = (feet % 1) * 12 
     print(f"{int(feet)} feet and {round(inches)} inches")
    # einde van meter naar foot
    # start van km naar mile
    elif lengte =='K':
     x = float(input("Hoeveel km is het?"))
     print(x * 0.621371)
    # einde van km naar mile
    # start van mile naar km
    elif lengte == "MI":
     x = float(input("Hoeveel mile is het?"))
     print(x * 1.60934)
    # einde van mile naar km
    else: print("Wrong")
    # einde van lengte
else: print("Wrong")