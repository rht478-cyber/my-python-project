# list_project.py
from calc.basic import add, subtract
from calc.advanced import multiply

def perform_calculations():
    result_add = add(5, 3)
    result_subtract = subtract(10, 4)
    result_multiply = multiply(2, 6)

    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")
    print(f"Multiplication: {result_multiply}")

if __name__ == "__main__":
    perform_calculations()
    
    