def main():
    all_students = {"Alice", "John", "Sara", "Bob"}
    attended_students = {"Alice", "Bob"}
    absent_students = all_students - attended_students
    print(absent_students)

if __name__ == "__main__":
    main()