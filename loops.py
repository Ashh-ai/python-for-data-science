

# practising loops
#  Python mainly has two loop types:
'''for loop — repeats over a collection or sequence.
while loop — repeats while a condition remains True.
'''
# range in looops (looping a fixed number of times)
"""
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(1, 6):     # 1,2,3,4,5
    print(i)

for i in range(0, 10, 2): # 0,2,4,6,8 (step of 2)
    print(i)
"""

#enumerate() — when you need both index AND value (very common in DS)

"""
students = ["Aditi", "Ravi", "Meena"]

for index, name in enumerate(students):
    print(index, name)
# 0 Aditi
# 1 Ravi
# 2 Meena
"""

#zip() — looping through two lists together (like pairing two data columns)

'''
names = ["Aditi", "Ravi", "Meena"]
marks = [88, 72, 95]

for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")


'''

'''
Loop control keywords
pythonfor score in scores:
    if score < 50:
        continue     # skip this iteration, move to next
    if score == 92:
        break        # stop the loop entirely
    print(score)

continue → skip current item, keep looping
break → exit the loop completely
pass → do nothing (placeholder, keeps code valid while you're still writing it)


''' 
'''
Nested loops (common in DS for grid/matrix operations)
matrix = [[1, 2], [3, 4]]

for row in matrix:
    for value in row:
        print(value)

        '''