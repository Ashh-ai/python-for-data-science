# Python Functions – Complete Interview + Coding Preparation
# Let's study Functions in Python exactly like we studied Sets: 60% interview preparation and 40% coding practice.
# I'll teach you from the basics to interview-level concepts, with proper definitions, examples, common interview questions and coding problems.
# Our goal is that you should be able to:
# - Explain functions confidently in interviews.
# - Understand how functions work internally.
# - Write your own functions without depending on tutorials.
# - Solve basic coding questions using functions.
# - Understand arguments, parameters, return statements, scope, lambda, *args, **kwargs, etc.
# Part 1. What is a Function in Python?
# 1. Definition (Interview-ready)
# A function in Python is a reusable block of code designed to perform a specific task. It executes when it is called and can accept inputs (arguments) and return an output.
# In simple Hinglish:
# Function ek reusable code block hota hai. Agar koi task baar-baar perform karna hai, toh uska code ek function ke andar likh dete hain. Jab bhi zarurat ho, function ko call kar sakte hain.
# Example without a function:
# print(10 + 20)print(30 + 40)print(50 + 60)



# Example with a function:
# def add():    print(10 + 20)add()add()add()



# Output:
# 30
# 30
# 30


# Notice that we wrote the logic only once but reused it three times.
# 2. Why do we use functions?
# Interviewers often ask this question.
# Reason	Explanation
# Code reusability	Write once, use multiple times.
# Modularity	Divide a large program into smaller parts.
# Readability	Makes code easier to understand.
# Maintainability	Easier to update and fix errors.
# Debugging	Easier to identify where an error occurs.
# Avoid repetition	Reduces unnecessary repeated code.
# Interview answer: Functions promote code reusability, modularity, readability and maintainability while reducing code duplication.

# Part 2. How to create a function
# 3. def keyword
# In Python, we use the def keyword to define a function.
# Syntax:
# def function_name():    # function body    statement



# Example:
# def greet():    print("Hello Ashray")greet()



# Output:
# Hello Ashray


# Let's understand every part:
# Component	Meaning
# def	Keyword used to define a function.
# greet	Function name.
# ()	Parentheses where parameters are written.
# :	Indicates the beginning of the function body.
# Indentation	Defines the function body.
# greet()	Calls or executes the function.
# Important interview question: What happens if you define a function but don't call it?
# Answer: The function is created, but its body does not execute until the function is called.
# def hello():    print("Hello")# No output because function is not called.



# Part 3. Parameters and Arguments
# Very important for interviews
# 4. What are Parameters?
# Interview definition: Parameters are variables defined inside a function's parentheses that receive values when the function is called.
# 5. What are Arguments?
# Interview definition: Arguments are the actual values passed to a function when it is called.
# Example:
# def greet(name):    print("Hello", name)greet("Ashray")



# Output:
# Hello Ashray


# Understand the difference:
# - name = Parameter
# - "Ashray" = Argument
# Remember this difference
# FUNCTION DEFINITION
# def greet(name):
# Parameter = name

# FUNCTION CALL
# greet("Ashray")
# Argument = "Ashray"