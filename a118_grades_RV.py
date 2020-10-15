#   a118_grades.py
my_courses = ["English", "Math", "CS"]


for course in my_courses:
    print(course)
    point = int(input("Enter your grade as a percentage: "))
    try:
        if point >= 90:
            print("You have an A")
        elif point >= 80:
            print("You have an B")
        elif point >= 70:
            print("You have an C")
        elif point >= 60:
            print("You have an D")
        else:
            print("You are failing")
    except:
        print("invalid input")
        course = my_courses[1]
    else:
        redo = input("do you want to redo your grades? (y/n)")
        if ( redo == "y"):
            course = my_courses[1]


