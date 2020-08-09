from cuadrado_medio import AleatorioMedio
from congruencial import AleatorioCongruencial

def main():
    print('Numeros aleatorios\n')
    print('Seleccione el metodo de generacion de numeros alearorios')
    print('1.Cuadrado medio')
    print('2.Congruencial')
    metodo = int(input())
    if metodo == 1:
        print('Selecciones los parametros para generar 50 numeros aleatorios')
        print('Semilla:')
        semilla = int(input())
        print('Digitos significativos:')
        dgt = int(input())

        alt = AleatorioMedio(semilla, dgt)
        s = []
        for _ in range(50):
            s.append(alt.generar_numero_aleatorio())
        print('Los numeros aleatorios generados son:')
        print(s)
    elif metodo == 2:
        print('Seleccione los parametros para generar 50 numeros aleatorios')
        print('Semilla:')
        semilla = int(input())
        print('Multiplicador:')
        multiplicador = int(input())
        print('Constante aditiva')
        constante_aditiva = int(input())
        print('Modulo')
        modulo = int(input())

        alt = AleatorioCongruencial(semilla, multiplicador, constante_aditiva, modulo)
        s = []

        for _ in range(50):
            s.append(alt.generar_aleatorio())
        
        cola, periodo = alt.obtener_cola_periodo()
        print('Los numeros aleatorios son:')
        print(s)
        print(f'La cola es: {cola} \nEl periodo es: {periodo}')
    else:
        print('La opcion seleccionada no es valida')


if __name__ == "__main__":
    main()