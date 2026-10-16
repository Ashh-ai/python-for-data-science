#range 
"""
range() creates numbers one by one; it does not usually store a full list in memory.
1. range(stop)
for i in range(5):
    print(i)
Output:
0
1
2
3
4
range(5) starts at 0 by default and stops before 5.

"""

#for pa in range(5):
  #  print(pa)
#for fi in range(8):
 #   print(fi, " we can take any var like fi")    
# range( start , stop )
"""
2. range(start, stop)
for i in range(2, 7):
    print(i)
Output:
2
3
4
5
6
Here:
2 is included
7 is excluded
range(2, 7)
means:
2, 3, 4, 5, 6
"""
#for pu in range(5,15):
 #   print(pu)


# range (start,stop,step)
"""
3. range(start, stop, step)
The third value is the step: how much the number changes each time.
for i in range(0, 11, 2):
    print(i)
Output:
0
2
4
6
8
10
range(0, 11, 2)
means:
Start from 0
Stop before 11
Add 2 each time

"""
# example
#for i in range(2,22,3):
#    print(i)
"""
4. Counting backwards with a negative step
Use a negative step to decrease values.
for i in range(10, 0, -1):
    print(i)
Output:
10
9
8
7
6
5
4
3
2
1
This means:
Start at 10
Stop before 0
Subtract 1 every time
To include 0:"""

"""
#for i in range(20,0,-2):
 #   print(i)
for i in range(20,-5,-2):
    print(i)

for i in range (20,-5,-1): # if we put stop a negative number vo vha tak jayega chahe negative

    print(i) 
    """



#range(1, 10, 1)    # forward
#range(10, 1, -1)   # backward

"""
1. break — stop the loop completely
Use break when you want to exit a loop immediately.
scores = [70, 82, 95, 40, 88]

for score in scores:
    if score == 40:
        print("Invalid score found:", score)
        break

    print("Valid score:", score)
Output:
Valid score: 70
Valid score: 82
Valid score: 95
Invalid score found: 40
Once Python reaches break, the entire loop ends. It does not check 88.
Data-science use case: stop processing when you find a critical invalid value.
data = [12, 15, 18, -999, 20]

for value in data:
    if value == -999:
        print("Missing-value marker found. Stopping.")
        break
    print(value)
2. continue — skip only the current iteration
Use continue when you want to ignore the current value and move to the next one.
ages = [22, None, 31, None, 45]

for age in ages:
    if age is None:
        continue

    print("Valid age:", age)
Output:
Valid age: 22
Valid age: 31
Valid age: 45
When Python sees None, it skips the rest of that loop iteration and continues with the next item.
Data-science use case: skip missing or invalid data.
temperatures = [28.4, -999, 30.1, 29.5, -999]

for temp in temperatures:
    if temp == -999:
        continue

    print("Temperature:", temp)
3. pass — do nothing for now
pass is a placeholder. It lets you write syntactically valid code where Python expects an indented block, even though you have not added real logic yet.
for i in range(5):
    pass

print("Loop completed")
The loop runs five times, but nothing happens inside it.
Example with a function you will write later:
def clean_data(data):
    pass
Python will accept this function, but it currently has no behavior.
pass does not skip the current iteration. It literally does nothing, then execution naturally proceeds to the next line.
for number in range(1, 4):
    if number == 2:
        pass
    print(number)
Output:
1
2
3
Even when number is 2, print(number) still runs because pass changes nothing.
"""