import xmlrpc.client

def display_menu():
    print("*************Menú************")
    print("a. Sumar.")
    print("b. Restar.")
    print("c. Multiplicar.")
    print("d. Dividir.")
    print("e. Potencia.")
    print("f. Fibonacci.")
    print("g. Operaciones con lista de números.")
    print("q. Salir.")

def get_user_option():
    return input("Escoja su opción: ")

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Por favor ingrese un número válido.")

def read_list_from_input():
    numbers = []
    print("Ingrese 15 números enteros:")
    for _ in range(15):
        number = int(input())
        numbers.append(number)
    return numbers

def save_list_to_file(numbers):
    with open("number_list.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

def call_rpc(option):
    try:
        proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
        result = ""

        operations = {
            'a': ('sumar', 2),
            'b': ('restar', 2),
            'c': ('multiplicar', 2),
            'd': ('dividir', 2),
            'e': ('potencia', 2),
            'f': ('fibonacci', 1),
            'g': ('operaciones_lista', 0)
        }

        if option == 'q':
            return False

        if option not in operations:
            print("Opción no válida.")
            return True

        operation_name, num_args = operations[option]

        if num_args > 0:
            args = []
            for i in range(num_args):
                args.append(get_number(f"Ingrese el argumento {i + 1}: "))

            result = getattr(proxy, operation_name)(*args)
            print("El resultado es:", result)
        else:
            if operation_name == 'operaciones_lista':
                access = login()
                if not access:
                    print("Acceso no autorizado.")
                print("Acceso autorizado.")
                numbers = read_list_from_input()
                save_list_to_file(numbers)
                operation_name = 'Invertir Lista'
                inverted_list = getattr(proxy, operation_name)("number_list.txt")
                print("Lista invertida guardada en 'inverted_list.txt':")
                with open(inverted_list, "r") as file:
                    inverted_content = file.readlines()
                    for line in inverted_content:
                        print(line.rstrip()) 

                operation_name = 'Repetir Número'
                repeated_number = getattr(proxy, operation_name)("number_list.txt")
                print("El número más repetido en la lista es:", repeated_number)

    except Exception as e:
        print("Ocurrió un error al llamar a la función RPC:", e)

    input("Presione Enter para continuar...")
    return True

def login():
    operation_name ="Verificar Usuario"
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    authentication_result = getattr(proxy, operation_name)(user, password)
    return authentication_result


if __name__ == "__main__":
    try:
        while True:
            display_menu()
            option = get_user_option()

            if not call_rpc(option):
                break
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")
