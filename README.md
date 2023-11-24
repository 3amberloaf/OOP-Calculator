## Introduction

This Python code will demonstrate the foundations of programming through the classic calculator program. 

I have established three calculators; teacher calculator, teacher calculation, and teacher history test files, which will be checked by their appropriate pytest test files.

## Overview

1. List
2. Dictionary
3. Mutable
4. Immutable
5. Sorted
6. Unsorted
7. Index
8. Element
9. Key
10. Value

## Steps

1. Set up a virtual environment through the terminal
   - python3 -m venv venv
   - source venv/bin/activate

2. Install the necessary requirements
   - pip3 install -r requirements.txt

3. Test the functions 
   - pytest tests/


## Conclusion

In this program, we have established the basics of OOP programming.

1. Establish calculator subclasses so the calculations are result at run time, rather than stored
2. Added a constructor to the calculations class that sets val1 and val2
3. Created a history class that extends the built-in list class and added it to the calculator as a static property
4. Added methods for the history: constructor, get last result, and print history Note run pytest with -s option i.e. pytest -s to show printed output
5. Added a `repr` method to the calculation to properly print the object contents.