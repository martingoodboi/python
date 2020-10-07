#okobere

from random import randrange, uniform




soucet = 0
while soucet < 21:
    odpoved = input("Chceš hrát?...")
    if odpoved == 'ano':
        karta = randrange(2,11)
        soucet = karta + soucet
        print ("Hodil jsi...", karta , "Součet je... ",soucet)
    elif odpoved == 'ne':
        print ("Jsi na ", soucet, " a končíš hru")
        break

if soucet == 21:
    soucet = karta + soucet
    print ("Gratuluji, jsi vítěz!")
        
elif soucet > 21: 
    print ("Bohužel to dnes nevyšlo ._. ")
else:
    print ("Chybělo ti", 21 - soucet,"třeba příště")
    
