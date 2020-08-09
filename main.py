from cuadrado_medio import AleatorioMedio
from congruencial import AleatorioCongruencial

def main():
    print('Numeros aleatorios\n')
    print('Seleccione los parametros para generar numeros aleatorios')
    print('Semilla:')
    semilla = int(input())
    print('Digitos significativos:')
    dgt = int(input())

    alt = AleatorioMedio(semilla, dgt)
    s = []
    for _ in range(50):
        s.append(alt.generar_numero_aleatorio())

    print(s)


if __name__ == "__main__":
    main()