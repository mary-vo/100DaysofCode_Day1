######## Notes from lecture
List: data structure, a way to organize and storing data in Python

We use variable to store one piece of data, for example:
a = 3
b = "hello"
When you need to store grouped pieces of data; data that has some sort of connectionw ith each other. For example, if you wanted to store all names of states in the US, it won't make sense to store them individually, since they sort of belong together, they have a relationship to each other. It would be if you had a variable called states_in_US, and you can store all the names of the states in one variable. Or perhaps you want to maintain order, for example a list of individuals in line. You may want to keep their order so that the last person does not jump the line. Introducing lists...

fruits = [item1, item2]
In python, LISTS always starts and end with square brackets []. In between, you have items separated by commas. Order is determined by the order in the list.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]


To reference an item in the list, you can indicate the index/offset of the item you want in brackets

print(states_of_america[2])

If I use negative index, it will start counting from the end of the list:
print(states_of_america[-1])

So far, we have only fetched data from a list based on indeces. We can also grab a hold of an item from the list and change/alter it:
states_of_america[1] = "Pencilvania"
print(states_of_america)

You can add to the list:
states_of_america.append("Lunaland")
print(states_of_america)

states_of_america.extend(["Kittyland", "Sorinland"])
print(states_of_america)

More things you can do with lists:
https://docs.python.org/3/tutorial/datastructures.html

######## Exercise - 
