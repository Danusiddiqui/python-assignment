#1) Explain the significance of Python keywords and provide examples of five keywords.
"""Keywords in Python are reserved words that have special meanings and cannot
 be used as identifiers (variable names, function names, etc.) because they are part 
 of the language syntax. These keywords are crucial for defining the structure and logic 
 of Python programs.we can use <help('keywords')> to see all the keywors in python.
 example of 5 keywors are:
 1) int 
  The int keyword is used to convert a value to an integer.
        a="42"
        b=int(a)
 2)print
   The print keyword is used to display output in the console.
        print("hello world")
 3)input:
   The input keyword is used to take user input. It returns the input as a string.
       a=input("enter your name")
 4)if, else:
        The if statement checks a condition. If it's true, it executes a block of code. 
        Otherwise, the else block is executed.   
            x = 5
            if x > 0:
               print("Positive number")
            else:
                print("Non-positive number")
 5)len:
     The len keyword is used to get the length of a sequence, such as a string, list, or tuple.
     python
            message = "Hello, World!"
            length = len(message)"""

#2) Describe the rules for defining identifiers in Python and provide an example 
"""Rules for Identifiers in Python:
     1)Valid characters include letters (upper and lower), digits, and underscore.
     2)Case-sensitive: myVar and myvar are different.
     3)Avoid using Python keywords or reserved words.
     4)Start with a letter or underscore, not a digit.
      Example:
           variable_name = 42
           _myVar = "Hello"       are valid identifiers."""

#3)What are comments in Python, and why are they useful6 Provide an example 
"""Comments in Python are text annotations within the code that are not
    executed. They are useful for providing explanations, documentation, or
    for temporarily disabling a piece of code.  Improve code readability and 
    maintainability.
    1) you can create single-line comments using the #
     eg:  #this is a comment """

#4)Why is proper indentation important in Python?
""" Proper Indentation in Python is important:
  Enforces Structure: Indentation defines block structures in Python.
  Readability: Proper indentation makes code visually clear and easy to understand.
  Execution: Incorrect indentation can lead to syntax errors or unintended logic.
  Pythonic Style: Follows PEP 8, Python's style guide, enhancing code consistency.
  
  eg        x = 5
            if x > 0:
               print("Positive number")
            else:
                print("Non-positive number") """

#5) What happens if indentation is incorrect in Python?
""" Incorrect indentation can lead to
    Syntax Errors: Inconsistent or incorrect indentation raises SyntaxError.
    Logic Errors: Can lead to unintended logic and unexpected behavior.
    Code Misinterpretation: Alters the meaning of the code; blocks with the same 
    level of indentation are considered part of the same block.
          # Incorrect indentation example
                 x = 5
                if x > 0:
                print("Positive number")
                print("Inside if block")  # Incorrect indentation print statement will
                                            be considerd outside if.
       """

#6) Differentiate 0etween expression and statement in Python with examples
"""  Expression:
       produces a value.
       examples: 2 + 3, x * 5, True and False.
    
    Statement:
    performs an action; may or may not produce a value.
    examples: Assignment (x = 10), Print (print("Hello")), 
    Conditional (if x > 5:)."""