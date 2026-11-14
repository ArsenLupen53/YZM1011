"""
Task 8 – Course Enrollments:
Given a list of (student, course) tuples, use sets to print the distinct students, the distinct courses,
the students who take both "Math" and "Physics", and the students who take "Math" but not "Physics",
each as a sorted list.
"""



def enrollment_report(record):
    students = set()
    courses = set()
    math = set()
    physics = set()

    for info in record:
        name,course = info
        students.add(name)
        courses.add(course)

        if course=="Math":
            math.add(name)
        elif course=="Physics":
            physics.add(name)
        
    print(f"Students: {sorted(students)}")
    print(f"Course: {sorted(courses)}")
    print(f"Math abd Physics {sorted(math & physics)}")
    print(f"Math only {sorted(math - physics)}")

    
record = [("Ada","Math"),("Mert","Physics"),("Ada","Physics"),
          ("Ece","Math"),("Mert","Physics"),("Can","Art")]

enrollment_report(record)

        
