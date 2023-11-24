# OOP Calculator Part 3 - Working with Lists Your First Data Structure

## Introduction

In this unit you will learn about lists and how to work with them. Lists are important to understand because they are
one of the simplest data structures to understand and one of the most common tools for programmers to use.
In your program, you will use a list to store calculations in a history class. You will extend the built-in list data
structure, so you inherit all the methods that lists use to manage their data.

You need to make the teacher calculator, teacher calculation, and teacher history test files pass by writing the code in
their respective dunder init files in the app folder/ sub folders.

## Code Screenshots

1. [Calculator](calculator.png)
2. [Calculations - partial without the subclasses (addition, division, etc...)](calculation.png)
3. [History](history.png)

## Tips:

1. Do not copy and paste!!!!!! YOU CAN'T LEARN BY DOING THIS 
2. Try to make one action / function work at a time even if it doesn't exactly do what you want, you need to understand
   what is being called and what data is being passed to each method, so you should use assert or print to check this.
3. Work on each test file individually and create your own test file to practice with, so you can come up with your own idea and try it out.
4. Realize that this is complicated and to truly understand what is going on you need to break things down into steps that you personally can understand.  Create your own experiments in your own test file(s) to validate your understanding.
5. Remember you need to have __init__ as the constructor method not __int__ 
6. Ask questions in  Slack, this is going to get a lot harder and at this point you need to make sure you understand what is going on in the program.
7. DO NOT PUT YOUR FINAL CODE IN THE TEST FILES THE CODE NEEDS TO GO INTO THE APPLICATION THAT IS  IN THE APP FOLDER OR ONE  OF ITS SUB FOLDERS!
8. GOOGLE THE ERROR MESSAGES and IF YOU ASK A QUESTION IN SLACK YOU NEED TO SHOW A SCREEN SHOT OF THE ERROR AND THE CODE THAT IT REFERS TO 
9. READ THE READINGS THEY ARE THERE FOR A REASON!

## Instructions - Not verbatim for how to get this to work but more or less correct

1. Fix calculations subclasses so that they calculate a calculation result at run-time rather than stores it
2. Add a constructor to the calculations class that sets val1 and val2
3. Create your calculation subclasses with only the get result method that will use the correct operation to return the results
4. Create a history class that extends the built-in list class and add it to the calculator as a static property i.e.
   one between the class signature (class name) and the first method.
5. Add methods for the history: constructor, get last result, and print history Note run pytest with -s option i.e.
   pytest -s to show printed output
6. Add a __repr__ method to the calculation to properly print the object contents.

## Assignment Requirements

Instructor Video - Part 1 [Watch Here](https://youtu.be/7jgo4yhZ1gk)
Instructor Video - Part 2 - [Watch Here](https://youtu.be/QeeyzIJFKnA)

## Module Readings:

1. https://towardsdatascience.com/intro-to-data-structures-2615eadc343d
2. https://towardsdatascience.com/solid-coding-in-python-1281392a6a94
3. https://www.w3schools.com/python/python_lists.asp
4. https://www.geeksforgeeks.org/python-data-structures/
5. https://docs.python.org/3/tutorial/datastructures.html

## Vocabulary

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

## Prerequisite Knowledge

Note: Previously completed on instances

## Steps to Complete the Assignment

1. Open Pycharm Pro / Pycharm Community and clone the assignment repository. Open up a terminal in Pycharm, run "pip
   install -r requirements.txt" and then run "pytest".  **If pycharm shows you an error about pip / requirements when
   you clone the repo just skip/cancel/dismiss the error and run the command in the terminal like I said above**
2. You will need to complete the requirements for the assignment and remove/replace the tests that are meant to fail
   that I placed in each file.
3. When your pytest passes just commit and push it back to the origin and the assignment will be graded automatically by
   GitHub running the test that you run locally.
4. Check that your tests pass on GitHub after you push the assignment and then submit a link to your repository to the
   assignment in Canvas. In GitHub on the repository, click the actions tab on GitHub to see your tests run. You will
   need to click on the autograding workflow to inspect that screen to see the detail test results.


