import numpy as np

# Sample student data (Reg, Exam Mark, Coursework Mark)
data = [
    ("101", 78, 65),
    ("102", 55, 60),
    ("103", 90, 85),
    ("104", 40, 30),
    ("105", 72, 68),
]

students = []

for reg, exam, course in data:
    # Overall = 70% Exam + 30% Coursework
    overall = exam * 0.7 + course * 0.3

    # Assign grade
    if overall >= 70:
        grade = "A"
    elif overall >= 50:
        grade = "B"
    else:
        grade = "C"

    students.append((reg, exam, course, overall, grade))

# NumPy structured array (like a small table)
dtype = [("Reg", "U10"), ("Exam", "f4"), ("Course", "f4"), ("Overall", "f4"), ("Grade", "U1")]
arr = np.array(students, dtype=dtype)

# Sort by Overall marks (highest first)
sorted_arr = np.sort(arr, order="Overall")[::-1]

# Show results
print("✅ Student Results (sorted by Overall):\n")
for s in sorted_arr:
    print(f"Reg: {s['Reg']}, Exam: {s['Exam']}, Course: {s['Course']}, Overall: {s['Overall']:.1f}, Grade: {s['Grade']}")
