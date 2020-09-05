# Author: Sarthak Singh sxs6666@psu.print

grade1 = (input(f"Enter your course 1 letter grade: "))
credit1 = (input(f"Enter your course 1 credit: "))


if grade1 == "A":
    grade1 = float(4.0)
    print(f"Grade point for course 1 is: {grade1}")
elif grade1 == "A-":
    grade1 = float(3.67)
    print(f"Grade point for course 1 is: {grade1}") 
elif grade1 == "B+":
    grade1 = float(3.33)
    print(f"Grade point for course 1 is: {grade1}")

elif grade1 == "B":
    grade1 = float(3.0)
    print(f"Grade point for course 1 is: {grade1}")
elif grade1 == "B-":
    grade1 = float(2.67)
    print(f"Grade point for course 1 is: {grade1}")
  
elif grade1 == "C+":
    grade1 = float(2.33)
    print(f"Grade point for course 1 is: {grade1}")
    
elif grade1 == "C":
    grade1 = float(2.0)
    print(f"Grade point for course 1 is: {grade1}")

    
elif grade1 == "D":
    grade1 = float(1.0)
    print(f"Grade point for course 1 is: {grade1}")
else:
    grade1 = float(0.0)
    print(f"Grade point for course 1 is: 0.0")




grade2 = (input(f"Enter your course 2 letter grade: "))
credit2 = (input(f"Enter your course 2 credit: "))


if grade2 == "A":
    grade2 = float(4.0)
    print(f"Grade point for course 2 is: {grade2}")
elif grade2 == "A-":
    grade2 = float(3.67)
    print(f"Grade point for course 2 is: {grade2}") 
elif grade2 == "B+":
    grade2 = float(3.33)
    print(f"Grade point for course 2 is: {grade2}")

elif grade2 == "B":
    grade2 = float(3.0)
    print(f"Grade point for course 2 is: {grade2}")
elif grade2 == "B-":
    grade2 = float(2.67)
    print(f"Grade point for course 2 is: {grade2}")
  
elif grade2 == "C+":
    grade2 = float(2.33)
    print(f"Grade point for course 2 is: {grade2}")
    
elif grade2 == "C":
    grade2 = float(2.0)
    print(f"Grade point for course 2 is: {grade2}")

elif grade2 == "D":
    grade2 = float(1.0)
    print(f"Grade point for course 2 is: {grade2}")
else:
    grade2 = float(0.0)
    print(f"Grade point for course 2 is: 0.0")

  

grade3 = (input(f"Enter your course 3 letter grade: "))
credit3 = (input(f"Enter your course 3 credit: "))


if grade3 == "A":
    grade3 = float(4.0)
    print(f"Grade point for course 3 is: {grade3}")
elif grade3 == "A-":
    grade3 = float(3.67)
    print(f"Grade point for course 3 is: {grade3}") 
elif grade3 == "B+":
    grade3 = float(3.33)
    print(f"Grade point for course 3 is: {grade3}")

elif grade3 == "B":
    grade3 = float(3.0)
    print(f"Grade point for course 3 is: {grade3}")
elif grade3 == "B-":
    grade3 = float(2.67)
    print(f"Grade point for course 3 is: {grade3}")
  
elif grade3 == "C+":
    grade3 = float(2.33)
    print(f"Grade point for course 3 is: {grade3}")
    
elif grade3 == "C":
    grade3 = float(2.0)
    print(f"Grade point for course 3 is: {grade3}")

    
elif grade3 == "D":
    grade3 = float(1.0)
    print(f"Grade point for course 3 is: {grade3}")
else:
    grade3 = float(0.0)
    print(f"Grade point for course 3 is: 0.0")




GPA = (grade1 * int(credit1) + grade2 * int(credit2) + grade3 * int(credit3)) / (int(credit1) + int(credit2) +  int(credit3))

print(f"Your GPA is: {GPA}")



#GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 