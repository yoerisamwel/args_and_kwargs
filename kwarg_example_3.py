def student_info(**kwargs):
    # Initializes a internal dictionary to store student information
    student_data = {
        'name': kwargs.get('name','John Doe'),
        'age': kwargs.get('age',18),
        'courses': kwargs.get('courses',[]),
        'grades': kwargs.get('grades',{}),
    }

# Add a new course and grade to the students record
    def add_course(course,grade):
        student_data['courses'].append(course)
        student_data['grades'][course] = grade

    # displays the students information
    def display_info():
        print(f"Name: {student_data['name']}")
        print(f"Age: {student_data['age']}")
        print("courses")
        for course, grade in student_data['grades'].items():
            print(f"{course}: {grade}")
    return add_course, display_info



if __name__ == "__main__":
# create a student record and get the inner function
    add_course_func, display_info_func = student_info(name="Alice", age=20)
# Add courses and grades to the students record
    add_course_func("Math",95)
    add_course_func("History",80)
# Display students information
    display_info_func()

