# tuple 

# A tuple is an ordered collection of items that cannot be changed after it is created. 
# It is written with round brackets and can hold duplicates and different data types.

# t1 = (1, 2, 3)         # normal
# t2 = ()                # khali tuple
# t3 = 1, 2, 3           # bina brackets ke bhi tuple ban jaata hai
# t4 = tuple([1, 2, 3])  # list se tuple

# # 
# A single-item tuple needs a trailing comma, like (5,).
# Without the comma, Python treats it as a normal value in brackets


# 2. Immutability (badal nahi sakte)
# python
# t = (10, 20, 30)
# t[1] = 99

# Error: TypeError: 'tuple' object does not support item assignment

# Isliye tuple ke paas append, remove, sort, pop jaise methods nahi hain. Sirf do methods hain:

# python
# t = (10, 20, 20, 30)
# print(t.count(20))     # 2   (20 kitni baar aaya)
# print(t.index(20))     # 1   (pehla 20 kis index pe)

# Interview mein bolo:

# Tuples are immutable. We cannot add, remove or change items. They have only two methods: count() and index().



# Tuple
# Pehle base samjho

# Tuple list jaisa hi hota hai, bas lock laga hua. Ek baar bana diya toh badal nahi sakte (na item badalna, na jodna, na hatana).

# Analogy:

# List = pencil se likhi shopping list. Jab chaho mita ke badal do.
# Tuple = pen se likha aur laminate kiya hua card. Ek baar ban gaya, ab badlega nahi.

# Tuple round brackets ( ) mein likhte hain:

# python
# point = (10, 20)
# colors = ("red", "green", "blue")
# mixed = (1, "hello", 3.14, True)

# Indexing aur slicing list jaisi hi hoti hai (t[0], t[-1], t[1:3]), toh woh hum dobara nahi padhenge.

# Easy Definition:

# A tuple is an ordered collection of items that cannot be changed after it is created. It is written with round brackets and can hold duplicates and different data types.

# 1. Tuple banana (aur ek bahut famous trap)
# python
# t1 = (1, 2, 3)         # normal
# t2 = ()                # khali tuple
# t3 = 1, 2, 3           # bina brackets ke bhi tuple ban jaata hai
# t4 = tuple([1, 2, 3])  # list se tuple

# Trap: ek item wala tuple

# python
# a = (5)
# b = (5,)
# print(type(a))     # <class 'int'>
# print(type(b))     # <class 'tuple'>

# Kyun? (5) mein brackets sirf grouping ke liye hain, jaise maths mein (5) + 2. Python ko tuple tab samajh aata hai jab comma ho. Tuple ko tuple banata hai comma, bracket nahi.

# Interview mein bolo:

# A single-item tuple needs a trailing comma, like (5,). Without the comma, Python treats it as a normal value in brackets.

# 2. Immutability (badal nahi sakte)
# python
# t = (10, 20, 30)
# t[1] = 99

# Error: TypeError: 'tuple' object does not support item assignment

# Isliye tuple ke paas append, remove, sort, pop jaise methods nahi hain. Sirf do methods hain:

# python
# t = (10, 20, 20, 30)
# print(t.count(20))     # 2   (20 kitni baar aaya)
# print(t.index(20))     # 1   (pehla 20 kis index pe)

# Interview mein bolo:

# Tuples are immutable. We cannot add, remove or change items. They have only two methods: count() and index().

# 3. Ek catch: tuple ke andar list ho toh

# Tuple lock hai, par agar uske andar list hai, toh us list ko badal sakte hain.

# python
# t = (1, [2, 3], 4)
# t[1][0] = 99
# print(t)               # (1, [99, 3], 4)

# Kaise chala: Tuple ne sirf yeh pakda hua hai ki “index 1 pe wahi list hai”. Us list ke andar ka content badalna allowed hai. Tuple ko doosri list se replace karna allowed nahi hai.

# python
# t[1] = [7, 8]          # TypeError ❌

# Interview mein bolo:

# A tuple is immutable, but if it holds a mutable object like a list, the inside of that list can still change.

# 4. Jodna aur repeat karna
# python
# a = (1, 2)
# b = (3, 4)
# print(a + b)       # (1, 2, 3, 4)
# print(a * 3)       # (1, 2, 1, 2, 1, 2)

# Yahan tuple badla nahi, nayi tuple bani. a aur b waise hi hain.

# python
# t = (1, 2)
# t += (3,)          # chalta hai
# print(t)           # (1, 2, 3)

# Yeh bhi chalta hai kyunki t ko nayi tuple de di gayi (purani tuple nahi badli).

# 5. Packing aur Unpacking (interview ka favourite)

# Packing: Kai values ko ek tuple mein rakh dena.
# Unpacking: Tuple ke items ko alag-alag variables mein nikalna.

# python
# person = ("Ashray", 20, "Delhi")     # packing

# name, age, city = person              # unpacking
# print(name)    # Ashray
# print(age)     # 20

# Kaise chala: Pehla item name ko, doosra age ko, teesra city ko mila. Variables ki ginti items ke barabar honi chahiye, warna ValueError aata hai.

# Swap trick (yaad hai?):

# python
# a, b = 5, 10
# a, b = b, a
# print(a, b)    # 10 5

# Yeh asal mein tuple packing aur unpacking hi hai. Temporary variable ki zaroorat nahi padti.

# Star ke saath (*) baaki sab pakdo:

# python
# first, *rest = (1, 2, 3, 4)
# print(first)   # 1
# print(rest)    # [2, 3, 4]   (yeh list ban jaati hai)

# Function se kai values return karna:

# python
# def stats(nums):
#     return min(nums), max(nums)      # tuple return hota hai

# low, high = stats([4, 9, 2])
# print(low, high)    # 2 9

# Interview mein bolo:

# Packing means putting several values into one tuple. Unpacking means assigning the items of a tuple to separate variables. A function that returns multiple values actually returns a tuple.

# 6. Tuple kyun use karte hain, jab list hai?
# Wajah	Matlab
# Safe data	Galti se badal nahi sakta (jaise coordinates, dates, config)
# Thoda tez aur kam memory	List se halka hota hai
# Dictionary key ban sakta hai	List key nahi ban sakti, tuple ban sakta hai
# Multiple return values	Function tuple hi return karta hai
# python
# locations = {(28.6, 77.2): "Delhi", (19.0, 72.8): "Mumbai"}
# print(locations[(28.6, 77.2)])     # Delhi
# Interview Preparation (60%)
# Part 1: Easy Definitions
# Tuple: An ordered collection of items that cannot be changed after creation.
# Immutable: Cannot be changed after it is created.
# Packing: Putting multiple values into one tuple.
# Unpacking: Taking the items out of a tuple into separate variables.
# Hashable: An object that never changes, so it can be used as a dictionary key or a set item. Tuples (of hashable items) are hashable, lists are not.
# Part 2: Theory Q&A

# Q1. What is the difference between a list and a tuple?

# Feature	List	Tuple
# Brackets	[ ]	( )
# Mutable?	Yes	No
# Methods	Many (append, sort...)	Only count, index
# Speed and memory	Slightly slower, more memory	Slightly faster, less memory
# Dictionary key?	No	Yes
# Use when	Data changes	Data should stay fixed

# Q2. How do you create a tuple with one item?
# Add a comma: (5,). Without the comma, (5) is just the number 5.

# Q3. Can we change a tuple?
# No. But we can create a new tuple from an old one: t = t + (4,).

# Q4. How do you “change” an item in a tuple?
# Convert it to a list, change it, and convert it back.

# python
# t = (1, 2, 3)
# temp = list(t)
# temp[0] = 99
# t = tuple(temp)
# print(t)        # (99, 2, 3)

# Q5. Why can a tuple be a dictionary key but a list cannot?
# A dictionary key must be hashable (it must never change). A tuple cannot change, so it is hashable. A list can change, so it is not.

# Q6. Is a tuple always completely immutable?
# The tuple itself cannot change, but if it contains a mutable object like a list, that object can change.

# Q7. What is tuple unpacking? Give an example.
# It assigns the items of a tuple to variables in one line: x, y = (10, 20).

# Q8. When would you use a tuple in data analysis?
# For fixed records like (name, age), coordinates (lat, long), dictionary keys made of two values, and for returning multiple results from a function.

# Part 3: Output-Based Questions (worked examples)

# Example 1: Brackets vs comma

# python
# print(type((5)))
# print(type((5,)))

# Output: <class 'int'> then <class 'tuple'>.

# Example 2: Error

# python
# t = (1, 2, 3)
# t[0] = 10

# Output: TypeError. A tuple does not support item assignment.

# Example 3: List inside tuple

# python
# t = (1, [2, 3])
# t[1].append(4)
# print(t)

# Output: (1, [2, 3, 4]). The tuple did not change, only the list inside it.

# Example 4: Unpacking with star

# python
# a, *b = (1, 2, 3)
# print(a, b)

# Output: 1 [2, 3].

# Example 5: Repetition

# python
# print((1, 2) * 2)

# Output: (1, 2, 1, 2).

# Part 4: Tricky Questions
# What is type(())? tuple. An empty pair of brackets is an empty tuple.
# What is tuple("abc")? ('a', 'b', 'c').
# Can this work: d = {[1, 2]: "x"}? No, TypeError: unhashable type: 'list'.
# Can this work: d = {(1, [2]): "x"}? No. The tuple holds a list, so it is not hashable. A tuple is hashable only if all its items are hashable.
# Is (1, 2, 3) == (1, 2, 3) true? Yes. Tuples are compared by values, item by item.
# Part 5: Little Coding Practice (hints only)
# #	Problem	Level	First hint
# 1	Swap two numbers using a tuple	Easy	a, b = b, a
# 2	Count how many times a value appears in a tuple	Easy	.count()
# 3	Convert a tuple to a list, add an item, and convert back	Easy	list() and tuple()
# 4	Write a function that returns both the minimum and maximum of a list	Medium	return min(x), max(x)
# 5	Given [(“Riya”, 80), (“Aman”, 65)], print each name and mark	Medium	Loop with unpacking: for name, mark in data:

# Jab try karo, code bhej dena, main review kar dunga.

# Part 6: Revision Sheet
# Tuple = list jaisa, par badal nahi sakte, ( ) mein
# Ek item wala tuple: comma zaroori, (5,)
# Sirf 2 methods: count(), index()
# Tuple ke andar list ho toh list badal sakti hai
# Unpacking: a, b, c = t, star: first, *rest = t
# Tuple dictionary key ban sakta hai (list nahi)
# Function kai values return kare toh woh tuple hota hai
# Tumhare liye sawaal (Step 7)

# Sirf ek sawaal:

# python
# x = (7)
# y = (7,)
# print(type(x))
# print(type(y))

# Dono lines ka output kya aayega, aur kyun? Yaad rakho: tuple ko tuple kaun banata hai, bracket ya comma? “Nahi pata” bhi theek hai. 🙂

# (Pending: list wala b = a aur c = a.copy() ka sawaal bhi, jab time mile.)