# 📝 Worksheet: 03 - Scalar Types and Control Flow

Use this worksheet to reinforce your understanding of variables, comparisons, and decision logic.

---

## 🧠 Section 1: Scalar Types

1. What is the output of the following code?

```python
x = 10
print(type(x))
```

`Answer:` ____<class 'int'>_____

2. What scalar type would best represent:
   - A person's name: ___string___
   - Their age: ___integer___
   - Whether they passed a test: ___bool___

---

### ✏️ Task: Type Practice

```python
# Create a variable for each type and print its value and type
# Example: an int, float, str, and bool
```

---

## 🔁 Section 2: Comparison Operators

3. What does the `!=` operator mean?

`Answer:` ____not equal to________

4. What will the following code print?

```python
a = 5
b = 3
print(a < b or b < 10)
```

`Answer:` _____True_______

---

## 🔀 Section 3: Control Flow

5. Write a conditional that prints "Pass" if a grade is >= 70, and "Fail" otherwise.

```python
grade = 75
if grade >= 70:
    print("Pass")
else:
    print("Fail")
```

6. What does `elif` allow you to do?

`Answer:` ____Lets you check more conditions after an if statement_______________

---

### ✏️ Task: Your Turn

Write a program that asks for the weather and prints:
- "Bring sunscreen" if it's sunny
- "Take an umbrella" if it's raining
- "Check the forecast" otherwise


weather = input("What is the weather like? ")
  if weather == "sunny":
     print("Bring sunscreen")
  elif weather == "raining":
     print("Take an umbrella")
  else:
     print("Check the forecast")

