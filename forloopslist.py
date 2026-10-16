"""
1. List — index se access karo

Lists ordered hote hain, matlab har element ka ek fixed position (index) hota hai, 0 se shuru hota hai.

python
fruits = ["apple", "banana", "mango", "grapes"]

print(fruits[0])    # apple  (pehla element)
print(fruits[2])    # mango  (teesra element)
print(fruits[-1])   # grapes (last element — negative index ulta gin ta hai)

Element dhoondhna hai ki list mein hai ya nahi:

python
if "mango" in fruits:
    print("Mango list mein hai")

Element ka index pata karna hai:

python
print(fruits.index("mango"))   # Output: 2
"""

#2. Tuple — same as list, bas immutable
"""
Tuple bhi ordered hai, indexing bilkul list jaisi hi kaam karti hai:

python
colleges = ("NIT-Delhi", "ABES", "BBAU", "IIT-D")

print(colleges[0])       # NIT-Delhi
print(colleges[-1])      # IIT-D
print("ABES" in colleges)   # True
print(colleges.index("BBAU"))  # 2

Farak sirf itna: tuple ke elements change nahi kar sakte (colleges[0] = "X" error dega), list ke kar sakte ho.
"""
"""
3. Set — koi index nahi hota!

Ye sabse important farak hai. Set unordered hota hai — matlab elements ka koi fixed position nahi hota, isliye:

python
skills = {"Python", "SQL", "Pandas"}

print(skills[0])   # ❌ ERROR! TypeError: 'set' object is not subscriptable

Set mein sirf ye check kar sakte ho ki element hai ya nahi, position nahi:

python
if "SQL" in skills:
    print("SQL set mein hai")

Set ko loop se print karoge toh order guarantee nahi hai — kabhi bhi kisi bhi sequence mein aa sakta hai.
"""

"""
4. String — list ki tarah hi index se access hoti hai

String bhi ordered hai — har character ka index hota hai, jaise list:

python
name = "Saumya"

print(name[0])    # S
print(name[-1])   # a
print("umy" in name)   # True — substring check
print(name.index("m"))  # 3
"""