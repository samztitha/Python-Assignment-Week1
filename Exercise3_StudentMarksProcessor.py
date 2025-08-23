# Exercise 3: Student Marks Processor
# Author: Samztitha
# This program reads student marks, calculates overall scores,
# assigns grades, sorts results, and saves everything into a file.

import numpy as np

try:
    # Step 1: Read input file
    # File should have lines like: 101,78,66  → reg_no, theory, assignment
    input_file = "student_input.txt"
    output_file = "student_results.txt"

    students = []
    with open(input_file, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue  # skip invalid rows
            reg_no, theory_score, assignment_score = parts
            students.append((reg_no.strip(),
                             float(theory_score),
                             float(assignment_score)))

    # Step 2: Calculate overall marks
    # Formula: theory is weighted more than assignment
    results = []
    for reg_no, theory_score, assignment_score in students:
        total = (theory_score * 3 + assignment_score * 2) / 5

        # Step 3: Assign grades
        if total >= 90:
            grade = "Outstanding"
        elif total >= 75:
            grade = "Excellent"
        elif total >= 60:
            grade = "Good"
        elif total >= 40:
            grade = "Pass"
        else:
            grade = "Fail"

        results.append((reg_no, theory_score, assignment_score, total, grade))

    # Step 4: Convert into NumPy structured array
    dtype = [('RegNo', 'U10'), ('Theory', 'f4'),
             ('Assignment', 'f4'), ('Total', 'f4'), ('Grade', 'U15')]
    data = np.array(results, dtype=dtype)

    # Step 5: Sort by total marks (descending)
    sorted_data = np.sort(data, order='Total')[::-1]

    # Step 6: Write results to output file
    with open(output_file, "w") as f:
        f.write("RegNo | Theory | Assignment | Total | Grade\n")
        f.write("-" * 50 + "\n")
        for row in sorted_data:
            f.write(f"{row['RegNo']:>5} | {row['Theory']:>6.1f} | {row['Assignment']:>9.1f} | "
                    f"{row['Total']:>5.1f} | {row['Grade']}\n")

    # Step 7: Show grade statistics
    print("=== Grade Statistics ===")
    grades, counts = np.unique(sorted_data['Grade'], return_counts=True)
    for g, c in zip(grades, counts):
        print(f"{g}: {c} student(s)")

    print("\nProcessing complete. Results saved in:", output_file)

except FileNotFoundError:
    print("Error: Input file not found. Please make sure 'student_input.txt' exists.")
except ValueError:
    print("Error: Invalid data format in file.")
except Exception as e:
    print("Unexpected error:", e)
