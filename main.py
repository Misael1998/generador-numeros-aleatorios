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
    for _ in range(50):
        # print(alt.generar_numero_aleatorio())
        s = alt.generar_numero_aleatorio()

    alt.obtener_cola()


if __name__ == "__main__":
    main()