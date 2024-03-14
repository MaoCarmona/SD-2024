import concurrent.futures
import math
import sys

class FactorialCalculator:
    def __init__(self):
        pass

    def calculate_partial_sum(self, start, end):
        partial_sum = sum(math.factorial(num) for num in range(start, end + 1))
        return partial_sum

    def calculate_total_sum(self, n, num_threads):
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            chunk_size = n // num_threads
            start = 1

            for _ in range(num_threads - 1):
                end = start + chunk_size - 1
                future = executor.submit(self.calculate_partial_sum, start, end)
                futures.append((future, start, end))
                start = end + 1

            end = n
            last_future = executor.submit(self.calculate_partial_sum, start, end)
            futures.append((last_future, start, end))

            total_sum = 0
            progress = 0
            for future, start, end in futures:
                sys.stdout.write(f"Ejecutando hilo: {start}-{end} [")
                while not future.done():
                    sys.stdout.write("|")
                    sys.stdout.flush()
                total_sum += future.result()
                progress += 1
                sys.stdout.write("]\n")
                print("Resultado del factorial calculado en el hilo: ",future.result(),"\n")

        print("La suma de los factoriales es:", total_sum)

# Pedir al usuario el valor de n y el número de hilos
n = int(input("Ingrese el valor de n: "))
num_threads = int(input("Ingrese el número de hilos: "))

# Calcular la suma de los factoriales con el número dado de hilos
factorial_calculator = FactorialCalculator()
factorial_calculator.calculate_total_sum(n, num_threads)
