#"""""Ce programme affectera un nombre signé aléatoire à la variable numéro à chaque fois qu'il sera exécuté. Complétez le code source afin d'indiquer si le nombre stocké dans la variable number est positif ou négatif.

#Vous trouverez le code source ici
#Le numéro de la variable stockera une valeur différente chaque fois que vous exécuterez ce programme
#Vous n'avez pas besoin de comprendre ce que font import, random et randint. Ne touchez pas à ce code
#Le résultat du programme devrait être :
#Le nombre, suivi de
#si le nombre est supérieur à 0 : est positif
#si le nombre est égal à 0 : est nul
#si le nombre est inférieur à 0 : est négatif
#suivi d'une nouvelle ligne

#Traduit avec DeepL.com (version gratuite)"""
#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number  > 0 :
    print(f"{number} is positif")
if number == 0 :
    print(f"{number} is nul")
if number < 0:
    print(f"{number} is négatif")
print()