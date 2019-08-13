#numero = int(input("digite um numero de 1 a 7: "))

#if numero == 1:
 #   print('é domingo!')
#elif numero == 2:
   # print('é segunda-feira!')
#elif numero == 3:
 #   print('é terça-feira!')
#elif numero == 4:
 #   print('é quarta-feira!')
#elif numero == 5:
 #   print('é quinta-feira!')
#elif numero == 6:
 #   print('é sexta!')
#elif numero == 7:
 #   print('é sabado!')
#else:
#    print('Digitou um numero invalido')
    



def dias (x):
    return{
        1: 'domingo',
        2: 'seg',
        3: 'ter',
        4: 'qua',
        5: 'qui',
        6: 'sex',
        7: 'sabado'
    }[x]

    x = int(input('digite o dia da semana de 1 a 7 : '))
    print(dias(x))
    
