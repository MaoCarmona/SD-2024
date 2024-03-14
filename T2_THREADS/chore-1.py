import concurrent.futures

class SequenceCalculator:
    def __init__(self):
        self.result = 0

    def calculate_term(self,base, exponent):
        term = base ** exponent
        self.result += term

    def calculate_sequence(self,base, start_exponent, end_exponent):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.calculate_term, base,exponent) for exponent in range(start_exponent, end_exponent + 1)]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # Wait for the calculation to finish
        print(f"Result: {self.result}")

# Example usage
sequence_calculator = SequenceCalculator()
sequence_calculator.calculate_sequence(2,1, 10)
