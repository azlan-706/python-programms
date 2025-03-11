def weight_calculator(total, obtain, weight):
    return (obtain / total) * weight if total != 0 else 0
def get_component_marks(component_name):
    print(f"\n{component_name.upper()} Calculation")
    total = float(input("Enter the total marks: "))
    obtain = float(input("Enter the obtained marks: "))
    weight = float(input("Enter the weightage: "))
    weighted_marks = weight_calculator(total, obtain, weight)
    print(f"Weighted marks for {component_name}: {weighted_marks:.2f}")
    return weighted_marks
def calculate_subject_marks(subject_name):
    print(f"\nCalculating marks for {subject_name}")
    total_subject_marks = 0
    total_subject_marks += get_component_marks("Assignment")
    total_subject_marks += get_component_marks("GDB")
    total_subject_marks += get_component_marks("Quiz")
    total_subject_marks += get_component_marks("Midterm")
    total_subject_marks += get_component_marks("Final Exam")
    print(f"Total marks for {subject_name}: {total_subject_marks:.2f}")
    return total_subject_marks
def main():
    num_subjects = int(input("Enter the number of subjects: "))
    grand_total_marks = 0
    for i in range(num_subjects):
        subject_name = input(f"\nEnter the name of subject {i + 1}: ")
        grand_total_marks += calculate_subject_marks(subject_name)
    print(f"\nYour total marks across all subjects are: {grand_total_marks:.2f}")
if __name__ == "__main__":
    main()
