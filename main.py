import random


def partest(x, y):
    if 1 in (x, y):  # teste agrupado, se 1 (infectado) estiver no par, teste de novo
        if x == 1:
            return 3
        else:
            return 3
    return 1


def covsim(incidencia, simulacoes):
    random.seed()
    lista = [0,0,0]
    a, b, testes = -1, -1, 0
    for p in range(2 * simulacoes):
        a = b
        if random.random() > incidencia:
            b = 0
        else:
            b = 1
        if p % 2 == 1:
            testes += partest(a, b)
            lista[partest(a, b)-1] += 1
    print(lista)
    return testes


def covsim2(incidencia, numero_de_testes):
    soma_testes = 0
    random.seed()
    for i in range(numero_de_testes):
        pessoa1 = random.random()
        pessoa2 = random.random()
        if pessoa1 >= incidencia and pessoa2 >= incidencia:
            testes = 1
        elif pessoa1 <= incidencia:
            testes = 3
        else:
            testes = 2
        soma_testes += testes
    return soma_testes


def main():
    simulacoes = int(input("Quantas simulações?: "))
    # incidencia = float(input("Qual a incidencia?: "))
    for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
        x = covsim(i, simulacoes)
        estimativa = 2 *i * (i + 2 * (1-i)) + 1
        print(f"{x / simulacoes} testes/par, estimativa probalistica: {estimativa}")


if __name__ == '__main__':
    main()
