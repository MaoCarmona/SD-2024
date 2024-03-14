import concurrent.futures
import random
import math

class NormCalculator:
    def __init__(self, vector, numThreads):
        self.vector = vector
        self.numThreads = numThreads

    def calculate_norm(self, chunk):
        return sum(x ** 2 for x in chunk)

    def run(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            chunk_size = len(self.vector) // numThreads
            chunks = [self.vector[i:i+chunk_size] for i in range(0, len(self.vector), chunk_size)]
            norm_futures = [executor.submit(self.calculate_norm, chunk) for chunk in chunks]

            norms = [future.result() for future in concurrent.futures.as_completed(norm_futures)]
            total_norm_squared = sum(norms)
            total_norm = math.sqrt(total_norm_squared)
            print("Norma del vector:", total_norm)

vector = [random.randint(1, 100) for _ in range(20)]
# vector = [1,2,3,4,5,6,7,8,9,,10,11,12,13,14,15,16,17,18,19,20] # for validate
numThreads=10
print(vector)
norm_calculator = NormCalculator(vector,numThreads)
norm_calculator.run()
