#Christopher Kenny
#CS 175
#Nested Loops Assignment

#Get the range for the outer loop
outer_loop = int(input("Enter range of outside loop: "))
inner_loop = 4
total = 0

#Outer Loop Function
for i in range(outer_loop):
  input1 = int(input("Outer loop value: "))

#Inner Loop Function
  for i in range(inner_loop):
    inputs = int(input("Enter a number: "))
    total = inputs + total
    cycles = inner_loop * outer_loop

#Print Statements
print(f"Total Cycles: {cycles}")
print(f"Total: {total}")
