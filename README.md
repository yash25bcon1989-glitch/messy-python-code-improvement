# Messy Python Code Improvement

An AI-assisted refactoring exercise based on **Lecture 6 — Practical on Code Improvement**. A deliberately messy student-marks program is cleaned up while preserving its output exactly.

## Objective

Demonstrate how AI-assisted tools can improve poorly written Python code without changing what the program does. The project contains two versions of the same program:

| File | Description |
|------|-------------|
| `messy.py` | The original, deliberately messy — but working — program. |
| `refactored.py` | The cleaned-up version with better practices. |
| `original_output.txt` | The exact output produced by running `messy.py`. |

## Problems in the Original Code (`messy.py`)

1. **Unclear names** — Variables like `s1`, `s2`, `a`, `b`, and functions `fn1`, `fn2` give no clue what they represent.
2. **Repeated average calculations** — `fn1` and `fn2` contain identical copy-pasted averaging logic instead of reusing one function.
3. **Repeated hard-coded number** — The value `100` (maximum marks) appears multiple times as a bare literal.
4. **Unused import** — `import math` sits at the top but `math` is never used anywhere in the program.
5. **String concatenation** — Output lines use `+` and `str()` to build strings, which is harder to read than f-strings.

## Refactoring Improvements (`refactored.py`)

| Problem | Fix |
|--------|-----|
| Unclear names | Renamed to `math_mark`, `science_mark`, `average`, `percentage`, `grade`, etc. |
| Repeated averaging | A single `calculate_average()` function replaces `fn1` and `fn2`. |
| Hard-coded `100` | A named constant `MAX_MARKS = 100` is defined once and reused. |
| Unused `math` import | Removed entirely. |
| String concatenation | Replaced with f-strings for readability. |

## Requirements

- **Python 3.7 or later**

No external libraries are needed — both scripts use only built-in Python features.

## How to Run

Open a terminal in this folder and run:

```bash
# Run the messy (original) version
python messy.py

# Run the refactored (improved) version
python refactored.py
```

## Example Output

Both programs produce identical output:

```
===== Student Marks Report =====
Subject: Math - Marks: 78/100
Subject: Science - Marks: 85/100
Subject: English - Marks: 92/100
Average Marks: 85.0
Percentage: 85.0%
Computed Average Again: 85.0
Grade: B
===== End of Report =====
```

## How Output Equivalence Was Checked

The output of `messy.py` was saved to `original_output.txt`. Then `refactored.py` was run and its output was compared against that file using a file-diff check:

```bash
python messy.py > original_output.txt
python refactored.py > refactored_output.txt
diff original_output.txt refactored_output.txt
```

If the `diff` command produces **no output**, the two files are identical — meaning the refactoring preserved the program's behavior exactly. This check passed during development: the outputs matched character for character.

The temporary `refactored_output.txt` file used during the comparison is not included in this submission; only `original_output.txt` is kept as a record of the program's output.

## File Structure

```
messy-python-code-improvement/
├── messy.py              # Original messy program
├── refactored.py         # Cleaned-up version
├── original_output.txt   # Output captured from messy.py
└── README.md             # This file
```

## Author

Yash Sharma — B.Tech Computer Science Engineering (AI & ML specialization)
