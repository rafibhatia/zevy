greeting = "Hello from global scope!"

def main_program(name=None):
    local_greeting = "Hello from local scope!"
    if name is None:
        print(local_greeting)
    else:
        print(f"Hello, {name}!")
    try:
        result = add_numbers(5, "ten")
        print(f"The result is: {result}")
    except TypeError:
        print("Oops! There was a problem with adding numbers.")

def add_numbers(a, b):
    return a + b

print(greeting)
main_program()
main_program(name="Alice")
