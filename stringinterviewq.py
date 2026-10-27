#Q1. Do string methods change the original string?
# No. Strings are immutable, so every method returns a new string. We must save it in a variable.


# Q2. What is the difference between find() and index()?
# Both give the position of a substring. If it is not found, find() returns -1, but index() raises a ValueError.


# 2. strip()

# Matlab: String ke shuru aur aakhir ke extra spaces hata deta hai. Beech ke spaces nahi chhedta.


# strip() removes the extra spaces from the start and the end of a string.


# 3. split()

# Matlab: Ek lambi string ko tukdon mein todta hai aur un tukdon ki list deta hai.

# Analogy: Jaise ek lambi roti ko chaku se kaat ke tukde karna.

# python
# text = "apple banana mango"
# print(text.split())

# Output: ['apple', 'banana', 'mango']

# Kaise chala: Python ne text ko spaces pe kaata. Teen tukde bane, aur teeno ek list [ ] mein aa gaye.

# Agar space ki jagah koi aur cheez (comma) pe todna ho, toh bracket mein batao:

# python
# print("a,b,c".split(","))      # ['a', 'b', 'c']

# Interview mein bolo:

# split() breaks a string into smaller parts and returns them as a list.



# 4 . join()

# Matlab: split() ka ulta. List ke tukdon ko jod ke ek string bana deta hai.

# python
# words = ["apple", "banana", "mango"]
# print("-".join(words))

# Output: apple-banana-mango

# Kaise chala: Jo cheez dot ke pehle hai ("-"), woh jodne wali glue hai. Woh har do items ke beech lag gayi.

# Dhyan do, syntax thoda ulta lagta hai:

# "glue".join(list)

# Aur kuch examples:

# python
# print(" ".join(words))      # apple banana mango   (space se jodo)
# print("".join(words))       # applebananamango     (bina kuch beech mein)

# Ek galti jo log karte hain: List ke andar sab items string hone chahiye. "-".join([1, 2, 3]) error dega, kyunki 1, 2, 3 numbers hain.

# Interview mein bolo:

# join() combines the items of a list into one string, using a separator between them.4


# 5. find()

# Matlab: String ke andar koi cheez dhoondhta hai aur batata hai ki woh kaunse index (position) pe mili.

# h   e   l   l   o
# 0   1   2   3   4
# python
# s = "hello"
# print(s.find("l"))     # 2
# print(s.find("o"))     # 4
# print(s.find("z"))     # -1

# Kaise chala:

# "l" pehli baar index 2 pe mila. (Dusra l index 3 pe hai, par find sirf pehla batata hai.)
# "o" index 4 pe mila.
# "z" string mein hai hi nahi, toh jawab -1 aaya. -1 ka matlab “mila nahi”.

# Interview mein bolo:

# find() returns the index of the first match. If the text is not found, it returns -1.


# 6. replace()

# Matlab: String ke andar ek hissa dhoondh ke doosre se badal deta hai (find and replace, jaise Word mein hota hai).

# python
# s = "I like cats and cats like me"
# print(s.replace("cats", "dogs"))

# Output: I like dogs and dogs like me

# Kaise chala: "cats" jitni baar aaya, har baar "dogs" ban gaya. Original s waisa hi raha, kyunki yeh bhi nayi copy deta hai.

# Syntax: string.replace(purana, naya)

# Interview mein bolo:

# replace() returns a new string where every old part is replaced with a new part.



# 7. Method chaining

# Matlab: Ek ke baad ek method ek hi line mein laga dena. Python unhe left se right chalata hai, aur har method ko pichhle ka result milta hai.

# python
# s = "   HELLO   "
# print(s.strip().lower())

# Kaise chala (step by step):

# Step	Kaam	Result
# 1	s.strip()	"HELLO"
# 2	us pe .lower()	"hello"

# Output: hello

# Order ka dhyan rakho: Har step ko pichhle step ka result chahiye.

# Interview mein bolo:

# Method chaining means calling one method after another in a single line. Each method works on the result of the previous one.