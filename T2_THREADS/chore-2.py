import concurrent.futures

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = None

    def addition(self):
        self.result = self.num1 + self.num2

    def subtraction(self):
        self.result = self.num1 - self.num2

    def multiplication(self):
        self.result = self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            self.result = self.num1 / self.num2
        else:
            self.result = "Cannot divide by zero"

    def execute_operations(self):
        operations = ["addition", "subtraction", "multiplication", "division"]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(getattr(self, op)) for op in operations]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # Wait for the operation to finish
        print("All operations completed")

    def print_results(self):
        print(f"Addition result: {self.result}")
        self.subtraction()
        print(f"Subtraction result: {self.result}")
        self.multiplication()
        print(f"Multiplication result: {self.result}")
        self.division()
        print(f"Division result: {self.result}")

# Example usage
calculator = Calculator(10, 5)
calculator.execute_operations()
calculator.print_results()
