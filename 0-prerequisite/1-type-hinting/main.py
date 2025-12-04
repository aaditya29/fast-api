from typing import List, Dict, Optional


def section(title: str):
    # Print the length of the title above and below the title itself
    print(len(title))
    print(title)  # Print the title itself
    # Print the length of the title above and below the title itself
    print(len(title))


age: int = 25
price: float = 19.99
name: str = "FastAPI"
is_active: bool = True
print(f"Age: {age}, Price: {price}, Name: {name}, Active: {is_active}")

# type hinted function


def greet_user(username: str) -> str:
    return f"Hello, {username}!"


print(greet_user("Aditya"))
