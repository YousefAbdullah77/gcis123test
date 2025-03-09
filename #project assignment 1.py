#project assignment 1

#part 1 
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Error: Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    if score < 0 or score > 100:
        return "Error: Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
#part 2 
import csv

def process_students(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    print(f"Error: Incorrect format for {row}")
                    continue
                name, score = row
                try:
                    score = int(score)  # Convert to integer
                    print(f"{name}: {calculate_grade(score)}")
                except:
                    print(f"Error: Non-numeric score for {name}")
    except:
        print("Error: File not found. Please provide a valid filename.")

#part 3
    
    import csv

def process_students(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    print(f"Error: Incorrect format for {row}")
                    continue
                name, score = row
                try:
                    score = int(score)  # Convert to integer
                    print(f"{name}: {calculate_grade(score)}")
                except:
                    print(f"Error: Non-numeric score for {name}")
    except:
        print("Error: File not found. Please provide a valid filename.")


#part 4 

def calculate_average_grade(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            scores = []
            for row in reader:
                try:
                    score = int(row[1])  # Convert to integer
                    if score >= 0 and score <= 100:
                        scores.append(score)
                except:
                    continue
            if scores:
                avg_score = sum(scores) // len(scores)
                print(f"Class Average: {calculate_grade(avg_score)}")
            else:
                print("Error: No valid scores found.")
    except:
        print("Error: File not found.")

#part 5

def main():
    while True:
        filename = input("Enter the student records filename: ")
        try:
            process_students(filename)
            calculate_average_grade(filename)
            count_failing_students(filename)
            break
        except:
            print("An error occurred. Please try again.")

#part 6

import pytest
from grading_system import calculate_grade

def test_calculate_grade():
    assert calculate_grade(-5) == "Error: Invalid score"
    assert calculate_grade(90) == "A"
    assert calculate_grade(75) == "C"

