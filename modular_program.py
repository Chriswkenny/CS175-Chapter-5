#Christopher Kenny
#CS 175
#Modular Program Assignment

#Main Function to run Grade Input/Calculation
def main():
  Assignment1_grade = get_grade()
  Assignment2_grade = get_grade()
  Assignment3_grade = get_grade()
  percentage_grade = (Assignment1_grade + Assignment2_grade + Assignment3_grade) / 3
  letter_grade(percentage_grade)

#User Inputs Grades
def get_grade():
  grades = int(input("Enter a grade between 0 and 100: "))
  return grades

#Display Grade Average and Letter Grade
def letter_grade(percentage_grade):
  print(f"Your final grade percentage is {percentage_grade}")
  if percentage_grade >= 92:
    print("You passed with a grade A")
  elif percentage_grade >= 85:
    print("You passed with a grade B")
  elif percentage_grade >= 70:
    print("You passed with a grade C")
  elif percentage_grade >= 60:
    print("You failed with a grade D")
  else:
    print("You failed with a grade F")

#Print
main()
