import random


def external(func):
    """Decorator to mark external interface functions"""
    func._external_tagged = True
    return func

def init(func):
    """Decorator to mark initialization functions"""
    return func


@external
async def add(a: int, b: int) -> int:
    """{
    "description": "Add two numbers",
    "parameters": {
        "a": {
            "description": "First number",
            "type": "int"
        },
        "b": {
            "description": "Second number",
            "type": "int"
        }
    },
    "returns": {
        "description": "Sum of the two numbers",
        "type": "int"
    }
    }"""
    # cast to ints to avoid float return
    return int(a) + int(b)

@external
async def subtract(a: int, b: int) -> int:
    """{
    "description": "Subtract two numbers",
    "parameters": {
        "a": {
            "description": "First number",
            "type": "int"
        },
        "b": {
            "description": "Second number",
            "type": "int"
        }
    },
    "returns": {
        "description": "Difference of the two numbers",
        "type": "int"
    }
    }"""
    return a - b

@external
async def multiply(a: int, b: int) -> int:
    """{
    "description": "Multiply two numbers",
    "parameters": {
        "a": {
            "description": "First number",
            "type": "int"
        },
        "b": {
            "description": "Second number",
            "type": "int"
        }
    },
    "returns": {
        "description": "Product of the two numbers",
        "type": "int"
    }
    }"""
    return a * b

@external
async def divide(a: int, b: int) -> float:
    """{
    "description": "Divide two numbers",
    "parameters": {
        "a": {
            "description": "First number",
            "type": "int"
        },
        "b": {
            "description": "Second number",
            "type": "int"
        }
    },
    "returns": {
        "description": "Quotient of the two numbers",
        "type": "float"
    }
    }"""
    return a / b

@external
async def get_random_number() -> int:
    """{
    "description": "Get a random number",
    "returns": {
        "description": "Random number",
        "type": "int"
    }
    }"""
    return random.randint(0, 100)