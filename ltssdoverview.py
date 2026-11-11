Laying out the revision table's main comparison and methods
Python Data Structures: Final Revision Sheet
1. Main comparison table
Feature	List	Tuple	String	Set	Dictionary
Syntax	[1, 2, 3]	(1, 2, 3)	"abc"	{1, 2, 3}	{"a": 1}
Empty one	[] / list()	() / tuple()	""	set() ({} gives a dict!)	{} / dict()
Ordered?	Yes	Yes	Yes	No	Yes (insertion order, Python 3.7+)
Mutable?	Yes	No	No	Yes	Yes
Duplicates	Allowed	Allowed	Allowed	Not allowed	Keys unique, values can repeat
Indexing x[0]	Yes	Yes	Yes	No	No (access by key)
Slicing x[1:3]	Yes	Yes	Yes	No	No
Stores	Any type	Any type	Only characters	Only hashable items	key-value pairs (keys hashable)
Hashable?	No	Yes (if items are hashable)	Yes	No (frozenset is)	No
Can be dict key / set item?	No	Yes	Yes	No	No
Search (in) speed	O(n)	O(n)	O(n)	O(1) avg	O(1) avg (on keys)
Memory	More	Less than list	Less	More	Most
Speed	Slower than tuple	Faster than list	Fast	Fast for lookup	Fast for lookup
Best use	Changing collection of items	Fixed data, constants, dict keys	Text	Unique items, set math	Mapping, lookup by key
Yaad rakhne ka trick:

Mutable: List, Set, Dict (LSD 😄)
Immutable: Tuple, String
Unordered: only Set
No duplicates: Set (and Dict keys)
2. All important methods
List (11 methods)
Method	Kaam
append(x)	End mein 1 item add
extend(iter)	End mein multiple items add
insert(i, x)	Index i par add
remove(x)	First matching value hatao (ValueError if missing)
pop(i)	Index se hatao and return (default last)
clear()	Sab hata do
index(x)	First index batao
count(x)	Kitni baar aaya
sort()	In-place sort, returns None
reverse()	In-place reverse
copy()	Shallow copy
Tuple (sirf 2 methods)
count(x), index(x).
Single item tuple: (5,). Comma zaroori hai, nahi to woh int ban jayega.

String (immutable, saare methods naya string return karte hain)
Category	Methods
Case	upper(), lower(), title(), capitalize(), swapcase(), casefold()
Clean	strip(), lstrip(), rstrip()
Split/Join	split(), rsplit(), splitlines(), join(), partition(), rpartition()
Search	find() (returns -1 if missing), rfind(), index() (error if missing), rindex(), count(), startswith(), endswith()
Replace	replace(), removeprefix(), removesuffix(), translate()
Check (return True/False)	isalpha(), isdigit(), isnumeric(), isdecimal(), isalnum(), isspace(), isupper(), islower(), istitle(), isidentifier(), isascii(), isprintable()
Align/Format	center(), ljust(), rjust(), zfill(), format(), expandtabs()
Other	encode()
Set
Method	Operator	Kaam
add(x)		1 item add
update(iter)		Multiple items add
remove(x)		Hatao (KeyError if missing)
discard(x)		Hatao (no error if missing)
pop()		Random item hatao
clear(), copy()		
union()	|	Dono ke sab items
intersection()	&	Common items
difference()	-	A mein hai, B mein nahi
symmetric_difference()	^	Jo common nahi hain
issubset(), issuperset(), isdisjoint()	<=, >=	Relationship check
*_update() versions		In-place version (e.g. intersection_update)
Dictionary
Method	Kaam
get(k, default)	Safe access, no KeyError
keys(), values(), items()	Views return karte hain
update(d2)	Merge/overwrite
pop(k)	Key hatao and value return
popitem()	Last inserted pair hatao (LIFO)
setdefault(k, v)	Key hai to value do, nahi to add karke do
fromkeys(keys, v)	Naya dict banao
clear(), copy()	
del d[k]	Key delete
d1 | d2	Merge (Python 3.9+)
3. Common to all (built-in functions)
len(), min(), max(), sum() (numbers only), sorted() (always returns a list), reversed(), enumerate(), zip(), any(), all(), in / not in, for loop iteration.

Operators:

+ (concatenate) works on list, tuple, string.
* (repeat) works on list, tuple, string.
+ and * do not work on set or dict.
4. Interview Q&A (English, easy definitions)
Q1. What is a list?
A list is an ordered, mutable collection of items that can store different data types and allows duplicates.

Q2. What is a tuple, and how is it different from a list?
A tuple is an ordered, immutable collection of items. A list can be changed after creation, but a tuple cannot. Tuples are faster, use less memory, and can be used as dictionary keys.

Q3. What is a set?
A set is an unordered, mutable collection of unique, hashable items. It is mainly used to remove duplicates and perform math operations like union and intersection.

Q4. What is a dictionary?
A dictionary is a collection of key-value pairs where each key is unique and hashable. Values can be of any type and can repeat.

Q5. Why are strings immutable?
Once a string is created, its characters cannot be changed in place. s[0] = 'X' gives a TypeError. Every string method returns a new string. Immutability makes strings hashable, safe to share, and usable as dictionary keys.

Q6. What does “hashable” mean?
An object is hashable if its hash value never changes during its lifetime. Immutable types like int, str, and tuple are hashable. Lists, sets, and dicts are not. Only hashable objects can be set items or dict keys.

Q7. Why is {} not an empty set?
{} creates an empty dictionary. To create an empty set, use set().

Q8. Difference between remove() and discard() in a set?
Both delete an item. remove() raises KeyError if the item is missing, while discard() does not raise an error.

Q9. Difference between sort() and sorted()?
sort() changes the original list in place and returns None. sorted() returns a new sorted list and works on any iterable.

Q10. Difference between append() and extend()?
append() adds one item as a single element (a list inside a list stays nested). extend() adds each element of an iterable separately.

Q11. Difference between find() and index() in a string?
find() returns -1 if not found. index() raises ValueError.

Q12. Why is set/dict lookup faster than list?
Sets and dicts use a hash table, so lookup is O(1) on average. A list checks items one by one, so it is O(n).

Q13. Is a dictionary ordered?
Yes, from Python 3.7 onwards, a dict remembers insertion order. Before that, it was unordered.

Q14. Can a tuple be changed if it contains a list?
The tuple itself cannot change (you cannot replace items), but a mutable object inside it can. t = (1, [2, 3]); t[1].append(4) works. Such a tuple is also not hashable.

Q15. What is a shallow copy vs deep copy?
A shallow copy (copy()) copies the outer container, but inner objects are still shared. A deep copy (copy.deepcopy()) copies everything recursively.

5. Quick coding practice (last-minute check)
python
# 1. Remove duplicates but keep order
nums = [1, 2, 2, 3, 1]
print(list(dict.fromkeys(nums)))      # [1, 2, 3]

# 2. Count frequency
from collections import Counter
print(Counter("banana"))              # Counter({'a': 3, 'n': 2, 'b': 1})

# 3. Reverse a string
print("hello"[::-1])                  # olleh

# 4. Common items of two lists
print(set([1, 2, 3]) & set([2, 3, 4]))   # {2, 3}

# 5. Swap keys and values
d = {"a": 1, "b": 2}
print({v: k for k, v in d.items()})   # {1: 'a', 2: 'b'}
6. One-line summary
List = flexible box 📦 | Tuple = locked box 🔒 | String = locked text 📝 | Set = unique bag 🎒 | Dict = labeled lockers 🗄️

Chahiye to main yeh table PDF cheat-sheet mein bhi bana sakta hoon, print ya mobile par save karne ke liye.

