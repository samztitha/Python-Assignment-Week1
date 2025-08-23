# Exercise 3: Student Marks Processor
# Reads student marks from a file, computes overall score,
# assigns grades, creates NumPy structured array,
# sorts by overall, writes to output file, and shows stats.

import numpy as np  # Import NumPy for structured array

# Function to calculate overall marks (60% exam, 40% coursework)
def compute(exam, coursework):
    return 0.6 * exam + 0.4 * coursework

# Function to assign grade
def grade(overall):
    if overall >= 70:
        return "A"
    elif overall >= 60:
        return "B"
    elif overall >= 50:
        return "C"
    elif overall >= 40:
        return "D"
    else:
        return "F"

# Input and output filenames
input_file = "student_marks.txt"
output_file = "student_results.txt"

students = []  # List to store student records

try:
    # Open input file
    with open(input_file, "r") as f:
        for line in f:
            try:
                # Split line into fields
                reg, exam, cw = line.strip().split(",")
                exam, cw = float(exam), float(cw)  # Convert to float

                # Compute overall and grade
                overall = compute(exam, cw)
                grade = grade(overall)

                # Append tuple record
                students.append((reg.strip(), exam, cw, overall, grade))

            except ValueError:
                # Skip lines with bad formatting
                print(f"Skipping invalid line: {line.strip()}")

    # Create structured array
    dtype = [
        ("reg_no", "U10"),
        ("exam", "f4"),
        ("coursework", "f4"),
        ("overall", "f4"),
        ("grade", "U2"),
    ]
    data = np.array(students, dtype=dtype)

    # Sort by overall (descending)
    sorted_data = np.sort(data, order="overall")[::-1]

    # Write results to output file
    with open(output_file, "w") as f:
        f.write("RegNo, Exam, Coursework, Overall, Grade\n")
        for row in sorted_data:
            f.write(f"{row['reg_no']}, {row['exam']}, {row['coursework']}, "
                    f"{row['overall']:.2f}, {row['grade']}\n")

    # Show grade statistics
    grades, counts = np.unique(sorted_data["grade"], return_counts=True)
    print("\nGrade Statistics:")
    for g, c in zip(grades, counts):
        print(f"Grade {g}: {c} student(s)")

    print("\n Processing complete. Results written to", output_file)

except FileNotFoundError:
    print("Input file not found. Please check the file name.")
except Exception as e:
    print("Unexpected error:", e)

