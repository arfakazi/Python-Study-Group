def greet(name, message="Hello"): #default message is “Hello”
    print(message, name)

greet(name="Alice", message="Hi") # call with both arguments specified
greet(message="Hey", name="Bob") # function call in another order
greet("Charlie") # function call without message
