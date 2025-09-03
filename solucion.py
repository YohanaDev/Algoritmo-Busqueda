def find_neighbors(database_list, query_number):
    """
    Encuentra el número más grande que es menor y el número más pequeño que es mayor
    en una lista ordenada para un número de consulta dado.
    """
    lower_neighbor = 'X'
    upper_neighbor = 'X'

    for num in reversed(database_list):
        if num < query_number:
            lower_neighbor = num
            break

    for num in database_list:
        if num > query_number:
            upper_neighbor = num
            break
            
    return f"{lower_neighbor} {upper_neighbor}"

def main():
    """
    Función principal para manejar la entrada y salida del algoritmo.
    """
    try:
    
        print("1. Ingrese el tamaño de la lista de la base de datos:")
        input() 
        
        print("2. Ingrese el listado de números separados por espacios (de menor a mayor):")
        database_input = input().strip().split()
        database_list = [int(n) for n in database_input]

        print("3. Ingrese el número de consultas a evaluar:")
        input()

        print("4. Ingrese la lista de números a consultar, separados por espacios:")
        query_input = input().strip().split()
        query_list = [int(n) for n in query_input]

        print("\nResultados:")

        for query in query_list:
            print(find_neighbors(database_list, query))

    except (ValueError, IndexError):
        print("\nError: Asegúrate de que los datos de entrada son números enteros y están en el formato correcto.")

if __name__ == "__main__":
    main()