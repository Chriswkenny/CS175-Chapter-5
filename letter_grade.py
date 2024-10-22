#Christopher Kenny
#CS 175
#Letter Grade

def main():
  grade = get_grade()
  letter_grade(grade)



def get_grade():
  count = 0
  total_sum = 0
  while count != 3:
    grade = int(input("Enter a grade between 0 and 100: "))
    total_sum = total_sum + grade
    count = count + 1
  return total_sum


def letter_grade(percentage_grade):
  total_sum = percentage_grade
  letter_grade = float(total_sum/3)
  print(f"Your final grade percentage is {letter_grade}")
  if letter_grade >= 90:
    print("You passed with Grade A")
  elif letter_grade < 90 and letter_grade >= 80:
    print("You passed with Grade B")
  elif letter_grade < 80 and letter_grade >= 70:
    print("You passed with Grade C")
  elif letter_grade < 70 and letter_grade >= 60:
    print("You failed with Grade D")
  else:
    print("You failed with Grade F")

main()
