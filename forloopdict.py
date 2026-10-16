# this one is for dictionary code 
"""
1. Variable ka naam kuch bhi rakh sakte ho

Haan, eachItem, item, x, banana, college — kuch bhi naam de sakte ho. Python ke liye ye sirf ek temporary label hai jo har loop-round mein current element ko point karta hai. Koi special meaning nahi hai item ya eachItem naam mein — bas readable naam rakhna best practice hai taaki code padhne mein samajh 

for xyz in collegesTuple:
    print(xyz)

Ye bhi bilkul same kaam karega jaisa eachItem wala.
"""
"""
"2. Dict pe for-loop chalta hai kya?

Bilkul chalta hai — bas thoda samajhna padega ki dict pe by default kya milta hai.

python
student = {"name": "Saumya", "age": 21, "course": "BCA"}

for x in student:
    print(x)"

    


    Output:

name
age
course

Dekha? Jab tum seedha for x in student: likhte ho, tumhe sirf keys milti hain, values nahi. Ye bahut common confusion hai beginners mein.
   
 Agar values chahiye ya dono chahiye?

Python teen tarike deta hai dict loop karne ke liye:

Keys chahiye (default):

python
for key in student:
    print(key)

Sirf values chahiye:

python
for value in student.values():
    print(value)

Output: Saumya, 21, BCA

Key aur value dono ek saath chahiye:

python
for key, value in student.items():
    print(key, ":", value)

Output:

name : Saumya
age : 21
course : BCA

Notice yahan .items() use kiya — ye important hai. Isi se Python ko pata chalta hai ki tum pair (key + value) chahte ho, aur isliye for ke baad do variables (key, value) likhne padte hain, ek nahi.

Quick comparison table:
Kya loop karna hai	Syntax
List / Tuple	for item in myList:
Dict — sirf keys	for key in myDict:
Dict — sirf values	for val in myDict.values():
Dict — key aur value dono	for key, val in myDict.items():

Try karo: apna khud ka ek chhota dict banao (jaise {"subject": "Python", "marks": 85}), aur teeno tarike se print karke dekho — keys, values, aur .items() se dono. Bata jab result mile.   
      """

data = {" ashray": 21, "prabh ": 34 , "sus" : 420 }

for key in data:
    print(key, "___this is the key to find key in dict ________")

for value in data.values():
    print(value,"--------- and this is value to find in dict") 

for key, value in data.items():# this is the function use to find both key and values fromthe dict
    print(key,":", value)    
