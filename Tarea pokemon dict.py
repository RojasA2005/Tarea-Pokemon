import random


PS_jugador = 100
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100
ataques_posibles = {"malicioso": 10, "placaje":35, "ascuas":20}
ataques_posibles_opp = [["látigo", "defensa", "10"], ["placaje", "vida", 0], ["pistola de agua", "vida", 0]]
damage = 0

while PS_jugador > 0 and PS_oponente > 0:
    print("Vida de tu pokemon: {}, vida de tu oponente: {}".format(PS_jugador, PS_oponente))
    ataque_jugador = input("Elige tu ataque: ")
    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador in ataques_posibles:
        for key, value in ataques_posibles.items():
            if ataque_jugador == key:
                if key == "malicioso":
                    print("La defensa de tu oponente ha disminuido!")
                    defensa_oponente = defensa_oponente - 10
                    if defensa_oponente <= 0:
                        defensa_oponente = 1
                    break
                else:
                    damage = round(ataques_posibles[key] * (100/defensa_oponente), 2)
                    PS_oponente -= damage
                    print("Bien! hiciste {} de daño!".format(damage))
                    break
    else:
        print('Que estas haciendo?! Tus ataques son placaje, malicioso y ascuas.' )     
        continue 
    if PS_oponente <= 0:
        break
    ataque_oponente = random.randrange(0, 3)
    if ataque_oponente == 0: #tail whip
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == 1: #tackle
        ataques_posibles_opp[ataque_oponente][2] = round(35 * (100/defensa_jugador), 2)
        PS_jugador -= ataques_posibles_opp[ataque_oponente][2] 
    elif ataque_oponente == 2: #water gun
        ataques_posibles_opp[ataque_oponente][2] = round(40 * (100/defensa_jugador), 2)
        PS_jugador -= ataques_posibles_opp[ataque_oponente][2] 
    print("Tu oponente utilizó {}, que te bajó {} puntos de {}".format(ataques_posibles_opp[ataque_oponente][0], str(ataques_posibles_opp[ataque_oponente][2]), ataques_posibles_opp[ataque_oponente][1]))
        



if PS_oponente <= 0 and PS_jugador <= 0:
    print("Empate.")
elif PS_oponente <= 0: 
    print("Felicidades, has ganado!")
else:
    print('Perdiste, seras movido al centro pokemon mas cercano.')