#Christopher Kenny
#CS 175
#Remove Empty Strings Assignment

#Lists
list1 = ['', '  a  ', 'b', ' ', 'c  ']
list2 = ['d', '    ', ' efg', 'h i']
list3 = ['j k', 'lm', '        ', 'n o', '']

#Create Function
def new_list(list1):
  newList = []
  for x in list1:
    if x.strip() != '' :
      newList.append(x)
  return newList

#Call Function
print(new_list(list1))
print(new_list(list2))
print(new_list(list3))
