## CSC500 Module 7 - Critical Thinking
## Sonya Bourgeois
## 06/16/2024

# Create COURSE ROOMS dictionary.
course_rooms = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}
# Create INSTRUCTORS dictionary.
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}
# Create COURSE TIMES dictionary.
course_times = {
    "CSC101": "8:00 AM",
    "CSC102": "9:00 AM",
    "CSC103": "10:00 AM",
    "NET110": "11:00 AM",
    "COM241": "1:00 PM"
}
# Display options and process input choices.
while True:
    print("\nOptions:")
    print("1. Display all course information")
    print("2. Look up course information")
    print("3. Exit")
    choice = input("Choose an option: ")    
# Display details for all courses - room number, instructor, course time. 
    if choice == '1':
        print("Course\tRoom\tInstructor\tTime")
        for course in course_rooms:  # Assuming all dictionaries have the same keys
            room = course_rooms[course]
            instructor = course_instructors[course]
            time = course_times[course]
            print(f"{course}\t{room}\t{instructor}\t{time}")
# Look up and display details for selected course input.
    elif choice == '2':
        course_number = input("Enter course number (e.g., CSC101): ")
        if course_number in course_rooms:
            print("Course Information:")
            print(f"  Room: {course_rooms[course_number]}")
            print(f"  Instructor: {course_instructors[course_number]}")
            print(f"  Time: {course_times[course_number]}")
        else:
            print("Error - no such course found. Please try again.")
# Exit the program.
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

