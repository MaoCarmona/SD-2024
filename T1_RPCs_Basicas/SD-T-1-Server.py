from xmlrpc.server import SimpleXMLRPCServer

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero."

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def fibonacci(n):
        if n <= 0:
            return "Error: Invalid input."
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_series = [0, 1]
            while len(fib_series) < n:
                fib_series.append(fib_series[-1] + fib_series[-2])
            return fib_series

    @staticmethod
    def invert_list(filename):
        try:
            with open(filename, 'r') as file:
                numbers = [int(line) for line in file]
            inverted_list = numbers[::-1]
            with open('inverted_list.txt', 'w') as output_file:
                for num in inverted_list:
                    output_file.write(str(num) + '\n')
            return "List inverted and saved to inverted_list.txt."
        except Exception as e:
            return "Error: " + str(e)

    @staticmethod
    def repeated_number(filename):
        try:
            with open(filename, 'r') as file:
                numbers = [int(line) for line in file]
            counter = {}
            for num in numbers:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
            most_common = max(counter, key=counter.get)
            return f"The most repeated number is {most_common}."
        except Exception as e:
            return "Error: " + str(e)

    @staticmethod
    def verify_user(username, password):
        valid_user = ('falcao', 'rayo2024')
        if (username, password) == valid_user:
            return True
        else:
            return False


if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_function(MathOperations.add, "sumar")
    server.register_function(MathOperations.subtract, "restar")
    server.register_function(MathOperations.multiply, "multiplicar")
    server.register_function(MathOperations.divide, "dividir")
    server.register_function(MathOperations.power, "potencia")
    server.register_function(MathOperations.fibonacci, "fibonacci")
    server.register_function(MathOperations.invert_list, "Invertir Lista")  # Ajuste aquí
    server.register_function(MathOperations.repeated_number, "Repetir Número")  # Registro de nueva función
    server.register_function(MathOperations.verify_user, "Verificar Usuario")  # Registro de nueva función
    print("Servidor iniciado...")
    server.serve_forever()
