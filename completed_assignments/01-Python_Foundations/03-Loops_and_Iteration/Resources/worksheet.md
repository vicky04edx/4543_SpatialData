# 📝 Worksheet: 04 - Loops and Iteration

Practice and reflect on how loops work in Python.

---

## 🔁 Section 1: For Loops

1. What does `range(5)` produce?

`Answer:` _____0, 1, 2, 3, 4_____

2. Write a `for` loop that prints numbers 1 to 10, but skips 5.

```python
# Your code:

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

---

## 🔁 Section 2: While Loops

3. What’s the difference between a `for` loop and a `while` loop?

`Answer:` _____A foor loop iterartes over a sequence, and a while loop iterates over and over again whie the condition is true_______

4. What happens if a `while` loop's condition never becomes `False`?

`Answer:` ____It creates an infinite loop and runs forever______

---

### ✏️ Task: Countdown with While

```python
# Use a while loop to count down from 5 to 1.
```
---
    i = 5

    while i >= 1:
        print(i)
        i -= 1
## 📁 Section 3: File Reading and `with`

5. What does the `with` statement do when opening a file?

`Answer:` ______It handles automatically opening and closing the file safely_______

6. How do you loop over each line in a file?

`Answer:` ____Use a for loop: for line in file______

---

### ✏️ Task: File Filter

Write code that prints only the lines in a file that contain the word `"error"`.

```python
# Your code here
with open("file.txt", "r") as file:
    for line in file:
        if "error" in line:
            print(line.strip())
```
