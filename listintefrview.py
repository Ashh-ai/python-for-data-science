# Q1. What is append() in Python?
# append() is used to add a single element to the end of a list.
# Example: list.append(10)
# Q2. What is extend() in Python?
# extend() is used to add multiple elements from an iterable to the end of a list.
# Example: list.extend([10, 20, 30])
# Easy difference to remember:
# - append() → Adds one element as a single item.
# - extend() → Adds elements individually from an iterable.



# reomve and pop interview
# Q1. What is remove() in Python?

# remove() is used to remove the first occurrence of a specified value from a list.

# Example: list.remove(10)

# Q2. What is pop() in Python?

# pop() is used to remove and return an element from a list by its index. By default, it removes the last element.



# Pehle base samjho

# List = ek shopping list jaisi cheez. Isme kai items ek order mein hote hain, aur sab square brackets [ ] ke andar likhte hain.

# python
# fruits = ["apple", "banana", "mango"]
# numbers = [10, 20, 30]
# mixed = [1, "hello", 3.14, True]

# List ki 4 khaas baatein:

# Baat	Matlab
# Ordered	Items ka ek fixed order hota hai (index 0, 1, 2...)
# Mutable	Banne ke baad badal sakte hain
# Duplicates allowed	Ek item kai baar aa sakta hai: [1, 1, 2]
# Mixed types	Number, text, sab ek saath ho sakte hain

# String se sabse bada farak (yeh yaad rakho):

# String = photocopy wala kaam. Method purani string chhedta nahi, nayi deta hai.
# List = original page pe seedha likhna. Method list ko wahin badal deta hai.
# python
# nums = [1, 2, 3]
# nums.append(4)
# print(nums)       # [1, 2, 3, 4]   (original hi badal gaya)

# Interview mein bolo:

# A list is an ordered collection of items that can be changed. It can hold duplicate values and different data types.

# 1. Item badalna

# Matlab: Index se kisi item ko naya value de do.

# python
# numbers = [10, 20, 30, 40]
# numbers[2] = 99
# print(numbers)      # [10, 20, 99, 40]

# Kaise chala: Index 2 pe 30 tha. Wahan 99 rakh diya. Baaki items waise hi rahe.

# (Yahi kaam string pe karte toh error aata. Yahi list aur string ka farak hai.)

# Interview mein bolo:

# Lists are mutable, so we can change an item using its index.

# 2. append()

# Matlab: List ke aakhir mein ek item jod do.

# python
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)      # [1, 2, 3, 4]

# Kaise chala: 4 seedha list ke end mein lag gaya. Ek baar mein sirf ek item jodta hai.

# Interview mein bolo:

# append() adds one item at the end of the list.

# 3. insert()

# Matlab: Kisi khaas position pe item daalo.

# Syntax: list.insert(position, item)

# python
# numbers = [1, 2, 3]
# numbers.insert(1, 99)
# print(numbers)      # [1, 99, 2, 3]

# Kaise chala: Index 1 pe 99 aa gaya. Jo items wahan the (2, 3), woh ek kadam aage khisak gaye.

# Interview mein bolo:

# insert() adds an item at a chosen position. The other items move forward.

# 4. extend()

# Matlab: Kai items ek saath end mein jodo (ek doosri list ke items).

# python
# numbers = [1, 2, 3]
# numbers.extend([4, 5, 6])
# print(numbers)      # [1, 2, 3, 4, 5, 6]

# Kaise chala: [4, 5, 6] ke har item ko alag-alag jod diya.

# append vs extend (interview ka favourite):

# python
# a = [1, 2]
# a.append([3, 4])
# print(a)            # [1, 2, [3, 4]]   (poori list ek item ban gayi)

# b = [1, 2]
# b.extend([3, 4])
# print(b)            # [1, 2, 3, 4]     (items alag-alag jude)

# Yaad rakhne ka trick: append = ek dabba poora ka poora rakh do. extend = dabba kholke saman nikal ke rakh do.

# Interview mein bolo:

# append() adds its argument as one single item. extend() adds each item of an iterable separately.

# 5. remove()

# Matlab: Value batao, woh item hata do. Agar value kai baar hai, toh sirf pehli wali hatata hai.

# python
# numbers = [10, 20, 30, 20, 40]
# numbers.remove(20)
# print(numbers)      # [10, 30, 20, 40]

# Kaise chala: Pehla 20 gaya, doosra 20 waise hi raha.

# Dhyan: Jo value list mein hai hi nahi, use remove() karoge toh ValueError aayega.

# Interview mein bolo:

# remove() deletes the first item that matches the given value.

# 6. pop()

# Matlab: Index batao, woh item hata do aur hataya hua item wapas bhi de do. Index nahi doge toh aakhri item hatata hai.

# python
# numbers = [10, 20, 30]
# x = numbers.pop(1)
# print(x)            # 20
# print(numbers)      # [10, 30]

# y = numbers.pop()   # bina index ke: aakhri item
# print(y)            # 30

# Kaise chala: pop(1) ne index 1 wala 20 nikala, hum use x mein pakad sake. pop() ne last item 30 nikala.

# remove vs pop:

# 	remove()	pop()
# Kya dete ho	Value	Index
# Hataya hua item wapas deta hai?	Nahi	Haan

# Interview mein bolo:

# pop() removes an item by its index and returns it. Without an index, it removes the last item.

# 7. del

# Matlab: Index (ya slice) se item delete kar do. Yeh method nahi, ek keyword hai.

# python
# numbers = [10, 20, 30, 40, 50]
# del numbers[2]
# print(numbers)      # [10, 20, 40, 50]

# del numbers[1:3]
# print(numbers)      # [10, 50]

# Kaise chala: Pehle index 2 (30) gaya. Phir numbers[1:3] yaani 20 aur 40 dono ek saath gaye.

# Interview mein bolo:

# del deletes an item or a slice by index. It does not return the deleted value.

# 8. sort()

# Matlab: List ke items ko chhote se bade (ascending) order mein laga deta hai.

# python
# numbers = [30, 10, 50, 20]
# numbers.sort()
# print(numbers)              # [10, 20, 30, 50]

# numbers.sort(reverse=True)
# print(numbers)              # [50, 30, 20, 10]

# Kaise chala: sort() ne original list ko hi order mein laga diya. reverse=True se bade se chhote order mila.

# Ek bahut common galti:

# python
# numbers = [3, 1, 2]
# print(numbers.sort())       # None   ❌

# sort() list ko badalta hai par kuch return nahi karta (None). Isliye x = numbers.sort() mat likhna.

# Agar original list safe rakhni ho: sorted() use karo, yeh nayi list deta hai.

# python
# a = [3, 1, 2]
# b = sorted(a)
# print(a)    # [3, 1, 2]   (original waisa hi)
# print(b)    # [1, 2, 3]

# Interview mein bolo:

# sort() arranges the list in order and changes the original list. sorted() returns a new sorted list and keeps the original unchanged.

# 9. Chhote methods: reverse(), count(), index(), clear()
# python
# nums = [10, 20, 20, 30]

# print(nums.count(20))     # 2   (20 kitni baar aaya)
# print(nums.index(20))     # 1   (20 pehli baar kis index pe)

# nums.reverse()
# print(nums)               # [30, 20, 20, 10]   (list ulti ho gayi)

# nums.clear()
# print(nums)               # []   (sab hata diya)
# Method	Kaam
# count(x)	x kitni baar hai
# index(x)	x ka pehla index
# reverse()	List ko ulta kar do (wahin)
# clear()	Saare items hata do

# Dhyan: index() mein value nahi mili toh ValueError aata hai (string ke find() ki tarah -1 nahi aata).

# Interview mein bolo:

# count() tells how many times a value appears. index() gives the position of its first match.

# 10. len() aur loop
# python
# fruits = ["apple", "banana", "mango"]
# print(len(fruits))          # 3

# for f in fruits:
#     print(f)

# len() batata hai ki list mein kitne items hain. for loop list ke har item ko ek-ek karke deta hai.

# 11. Nested list (list ke andar list)

# Matlab: List ke andar items bhi list ho sakte hain. Table (rows aur columns) jaisa data aise store hota hai.

# python
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0])        # [1, 2, 3]
# print(matrix[1][2])     # 6

# Kaise chala:

# matrix[0] → pehli row poori: [1, 2, 3]
# matrix[1][2] → pehle row 1 ([4, 5, 6]), phir uska index 2 (6)

# Yaad rakho: pehla number row, doosra number column.

# Interview mein bolo:

# A nested list is a list that contains other lists. We use two indexes to reach an inner item.

# Summary table
# Kaam	Method	Kya hota hai
# End mein 1 item	append(x)	Ek item jode
# Kisi position pe	insert(i, x)	Index i pe daale
# Kai items	extend(list)	Alag-alag jode
# Value se hatao	remove(x)	Pehla x hataye
# Index se hatao + wapas lo	pop(i)	Hataye aur return kare
# Index/slice se delete	del l[i]	Delete kare
# Order mein lagao	sort()	Wahin sort, None return
# Ulta karo	reverse()	Wahin ulta