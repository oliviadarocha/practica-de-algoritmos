user1 = input('Escoja piedra, papel o tijeras: ')
user2 = input('Escoja piedra, papel o tijeras: ')

if user1 == user2 :
    print("empate")
elif (user1 == 'piedra') and (user2 == 'papel') :
    print('gana el jugador 2')
elif (user1 == 'piedra') and (user2 == 'tijeras') :
    print('gana el jugador 1')
elif (user1 == 'papel') and (user2 == 'tijeras') :
    print('gana el jugador 2')
elif (user1 == 'papel') and (user2 == 'piedra') :
    print('gana el jugador 1')
elif (user1 == 'tijeras') and (user2 == 'piedra') :
    print('gana el jugador 2')
elif (user1 == 'tijeras') and (user2 == 'papel') :
    print('gana el jugador 1')