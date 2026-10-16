### “== compares the values of two objects, while is compares their identity|
"""
Q&A (model answers)

Q1. When should we use is, and when ==?
Use == for almost all comparisons of values. Use is mainly to check None, like if x is None:.

Q2. Why do we write x is None and not x == None?
None exists only once in Python, so is is the exact and safe check. Also, a class can change how == behaves, so == None can give a surprising result. is None is also the style recommended by PEP 8.

Q3. If a is b is True, will a == b also be True?
Yes. If both names point to the same object, their values must be equal.

Q4. If a == b is True, will a is b also be True?
Not always. Two different lists can have equal values but be different objects



"""

    #                     ####LOOPS INTERVIEW QUEDTIONS 

"""
Part 3: Core Theory Q&A (model answers)

Q1. What is the difference between for and while?
A for loop is used when we know what to iterate over (a sequence or a fixed count). A while loop is used when we do not know the number of iterations and want to run until a condition becomes False.

Q2. What is the difference between break and continue?
break exits the whole loop. continue only skips the current iteration and goes on with the next one.

Q3. What does range(1, 10, 2) give?
1, 3, 5, 7, 9. It starts at 1, stops before 10, and moves by 2.

Q4. Is range() a list?
No. In Python 3 it is a lazy range object. It creates numbers when needed, so it uses very little memory even for range(10**9). We can use list(range(5)) if we need a list.

Q5. What is the else block of a loop?
It runs only when the loop finishes normally, without hitting break. It is useful for search problems, like checking whether a number is prime.

Q6. What is an infinite loop? How do you avoid it?
It is a loop that never stops. In a while loop, we avoid it by making sure the condition changes inside the loop (for example i += 1), or by using break.

Q7. What is the use of enumerate()?
It gives the index and the value together while looping, so we do not need to manage a counter by hand.

Q8. What is the use of zip()?
It joins two or more iterables item by item, so we can loop over them together. It stops at the shortest one.

Q9. How do you loop over a dictionary?
for key in d gives keys, for v in d.values() gives values, and for k, v in d.items() gives both.

Q10. What is the time complexity of a single loop and a nested loop?
A single loop over n items is O(n). A nested loop (both over n) is O(n²).

Q11. What is a list comprehension? Why is it used instead of a loop?
It is a short, readable way to build a list in one line: [x**2 for x in range(5)]. It is usually shorter and a bit faster than the same for loop with append.

Q12. Does the loop variable exist after the loop ends?
Yes. After for i in range(3): pass, i is still 2.

Q. Why do interviewers ask you to solve with a loop when sum() or max() exists?
To check if you understand the logic behind it. In real work, use built-in functions.


Example 2: Infinite while Loop
If the condition is always True, the loop will run indefinitely (infinite loop), unless a break
statement is used to exit the loop manually.

Nested loop is a loop placed inside another loop. Both while and for loops can be nested, and 
they allow you to solve problems requiring iteration over multiple dimensions.

Part 6: Loops in Data Science Interviews

1. Loops vs Vectorization (the most important DS point)

Q. Why should we avoid Python loops on large data in NumPy and Pandas?
Python loops run one item at a time in slow Python code. NumPy and Pandas operations are vectorized:
 they run on the whole array at once in fast compiled code (C). So they are much faster on big data.

"""

#enumerate function = it is built in function , allows you to loop on a sequence and get the index and value of each elemtn ,
#we can also start fronm 1 by using ( start = 1)


fruits =  [ "apple" , "mango" , "cherry" , "bananna" ]

for f in enumerate(fruits,start=1):
    print(f) 
