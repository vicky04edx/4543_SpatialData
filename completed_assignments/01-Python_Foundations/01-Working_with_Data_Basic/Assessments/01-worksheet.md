# 📝 Worksheet: 02 - Working with Data

Use this worksheet to review and reinforce your understanding of Python data containers.

---

## 🧠 Section 1: Lists

1. What method adds an item to the end of a list?  
   `Answer:` __________append()____________

2. How can you remove an item from a list by value?  
   `Answer:` _________remove()_________

3. What’s the result of this code?

```python
nums = [2, 4, 6]
nums.append(8)
print(nums)
```

   `Answer:` _____2, 4, 6, 8______

---

### ✏️ Task: List Practice

```python
# Create a list of your top 3 favorite foods.
# Add another food to the list.
# Remove one item and print the list.
```
pets = [rabbit, dog, cat, turtle, hamster]
pets.append("monkey")
pets.remove("cat")
print(pets)

## 🔒 Section 2: Tuples

4. What is a key difference between a list and a tuple?  
   `Answer:` __Lists can change (mutable) and tuple's cannot be changed (immutable)___

5. Can you change the contents of a tuple once it is created? Why or why not?  
   `Answer:` _____No because tupples cannot be changed or modified after their creation____

---

### ✏️ Task: Tuple Practice

```python
# Create a tuple with your favorite 3 numbers.
# Unpack it into three variables and print each.
```
numbers = (28, 22, 4)
a, b, c = numbers
print(numbers)

## 🔑 Section 3: Dictionaries

6. What does the `.get()` method do differently from accessing a key directly?  
   `Answer:` ___.get() returns none if the key doesn't exist instead of causing an error____

7. How do you loop through both keys and values in a dictionary?  
   `Answer:` ___Using .items()_____
---

### ✏️ Task: Dictionary Practice

```python
# Create a dictionary with keys: 'name', 'age', and 'hobby'.
# Print each key and value in the format "key: value".
```
person = { "name": "Vicky","age": 21,"hobby": "singing" }
for key, value in person.items():
    print(f"{key}: {value}")

## 🧾 Submit Checklist

- [x] I practiced creating and modifying lists.
- [x] I understand how tuples are different from lists.
- [x] I accessed and looped through dictionary items.
