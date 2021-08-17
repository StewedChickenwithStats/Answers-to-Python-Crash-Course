people=['mom','dad','sister']
print("Now there will be a larger dining-table.")
people.insert(0,'brother')
people.insert(2,'friend')
people.append('teacher')
print("Now you can only invite two guests.")
delete_1=people.pop()
print("Dear "+delete_1+", I am sorry to tell you that I have to cancel the dinner plan.")
delete_2=people.pop()
delete_3=people.pop()
print("Dear "+delete_3+", I am sorry to tell you that I have to cancel the dinner plan.")
print("Dear "+people[0]+", please attend dinner as planned.")
print("Dear "+people[1]+", please attend dinner as planned.")
del people[0]
del people[0]
del people[0]
print("Now print the list:")
print(people)