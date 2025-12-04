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

scores: List[int] = [85, 90, 78]  # List of integers representing scores
# Dictionary with string keys and string values
user_info: Dict[str, str] = {"name": "Aditya", "city": "New York"}
optional_value: Optional[str] = None  # Optional string that can be None
print(
    f"Scores: {scores}, User Info: {user_info}, Optional Value: {optional_value}")


class Product:
    name: str
    price: float
    tags: Optional[List[str]]  # Optional list of string tags

    # Constructor with type hints
    def __init__(self, name: str, price: float, tags: Optional[List[str]] = None):
        self.name = name
        self.price = price
        self.tags = tags

    def __repr__(self):
        # Representation method for printing
        return f"Product(name={self.name}, price={self.price}, tags={self.tags})"


p = Product(name="Laptop", price=999.99, tags=["electronics", "computer"])
print(p)  # Print the product instance
