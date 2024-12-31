from pydantic import BaseModel
from typing import Union

class Exit(BaseModel):
    """A model which defines exit codes which can terminate the application."""
    code: int

class Fibonacci(BaseModel):
    """A model which defines the length of a fibonacci sequence to generate."""
    length: int
