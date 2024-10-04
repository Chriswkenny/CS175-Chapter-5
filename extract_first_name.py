#Christopher Kenny
#CS 175
#Extract First Name Assignment

def main():
  full_name = input("Please enter your full name: ")
  first_name = extract_first_name(full_name)
  print(f"Your first name is: {first_name}")


def extract_first_name(full_name):
  first_name = full_name.split()
  return first_name[0]

main()
