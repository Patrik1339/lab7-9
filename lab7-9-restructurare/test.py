from logging import raiseExceptions


def main():
    lista = [5,1,7,11,2]
    for i in range(1, len(lista)):
        for j in range(i - 1, -1, -1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    print(lista)

    dictionar = {1:7, 2:9, 3:1, 4:4}
    dictionar = dict(sorted(dictionar.items(), key=lambda x: x[1]))
    print(dictionar)

    lista = [5,1,7,11,2]
    print(sorted(lista))

    try:
        if 1 == 2:
            print('qwefr')
        else:
            raise ValueError('qwefr')
    except ValueError as ve:
        print(ve)

main()