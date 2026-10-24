"""
Messy Student Marks Program (BEFORE refactoring)
=================================================
This program is intentionally written with poor practices so it can be
refactored in refactored.py. Do NOT use this as a style reference.

Deliberate problems (for the refactoring exercise):
  1. Unclear names: s1, s2, s3, a, b, fn1, fn2, etc.
  2. Repeated average calculations — the averaging logic is copy-pasted.
  3. A repeated hard-coded number (100) used for percentage conversion.
  4. An unused import (math) sitting at the top.
  5. String concatenation with + and str() instead of f-strings.
"""

import math  # unused import — never called anywhere below


def fn1(x, y, z):
    # calculates average of three numbers (but the name tells you nothing)
    t = x + y + z
    a = t / 3
    return a


def fn2(x, y, z):
    # same average logic, copy-pasted instead of reused  (repeated code)
    t = x + y + z
    a = t / 3
    return a


# ---- Student marks (out of 100) ----
s1 = 78
s2 = 85
s3 = 92

# ---- Subject names ----
n1 = "Math"
n2 = "Science"
n3 = "English"

print("===== Student Marks Report =====")
print("Subject: " + n1 + " - Marks: " + str(s1) + "/" + str(100))
print("Subject: " + n2 + " - Marks: " + str(s2) + "/" + str(100))
print("Subject: " + n3 + " - Marks: " + str(s3) + "/" + str(100))

# Average using fn1
a = fn1(s1, s2, s3)
print("Average Marks: " + str(a))

# Convert to percentage — hard-coded 100 repeated again
p = (a / 100) * 100
print("Percentage: " + str(p) + "%")

# Average computed AGAIN using fn2 instead of reusing the first result
b = fn2(s1, s2, s3)
print("Computed Average Again: " + str(b))

# Determine grade
if p >= 90:
    g = "A"
elif p >= 80:
    g = "B"
elif p >= 70:
    g = "C"
elif p >= 60:
    g = "D"
else:
    g = "F"

print("Grade: " + g)
print("===== End of Report =====")
