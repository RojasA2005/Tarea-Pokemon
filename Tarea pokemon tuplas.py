import random


PS_jugador = (100, 100)
PS_oponente = (100, 100)
ataques_posibles = {"malicioso":(0, 10), "placaje":(35, 0), "ascuas":(20, 0)}
ataques_posibles_opp = ("látigo", "placaje", "pistola de agua")
opp_damages = ((10, 10), (35, 0), (40, 0))
cambio_vida = 0
cambio_defensa = 0

while PS_jugador[0] > 0 and PS_oponente[0] > 0:
    print("Vida de tu pokemon: {}, vida de tu oponente: {}".format(PS_jugador[0], PS_oponente[0]))
    ataque_jugador = input("Elige tu ataque: ")
    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador in ataques_posibles:
        cambio_defensa = PS_oponente[1] - ataques_posibles[ataque_jugador][1]
        cambio_vida = round(PS_oponente[0] - (ataques_posibles[ataque_jugador][0] * (100/PS_oponente[1])), 2)
        PS_oponente = (cambio_vida, cambio_defensa)
        if PS_oponente[1] <= 0:
            PS_oponente = (cambio_vida, 1)
        if PS_oponente[0] <= 0:
            break
        print("Usaste {}, ahora a tu oponente le quedan {} puntos de vida y {} de defensa".format(ataque_jugador, PS_oponente[0], PS_oponente[1]))
    else:
        print('Que estas haciendo?! Tus ataques son placaje, malicioso y ascuas.' )     
        continue 
    ataque_oponente = random.randrange(0, 3)
    cambio_defensa = PS_jugador[1] - opp_damages[ataque_oponente][0]
    cambio_vida = round(PS_jugador[0] - (opp_damages[ataque_oponente][0] * (100/PS_jugador[1])), 2)
    PS_jugador = (cambio_vida, cambio_defensa)
    if PS_jugador[1] <= 0:
        PS_jugador = (cambio_vida, 1)
    print("Tu oponente usó {}, te quedan {} puntos de vida y {} de defensa".format(ataques_posibles_opp[ataque_oponente], PS_jugador[0], PS_jugador[1]))
        



if PS_oponente[0] <= 0 and PS_jugador[0] <= 0:
    print("Empate.")
elif PS_oponente[0] <= 0: 
    print("Felicidades, has ganado!")
else:
    print('Perdiste, seras movido al centro pokemon mas cercano.')