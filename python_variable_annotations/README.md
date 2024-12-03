Python Variable Annotations
🏆 Project Badge
Python - Variable Annotations
Master
By: Emmanuel Turlay, Staff Software Engineer at Cruise
Weight: 1
Your score will be updated as you progress.

📖 Description
This project is about type annotations in Python, a powerful feature that improves code clarity, helps prevent bugs, and assists in catching type-related issues during development. You will learn to define type annotations for functions, variables, and complex types, and validate them using tools like mypy.

📚 Resources
Make sure to check out these resources for better understanding:

Python 3 Typing Documentation
MyPy Cheat Sheet
🎯 Learning Objectives
By the end of this project, you will be able to:

Understand type annotations in Python 3.
Use type annotations to specify function signatures and variable types.
Understand and apply Duck Typing in Python.
Validate your code using mypy.
🛠 Requirements
Allowed editors: vi, vim, emacs.
Environment: Ubuntu 20.04 LTS using Python 3.9.
Style: Your code must follow pycodestyle (version 2.5).
Each file must be executable and end with a new line.
Documentation: All modules, classes, and functions must have proper documentation.
📝 Tasks
0. Basic Annotations - Add
Objective: Write a type-annotated function add that takes two floats as arguments and returns their sum as a float.

Example:

def add(a: float, b: float) -> float:
    return a + b
1. Basic Annotations - Concat
Objective: Write a type-annotated function concat that concatenates two strings.

Example:


def concat(str1: str, str2: str) -> str:
    return str1 + str2
2. Basic Annotations - Floor
Objective: Write a type-annotated function floor that returns the floor of a float.

Example:

import math

def floor(n: float) -> int:
    return math.floor(n)
3. Basic Annotations - To String
Objective: Write a type-annotated function to_str that converts a float to its string representation.

Example:

def to_str(n: float) -> str:
    return str(n)
4. Define Variables
Objective: Define and annotate the following variables:

a (int): 1
pi (float): 3.14
i_understand_annotations (bool): True
school (str): "Holberton"
Example:


a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
5. Complex Types - List of Floats
Objective: Write a type-annotated function sum_list that sums a list of floats.

Example:

from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
6. Complex Types - Mixed List
Objective: Write a type-annotated function sum_mixed_list that sums a list containing integers and floats.

Example:

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
7. Complex Types - String and Int/Float to Tuple
Objective: Write a type-annotated function to_kv that returns a tuple with a string and the square of an int/float as a float.

Example:

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v**2))

8. Complex Types - Functions
Objective: Write a type-annotated function make_multiplier that returns a function to multiply a float by a given multiplier.

Example:

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
9. Duck Typing an Iterable Object
Objective: Write a type-annotated function element_length that returns a list of tuples containing an element and its length.

Example:

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
🛡️ Validating Code with mypy
To check your type annotations, use the mypy command:


mypy <filename>.py
Example:


mypy 0-add.py
📌 Key Concepts Recap
Type Annotations: Add clarity and help catch type errors before runtime.
Duck Typing: Focus on the object’s behavior rather than its type.
mypy: A static type checker for Python that validates type hints.
🌟 Contribute or Explore More!
Feel free to dive deeper into the Python Typing documentation or suggest improvements to this repository. 🚀

Author: Xavier
Project Repository: Python Variable Annotations
Happy Coding! 😊