import time
from pprint import pprint

def main():
    #pprint(dir(time))
    hora=time.localtime()
    horaA=int(hora[3])
    minA=int(hora[4])
    #pprint(hora)
    #pprint(horaA)
    #pprint(minA)
    horaS=19
    minS=60
    difHora=horaS-horaA-1
    difMin=minS-minA
    #pprint(difHora)
    #pprint(difMin)
    print("Este programa calcula el tiempo que te falta para ir a casa cuando estas en el trabajo")
    if difHora>=0 :
        print('Te faltan : ',difHora,'horas',' y ', difMin,' minutos ', 'para ir a casa')
    else :
        print(('Ya debes ir a casa, haz excedido tu horario de trabajo'))


if __name__ == '__main__':
    main()


