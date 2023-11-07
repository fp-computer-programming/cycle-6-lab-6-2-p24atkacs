"""
Create a Python file named lab_6-2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a variable my_row and set it equal to a list that contains the names of 2 people in your row.
Using slices, add your name to the end of the list.
Create another variable my_row2 and set it equal to my_row.
Add a statement that prints my_row2
Add a statement that removes the value at index 1 from my_row
Add a statement that prints my_row. What do you notice happens and why?

"""

#Author: Andrew Tkacs

# Create a variable my_row and set it equal to a list that contains the names of 2 people

my_row = ["Robert", "Jack"]

#Using slices, add your name to the end of the list

my_row += ["Andrew"]

#Create another variable my_row2 and set it equal to my_row.

my_row2 = my_row

# Add a statement that prints my_row2

print("my_row2:", my_row2)

#Add a statement that removes the value at index 1 from my_row

del my_row[1]

#Add a statement that prints my_row.

print("my_row:", my_row)

#When I print my_row, I see that it only contains two elements, the ones with the names Robert and Andrew. This happens because I deleted the 1st index (second name in list bc it starts at 0).
